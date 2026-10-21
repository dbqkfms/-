# 결과 파일(04·05·06)을 직접 읽어 다시 검산한다 — 스펙을 거치지 않는 독립 확인
import re, json, math, collections, sys
R = '/home/user/-/results/'
J = '/tmp/claude-0/-home-user--/f74f8fd9-d08b-56d5-a2e9-6c58b1e53757/scratchpad/작업/편A_장면순서.json'
t4 = open(R + '04_장면_001_모기터짐.md', encoding='utf-8').read()
t5 = open(R + '05_그림목록_001_모기터짐.md', encoding='utf-8').read()
t6 = open(R + '06_모션계획_001_모기터짐.md', encoding='utf-8').read()
MATS = ['실사', '실영상', '도해', '문서', '생성 그림', '움직이는 클립']
rows = [l for l in t4.split('\n') if re.match(r'^\| P03-\d\d \| \d+-\d+ \|', l)]
assert len(rows) == 67, len(rows)
jd = json.load(open(J, encoding='utf-8'))
prev = 0; recs = []
for l, j in zip(rows, jd):
    c = [x.strip() for x in l.strip('|').split('|')]
    sid, tm, n, mat, narr, mv, ref = c[0], c[1], int(c[2]), c[3], c[4], c[5], c[6]
    a, b = map(int, tm.split('-'))
    assert sid == j['id'] and narr == j['text'], sid
    assert a == prev and b > a, sid
    assert mat in MATS, mat
    prev = b
    m = re.search(r'\[컷: ([^\]]+)\]', mv)
    if m:
        parts = [re.match(r'(.+?)(\d+)$', p).groups() for p in m.group(1).split('·')]
        cuts = [(k, int(v)) for k, v in parts]
    else:
        cuts = [(mat, n)]
    assert sum(v for _, v in cuts) == n, sid
    top = max(v for _, v in cuts)
    assert dict(cuts).get(mat) == top, ('label not majority', sid)
    mov = sum(v for k, v in cuts if k in ('실영상', '움직이는 클립'))
    ids = re.findall(r'A-SH\d{3}', mv)
    assert len(ids) == n, (sid, ids)
    recs.append(dict(id=sid, a=a, b=b, n=n, mat=mat, moving=mov * 2 >= n, ids=ids, ref=ref, mv=mv))
total = prev
nb = math.ceil(total / 30); bins = [0] * nb
for r in recs:
    for k in range(r['n']):
        bins[min(int((r['a'] + k * (r['b'] - r['a']) / r['n']) // 30), nb - 1)] += 1
run = 1; maxrun = 1
for i in range(1, 67):
    run = run + 1 if recs[i]['mat'] == recs[i - 1]['mat'] else 1
    maxrun = max(maxrun, run)
use = collections.defaultdict(set)
for r in recs:
    for i in r['ids']: use[i].add(r['id'])
mv = sum(r['moving'] for r in recs)
refresh = [r['id'] for r in recs if r['ref'] == '○']
print('total', total, '<=295', total <= 295)
for i, b in enumerate(bins):
    lo, hi = i * 30, min(i * 30 + 30, total); span = hi - lo
    mn, mx = (6, 10) if span >= 30 else (math.ceil(6 * span / 30), math.floor(10 * span / 30))
    print('  bin %d-%d: %d (%d-%d) %s' % (lo, hi, b, mn, mx, mn <= b <= mx))
print('maxrun', maxrun, 'moving %d/67 = %.1f%%' % (mv, 100 * mv / 67), 'maxuse', max(len(v) for v in use.values()), 'ids', len(use))
print('refresh', refresh)
# 05: 67행, 06: 움직이는 장면 수와 같은 행 수
r5 = [l for l in t5.split('\n') if re.match(r'^\| P03-\d\d \| ', l)]
r6 = [l for l in t6.split('\n') if re.match(r'^\| P03-\d\d \| ', l)]
s6 = [l for l in t6.split('\n') if re.match(r'^- P03-\d\d ', l)]
print('05 rows', len(r5), '06 moving rows', len(r6), '06 static bullets', len(s6), 'moving match', len(r6) == mv, len(r6) + len(s6) == 67)
mov_ids = {r['id'] for r in recs if r['moving']}
print('06 ids == moving ids', {l.split('|')[1].strip() for l in r6} == mov_ids)
# 05 재료 칸 == 04 재료 칸
m4 = {r['id']: r['mat'] for r in recs}
print('05 mat == 04 mat', all(m4[l.split('|')[1].strip()] == l.split('|')[2].strip() for l in r5))
# 외부 재료 장면이 라이선스 표에 있는지
ext = [r['id'] for r in recs if re.search(r'←L\d', r['mv'])]
lic = t5[t5.index('## 라이선스 표'):]
print('external scenes', ext, 'all in license table', all(e in lic for e in ext))
# 05 사전에 모든 id
print('dict has all ids', all(('| %s |' % i) in t5 for i in use))
# 썸네일은 04 맨 아래 한 곳
print('thumb sections', t4.count('## 썸네일'), 'last section is thumb', t4.rstrip().rfind('## 썸네일') > t4.rfind('## 검산'))
print('json block verbatim', open(J, encoding='utf-8').read().rstrip('\n') in t4)
