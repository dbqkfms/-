# 사용: python3 -I check04.py <04_장면 파일>
# 9-9 장면표(행 = 컷 하나, id는 모두 '장면id-컷번호')를 읽어 10번 통과 기준 2·7·8·10과 JSON 블록을 집계한다.
import re, sys, json, math
from collections import Counter, OrderedDict
MATS = ['실사', '도해', '실영상', '생성 그림', '움직이는 클립', '문서']
TARGET = {'실사': 25, '도해': 25, '실영상': 15, '생성 그림': 15, '움직이는 클립': 12, '문서': 8}
MOVING = {'실영상', '움직이는 클립'}
src = open(sys.argv[1], encoding='utf-8').read()
rows, header = [], None
for line in src.splitlines():
    s = line.strip()
    if not s.startswith('|'): header = None if not s else header; continue
    cells = [c.strip() for c in s.strip('|').split('|')]
    if '화면 재료' in cells and any('시간' in c for c in cells): header = cells; continue
    if header is None or set(''.join(cells)) <= set('-: '): continue
    if len(cells) != len(header): print('열 수 불일치 행:', s[:100]); continue
    rows.append(dict(zip(header, cells)))
def col(r, key): return next((v for k, v in r.items() if key in k), '')
cuts = []
for r in rows:
    cid = col(r, '장면 id').strip('` ')
    t = re.match(r'\s*(\d+(?:\.\d+)?)\s*[-–]\s*(\d+(?:\.\d+)?)', col(r, '시간'))
    cuts.append(dict(id=cid, scene=re.sub(r'-\d+$', '', cid), has_suffix=bool(re.search(r'-\d+$', cid)),
                     t0=float(t.group(1)) if t else None, t1=float(t.group(2)) if t else None,
                     mat=col(r, '화면 재료'), motion=col(r, '움직임'), q=col(r, '궁금증')))
n = len(cuts)
print(f'컷 수: {n}  (기준 150–200) -> {"맞음" if 150 <= n <= 200 else "어김"}')
bad_id = [c['id'] for c in cuts if not c['has_suffix']]
if bad_id: print(f'컷 번호(-N) 없는 id {len(bad_id)}개: {bad_id[:10]}')
bad_mat = [(c['id'], c['mat']) for c in cuts if c['mat'] not in MATS]
print('6종 밖 화면 재료:', bad_mat[:10] if bad_mat else '없음')
cnt = Counter(c['mat'] for c in cuts)
print('화면 재료별 컷 수 (출발 배합 ±5%p):')
for m in MATS:
    p = 100 * cnt[m] / n if n else 0
    ok = abs(p - TARGET[m]) <= 5 and not (m == '생성 그림' and p > 20)
    print(f'  {m}: {cnt[m]}컷 {p:.1f}% (출발 {TARGET[m]}%) -> {"맞음" if ok else "어긋남"}')
run, best, where = 1, 1, ''
for a, b in zip(cuts, cuts[1:]):
    run = run + 1 if a['mat'] == b['mat'] else 1
    if run > best: best, where = run, b['id']
print(f'같은 화면 재료 최장 연속: {best}컷 (끝 {where}) -> {"맞음" if best <= 2 else "어김(3연속 이상)"}')
scenes = OrderedDict()
for c in cuts: scenes.setdefault(c['scene'], []).append(c)
mv = [s for s, cs in scenes.items() if sum(c['mat'] in MOVING for c in cs) * 2 >= len(cs)]
ns = len(scenes)
print(f'장면 수: {ns}  움직이는 장면: {len(mv)} = {100*len(mv)/ns if ns else 0:.1f}% (기준 30% 이상) -> {"맞음" if ns and len(mv)/ns >= 0.3 else "어김"}')
no_motion = [c['id'] for c in cuts if c['motion'] in ('', '-', '—')]
print('움직임 한 줄 빈 컷:', no_motion[:10] if no_motion else '없음')
q = [c['id'] for c in cuts if '○' in c['q']]
print(f'궁금증 갱신(○) 표시: {len(q)}곳 {q} -> {"맞음" if len(q) >= 3 else "어김"}')
timed = [c for c in cuts if c['t0'] is not None]
if len(timed) != n: print(f'시간 형식 못 읽은 컷: {n-len(timed)}개')
gaps = [(a['id'], a['t1'], b['id'], b['t0']) for a, b in zip(timed, timed[1:]) if abs(a['t1'] - b['t0']) > 0.01]
print('시간 끊김/겹침:', gaps[:8] if gaps else '없음')
if timed:
    end = max(c['t1'] for c in timed)
    print(f'총 길이: {end:.0f}초 ({end/60:.2f}분)')
    wins = []
    for w in range(math.ceil(end / 30)):
        k = sum(1 for c in timed if w*30 <= c['t0'] < (w+1)*30)
        span = min(30, end - w*30)
        wins.append((w*30, k, span))
    off = [(s, k) for s, k, span in wins if span >= 20 and not (8 <= k <= 12)]
    print('30초 구간별 교체 수:', ' '.join(f'{s}s:{k}' for s, k, _ in wins))
    print('8–12 범위 밖 구간(20초 미만 끝 구간 제외):', off if off else '없음')
jb = re.search(r'```json\s*\n(.*?)```', src, re.S)
if not jb: print('장면순서 JSON 블록: 없음 -> 어김')
else:
    try:
        arr = json.loads(jb.group(1)); ids = [a['id'] for a in arr]
        miss = [s for s in scenes if s not in ids]; extra = [i for i in ids if i not in scenes]
        wc = sum(len([w for w in a['text'].split() if re.search(r'[A-Za-z0-9]', w)]) for a in arr)
        print(f'장면순서 JSON: {len(arr)}개 항목, 단어 {wc}. 장면표에만 있는 id: {miss[:10] or "없음"} / JSON에만 있는 id: {extra[:10] or "없음"}')
    except Exception as e: print('장면순서 JSON 파싱 실패:', e)
print('썸네일 항목:', '있음' if re.search(r'썸네일', src.split('\n')[-80:] and '\n'.join(src.split('\n')[-80:])) else '없음(맨 아래 80줄 안)')
