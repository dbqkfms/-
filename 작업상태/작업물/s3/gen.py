import json, re, sys, math
from collections import Counter, OrderedDict
sys.path.insert(0, '.')
from plan import PLAN
import patch
MAT = {'P': '실사', 'V': '실영상', 'D': '도해', 'C': '문서', 'G': '생성 그림', 'M': '움직이는 클립'}
WPM = 165.0
a4 = json.load(open('a4.json'))
def wc(s): return len([w for w in s.split() if re.search(r'[A-Za-z0-9]', w)])
rows = []; t = 0.0; problems = []
for sc in a4:
    sid = sc['id']; cuts = PLAN.get(sid)
    if not cuts: problems.append(('계획 없음', sid)); continue
    dur = wc(sc['text']) / WPM * 60 + sc.get('silent_sec', 0)
    if sid not in ('T02a',) and sc['text']:
        joined = ' '.join(c[1] for c in cuts)
        if joined != sc['text']: problems.append(('구절 불일치', sid, joined, sc['text']))
    ws = []
    for c in cuts:
        if len(c) > 4: ws.append(c[4])
        else: ws.append(max(wc(c[1]), 1.6) if sc['text'] else 1)
    tot = sum(ws); acc = 0
    for i, c in enumerate(cuts):
        t0 = t + dur * acc / tot; acc += ws[i]; t1 = t + dur * acc / tot
        rows.append(dict(id=f'{sid}-{i+1}', scene=sid, n=len(cuts), mat=MAT[c[0]], code=c[0], frag=c[1], mot=c[2], q=c[3], t0=t0, t1=t1))
    t += dur
# round boundaries once
for r in rows: r['a'] = round(r['t0'], 1); r['b'] = round(r['t1'], 1)
for x, y in zip(rows, rows[1:]): y['a'] = x['b']
def stats():
    n = len(rows); cnt = Counter(r['mat'] for r in rows)
    print('컷', n, {k: (cnt[v], round(100*cnt[v]/n, 1)) for k, v in MAT.items()})
    run = 1; best = 1
    for x, y in zip(rows, rows[1:]):
        run = run + 1 if x['mat'] == y['mat'] else 1
        if run >= 3: print('  3연속', y['id'], y['mat'])
    sc = OrderedDict()
    for r in rows: sc.setdefault(r['scene'], []).append(r)
    mv = [s for s, cs in sc.items() if sum(c['code'] in 'VM' for c in cs) * 2 >= len(cs)]
    print('장면', len(sc), '움직이는', len(mv), round(100*len(mv)/len(sc), 1))
    end = rows[-1]['b']; wins = []
    for w in range(math.ceil(end/30)):
        k = sum(1 for r in rows if w*30 <= r['a'] < (w+1)*30); wins.append(k)
    print('30초 창', wins, '끝', end)
    # 실영상 간격
    vi = [i for i, r in enumerate(rows) if r['code'] == 'V']
    gaps = [(rows[a]['id'], rows[b]['id'], b-a-1) for a, b in zip(vi, vi[1:]) if b-a-1 < 3]
    print('실영상 사이 3컷 미만:', gaps)
    ids = Counter(m for r in rows for m in re.findall(r'(?:RS|P)_?\d+[a-z]?(?:_r\d)?', r['mot']) if r['code'] in 'GM')
    print('같은 그림 3회 이상:', [k for k, v in ids.items() if v > 2])
    short = [(r['id'], round(r['b']-r['a'], 2)) for r in rows if r['b']-r['a'] < 0.5]
    print('0.5초 미만 컷:', short)
    return mv
if __name__ == '__main__':
    for p in problems: print(p)
    stats()

def table():
    out = ['| 장면 id | 시간(초) | 컷 수 | 화면 재료 | 내레이션 구절 | 움직임 한 줄 | 궁금증 갱신 |', '|---|---|---|---|---|---|---|']
    for r in rows:
        if 'Tesla 짧은 인용' in r['mot']:
            r['mot'] = re.sub(r'약 [\d.]+초', f"{r['b']-r['a']:.1f}초", r['mot'])
        out.append(f"| {r['id']} | {r['a']:.1f}-{r['b']:.1f} | {r['n']} | {r['mat']} | {r['frag']} | {r['mot']} | {'○' if r['q'] else '—'} |")
    return '\n'.join(out)
def scenes():
    sc = OrderedDict()
    for r in rows: sc.setdefault(r['scene'], []).append(r)
    return sc
