# 편 A 장면표 검산: 시간·30초 구간 컷 수·재료 연속·움직이는 장면 비율·완성 화면 재사용·마스코트 공백
import json, math, os, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
JSON = os.path.join(os.path.dirname(HERE), '편A_장면순서.json')
ns = {}
exec(open(os.path.join(HERE, 'spec.py'), encoding='utf-8').read(), ns)
S, MAT, MOVING = ns['S'], ns['MAT'], ns['MOVING']

WPS = 2.7      # 낭독 어림 (공통지침)
PAUSE = 0.35   # 장면 사이 숨 (02와 같은 값)
MIN_SEC = 2

def load():
    d = json.load(open(JSON, encoding='utf-8'))
    assert [x['id'] for x in d] == [s['id'] for s in S], 'id mismatch'
    return d

def build():
    d = load()
    # 연속 시간 → 정수 경계(누적 반올림, 장면 최소 2초)
    t = 0.0; bounds = [0]
    for x, s in zip(d, S):
        w = len(x['text'].split())
        t += w / WPS + PAUSE + s['beat']
        b = int(round(t))
        if b - bounds[-1] < MIN_SEC:
            b = bounds[-1] + MIN_SEC
        bounds.append(b)
    rows = []
    ids = {}; n = 0
    for i, (x, s) in enumerate(zip(d, S)):
        st, en = bounds[i], bounds[i + 1]
        cuts = []
        for c in s['cuts']:
            mat, key, masc = c[0], c[1], c[2]
            ext = c[3] if len(c) > 3 else None
            if key not in ids:
                n += 1; ids[key] = 'A-SH%03d' % n; new = True
            else:
                new = False
            cuts.append(dict(mat=mat, key=key, sid=ids[key], masc=masc, ext=ext, new=new))
        cnt = collections.Counter(c['mat'] for c in cuts)
        top = max(cnt.values())
        tied = [m for m in cnt if cnt[m] == top]
        # 동률이면 장면을 여는 첫 컷의 재료
        label = cuts[0]['mat'] if len(tied) > 1 and cuts[0]['mat'] in tied else [m for m in cnt if cnt[m] == top][0]
        if len(tied) > 1:
            label = next(c['mat'] for c in cuts if c['mat'] in tied)
        mov = sum(1 for c in cuts if c['mat'] in MOVING)
        rows.append(dict(id=s['id'], text=x['text'], words=len(x['text'].split()), st=st, en=en,
                         cuts=cuts, label=label, tied=tied if len(tied) > 1 else None,
                         moving=(mov * 2 >= len(cuts)), spec=s))
    return rows

def checks(rows, verbose=True):
    out = []
    total = rows[-1]['en']
    out.append(('총 길이(초)', total, total <= 295))
    # 30초 구간
    nb = math.ceil(total / 30)
    bins = [0] * nb
    for r in rows:
        k = len(r['cuts']); dur = r['en'] - r['st']
        for j in range(k):
            cs = r['st'] + j * dur / k
            bins[min(int(cs // 30), nb - 1)] += 1
    binres = []
    for b in range(nb):
        lo, hi = b * 30, min((b + 1) * 30, total)
        span = hi - lo
        if span >= 30:
            mn, mx = 6, 10
        else:
            mn, mx = math.ceil(6 * span / 30), math.floor(10 * span / 30)
        binres.append((lo, hi, bins[b], mn, mx, mn <= bins[b] <= mx))
    # 재료 연속
    runs = []; cur = 1; best = 1
    for i in range(1, len(rows)):
        if rows[i]['label'] == rows[i - 1]['label']:
            cur += 1
        else:
            cur = 1
        best = max(best, cur)
        if cur >= 3:
            runs.append(rows[i]['id'])
    # 최악 읽기(동률을 어느 쪽으로 읽어도) 3연속 가능 지점
    worst = []
    for i in range(2, len(rows)):
        sets = []
        for r in rows[i - 2:i + 1]:
            sets.append(set(r['tied']) if r['tied'] else {r['label']})
        if sets[0] & sets[1] & sets[2]:
            worst.append(rows[i - 2]['id'] + '~' + rows[i]['id'])
    mv = sum(r['moving'] for r in rows)
    use = collections.defaultdict(set)
    for r in rows:
        for c in r['cuts']:
            use[c['sid']].add(r['id'])
    maxuse = max(len(v) for v in use.values())
    reused = {k: sorted(v) for k, v in use.items() if len(v) > 1}
    # 마스코트 없는 최장 구간
    gaps = []; gs = None
    for r in rows:
        k = len(r['cuts']); dur = r['en'] - r['st']
        for j, c in enumerate(r['cuts']):
            cs = r['st'] + j * dur / k; ce = cs + dur / k
            if not c['masc']:
                if gs is None: gs = cs
                ge = ce
            else:
                if gs is not None: gaps.append((ge - gs, gs, ge)); gs = None
    if gs is not None: gaps.append((ge - gs, gs, ge))
    gaps.sort(reverse=True)
    res = dict(total=total, bins=binres, runs=runs, maxrun=best, worst=worst, moving=mv,
               nscene=len(rows), maxuse=maxuse, reused=reused, gaps=gaps[:5],
               ncuts=sum(len(r['cuts']) for r in rows), nshots=len(use),
               ties=[r['id'] for r in rows if r['tied']])
    return res

if __name__ == '__main__':
    rows = build(); r = checks(rows)
    print('total', r['total'], 'cuts', r['ncuts'], 'shots', r['nshots'])
    for b in r['bins']: print('bin %d-%d: %d (허용 %d-%d) %s' % b)
    print('maxrun', r['maxrun'], 'runs>=3 at', r['runs'])
    print('worst-case tie runs', r['worst'])
    print('moving %d/%d = %.1f%%' % (r['moving'], r['nscene'], 100 * r['moving'] / r['nscene']))
    print('maxuse', r['maxuse'], r['reused'])
    print('mascot gaps (sec,start,end)', [(round(a, 1), round(b, 1), round(c, 1)) for a, b, c in r['gaps']])
    print('ties', r['ties'])
    print(' '.join('%s:%s%s' % (x['id'][-2:], x['label'], '*' if x['moving'] else '') for x in rows))
