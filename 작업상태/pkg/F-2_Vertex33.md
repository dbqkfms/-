### 부록 F-2. script_Vertex33_API.py.txt

```text
"""Vertex-only REST client. Explicit account/project; no provider/account fallback."""
import argparse
import base64
import datetime as dt
import json
import importlib.util
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

ACCOUNT='<계정: 로컬 설정 참조, 저장소에 넣지 않음>'
PROJECT='<프로젝트: 로컬 설정 참조, 저장소에 넣지 않음>'
LOCATION='global'
DEFAULT_MODEL='gemini-4-argon'
MAX_REQUEST_BYTES=18_000_000
MEDIA_MIME_TYPES={'.mp3':'audio/mpeg','.wav':'audio/wav','.m4a':'audio/mp4',
                  '.mp4':'video/mp4','.png':'image/png','.jpg':'image/jpeg'}
ROOT=Path(__file__).resolve().parent
GCLOUD=shutil.which('gcloud.cmd') or shutil.which('gcloud')

def vertex_authorization(model):
    path=Path(__file__).resolve().parents[2]/'운영관리/API_비용차단/google_api_cost_gate.py'
    spec=importlib.util.spec_from_file_location('vertex33_cost_gate',path)
    gate=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    return gate.require_free_google_call('google_vertex',PROJECT,model)

def sdk(*args):
    if not GCLOUD:raise RuntimeError('GCLOUD_NOT_INSTALLED')
    p=subprocess.run([GCLOUD,*args],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=180)
    if p.returncode:raise RuntimeError('GCLOUD_AUTH_NOT_READY_FOR_ACCOUNT33')
    return p.stdout.strip()

def status():
    accounts=json.loads(sdk('auth','list','--format=json(account,status)'))
    verified=[]
    for path in ROOT.glob('Vertex33_*_영수증.json'):
        try:
            r=json.loads(path.read_text(encoding='utf-8'))
            if (r.get('account')==ACCOUNT and r.get('project')==PROJECT and
                r.get('method')=='generateContent' and r.get('state')=='RESPONSE_RECEIVED' and
                r.get('http_status')==200 and r.get('text_chars',0)>0):verified.append(r)
        except (ValueError,OSError):pass
    latest=max(verified,key=lambda r:r.get('completed_at',''),default={})
    return {'route':'Vertex AI REST / OAuth','account':ACCOUNT,'project':PROJECT,'location':LOCATION,
            'account33_registered':any(a.get('account')==ACCOUNT for a in accounts),
            'active_sdk_account':next((a['account'] for a in accounts if a.get('status')=='ACTIVE'),None),
            'model_default':DEFAULT_MODEL,'generation_verified':bool(verified),
            'last_generation_verified_at':latest.get('completed_at'),
            'credit_settlement_verified':False,
            'note':'Credential registration is not proof of generation or free-credit settlement.'}

def request(args):
    model=args.model
    if not model.startswith('gemini-') or '/' in model:raise RuntimeError('GOOGLE_GEMINI_MODEL_ID_REQUIRED')
    major=model.removeprefix('gemini-').split('-')[0].split('.')[0]
    if not major.isdigit() or int(major)<3:raise RuntimeError('OLDER_MODEL_NOT_ALLOWED')
    text=Path(args.file).read_text(encoding='utf-8-sig') if args.file else args.prompt
    if not text:raise RuntimeError('PROMPT_REQUIRED')
    method='countTokens' if args.command=='count' else 'generateContent'
    endpoint=f'https://aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/{LOCATION}/publishers/google/models/{model}:{method}'
    parts=[]
    body={'contents':[{'role':'user','parts':parts}]}
    if method=='generateContent':
        body['generationConfig']={'maxOutputTokens':args.max_tokens,'thinkingConfig':{'thinkingLevel':'HIGH'}}
    rid=uuid.uuid4().hex
    receipt={'local_request_id':rid,'route':'Vertex AI REST / OAuth','account':ACCOUNT,'project':PROJECT,
             'location':LOCATION,'model':model,'method':method,'automatic_retries':0,
             'credit_settlement_verified':False,'started_at':dt.datetime.now(dt.timezone.utc).isoformat(),
             'state':'REQUEST_PREPARED'}
    receipt_path=ROOT/('Vertex33_'+rid+'_영수증.json')
    def save():receipt_path.write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
    save()
    try:
        receipt['media']=[]
        # Include base64 expansion, text, configuration and JSON overhead in the limit.
        for filename in args.media:
            path=Path(filename)
            mime=MEDIA_MIME_TYPES.get(path.suffix.lower())
            if not mime:raise RuntimeError('UNSUPPORTED_MEDIA_EXTENSION: '+path.suffix)
            size=path.stat().st_size
            if not path.is_file():raise RuntimeError('MEDIA_FILE_REQUIRED')
            if 4*((size+2)//3)>MAX_REQUEST_BYTES:
                raise RuntimeError('REQUEST_EXCEEDS_18MB: base64 media alone exceeds 18000000 bytes; no automatic trimming')
            # Bound reads even if a file grows after stat().
            with path.open('rb') as source:data=source.read(MAX_REQUEST_BYTES+1)
            parts.append({'inline_data':{'mimeType':mime,'data':base64.b64encode(data).decode('ascii')}})
            receipt['media'].append({'mimeType':mime,'bytes':len(data)})
            if len(json.dumps(body).encode('utf-8'))>MAX_REQUEST_BYTES:
                raise RuntimeError('REQUEST_EXCEEDS_18MB: serialized request exceeds 18000000 bytes; no automatic trimming')
        parts.append({'text':text})
        payload=json.dumps(body).encode('utf-8')
        receipt['request_bytes']=len(payload)
        if len(payload)>MAX_REQUEST_BYTES:
            raise RuntimeError('REQUEST_EXCEEDS_18MB: serialized request exceeds 18000000 bytes; no automatic trimming')
        save()
        receipt['authorization']=vertex_authorization(model)
        token=sdk('auth','print-access-token','--account='+ACCOUNT,'--quiet')
        if not token:raise RuntimeError('EMPTY_AUTH_TOKEN')
    except (OSError,RuntimeError,subprocess.TimeoutExpired) as e:
        receipt.update(state='NOT_EXECUTED',reason=str(e),
                       completed_at=dt.datetime.now(dt.timezone.utc).isoformat())
        save();print(json.dumps(receipt,ensure_ascii=True));raise SystemExit(1)
    req=urllib.request.Request(endpoint,data=payload,method='POST',
        headers={'Authorization':'Bearer '+token,'Content-Type':'application/json','x-goog-user-project':PROJECT})
    try:
        receipt['authorization']=vertex_authorization(model)
    except RuntimeError as error:
        token=None
        receipt.update(state='NOT_EXECUTED',reason=str(error),
                       completed_at=dt.datetime.now(dt.timezone.utc).isoformat())
        save();print(json.dumps(receipt,ensure_ascii=True));raise SystemExit(1)
    receipt['state']='REQUEST_SENT_OUTCOME_PENDING';save()
    try:
        with urllib.request.urlopen(req,timeout=180) as response:
            result=json.load(response);receipt['http_status']=response.status
        output='\n'.join(p.get('text','') for c in result.get('candidates',[]) for p in c.get('content',{}).get('parts',[]) if not p.get('thought'))
        receipt.update(state='RESPONSE_RECEIVED',response_id=result.get('responseId'),model_version=result.get('modelVersion'),
                       usage=result.get('usageMetadata'),text_chars=len(output),
                       finish_reasons=[c.get('finishReason') for c in result.get('candidates',[])])
        if method=='countTokens':receipt['token_count']=result.get('totalTokens')
        (ROOT/('Vertex33_'+rid+'_응답.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
        if method=='generateContent' and not output:receipt['state']='EMPTY_GENERATION_NOT_SUCCESS'
        if output:print(output)
    except urllib.error.HTTPError as e:
        try:err=json.loads(e.read().decode('utf-8',errors='replace')).get('error',{})
        except Exception:err={}
        receipt.update(state='PROVIDER_REJECTED',http_status=e.code,error_status=err.get('status'),
                       error_message=str(err.get('message','')).replace(token,'[REDACTED]'))
    except Exception as e:
        receipt.update(state='OUTCOME_UNKNOWN_NO_AUTOMATIC_RETRY',error_type=type(e).__name__)
    finally:
        token=None;receipt['completed_at']=dt.datetime.now(dt.timezone.utc).isoformat();save()
    print(json.dumps(receipt,ensure_ascii=True))

def main():
    p=argparse.ArgumentParser(description='33-account Vertex-only client; no paid Developer API fallback.')
    p.add_argument('command',choices=['status','count','ask'])
    p.add_argument('--prompt',default='')
    p.add_argument('--file')
    p.add_argument('--media',action='extend',nargs='+',default=[],metavar='PATH',
                   help='Media files (mp3/wav/m4a/mp4/png/jpg); repeatable; total JSON request <=18MB.')
    p.add_argument('--model',default=DEFAULT_MODEL)
    p.add_argument('--max-tokens',type=int,default=4096)
    a=p.parse_args()
    try:
        if a.command=='status':print(json.dumps(status(),ensure_ascii=True,indent=2))
        else:request(a)
    except Exception as e:
        print(json.dumps({'state':'NOT_EXECUTED','reason':str(e)},ensure_ascii=True));raise SystemExit(1)

if __name__=='__main__':main()
```
