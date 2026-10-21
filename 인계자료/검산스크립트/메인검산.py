"""메인 독립 검산: 7절 기준 5·6·8 + JSON·현지화·그림목록 정합성.
사용: python3 -I 메인검산.py A|B
"""
import json
import re
import sys
from collections import Counter

import os
_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R = os.path.join(_ROOT, 'results') + '/'
W = os.path.join(_ROOT, '인계자료', '장면순서') + '/'
EP = {
    'A': dict(n='001_모기터짐', s='02_대본_001_모기터짐_영어v3.md', j='편A_장면순서.json', lo=662, hi=760, pre='P03-'),
    'B': dict(n='002_풍선껌자동차', s='02_대본_002_풍선껌자동차_영어v2.md', j='편B_장면순서.json', lo=650, hi=760, pre='GUM-'),
}[sys.argv[1]]
MAT = ['실사', '실영상', '도해', '문서', '생성 그림', '움직이는 클립']
MOVING = {'실영상', '움직이는 클립'}


def read(p):
    return open(p, encoding='utf-8').read()


def tables(text):
    """마크다운 표들을 (머리줄, 행 목록)으로."""
    out, cur = [], None
    for line in text.splitlines():
        if line.strip().startswith('|'):
            cells = [c.strip() for c in line.strip().strip('|').split('|')]
            if cur is None:
                cur = [cells, []]
            elif set(''.join(cells)) <= set('-: '):
                continue
            else:
                cur[1].append(cells)
        else:
            if cur:
                out.append(cur)
            cur = None
    if cur:
        out.append(cur)
    return out


def find_table(text, *keys):
    for h, rows in tables(text):
        if all(any(k in c for c in h) for k in keys):
            return h, rows
    return None, []


def col(h, key):
    return next(i for i, c in enumerate(h) if key in c)


# 5. 낭독 분량
s = read(R + EP['s'])
blk = re.search(r'```text\n(.*?)```', s[s.index('**[낭독본 (영어)]**'):], re.S).group(1)
lines = [l.strip() for l in blk.splitlines() if l.strip()]
words = len(' '.join(lines).split())
print(f'[5] 단어 {words} (범위 {EP["lo"]}-{EP["hi"]}) ->', '맞음' if EP['lo'] <= words <= EP['hi'] else '어김')

# JSON 정본 vs 대본
js = json.load(open(W + EP['j'], encoding='utf-8'))
ids = [x['id'] for x in js]
print('[JSON] 장면', len(js), '대본과 일치', ' '.join(x['text'] for x in js).split() == ' '.join(lines).split())

# 04 장면표
t4 = read(R + f'04_장면_{EP["n"]}.md')
m4 = re.search(r'```json\n(.*?)```', t4, re.S)
if m4:
    print('[04 JSON] 정본과 같음', json.loads(m4.group(1)) == js)
h, rows = find_table(t4, '장면 id', '시간', '컷')
rows = [r for r in rows if r[0].startswith(EP['pre'])]
ci, ct, cc, cm, cv, cq = (col(h, k) for k in ('장면 id', '시간', '컷', '재료', '움직임', '궁금증'))
print('[04] 행', len(rows), 'id 순서 일치', [r[ci] for r in rows] == ids)
prev_end, gaps, cuts, mats, moving, q = 0, [], [], [], 0, 0
for r in rows:
    a, b = map(int, re.findall(r'\d+', r[ct])[:2])
    if a != prev_end:
        gaps.append((r[ci], prev_end, a))
    prev_end = b
    n = int(re.findall(r'\d+', r[cc])[0])
    for k in range(n):
        cuts.append(a + (b - a) * k / n)
    m = r[cm]
    mats.append(m)
    if m not in MAT:
        print('  재료 6종 밖:', r[ci], m)
    # 움직이는 장면: 컷 내역이 있으면 그것으로, 없으면 재료 칸으로
    det = re.search(r'\[컷:([^\]]*)\]', r[cv])
    if det:
        mv = sum(int(x) for name, x in re.findall(r'(실영상|움직이는 클립)\s*(\d+)', det.group(1)))
        is_mv = mv * 2 >= n
    else:
        is_mv = m in MOVING
    moving += is_mv
    q += '○' in r[cq]
total = prev_end
print('[04] 총 길이', total, '초', '빈틈/겹침', gaps or '없음')
wins = Counter(int(c // 30) for c in cuts)
bad = []
for w in range(int((total - 1) // 30) + 1):
    span = min(30, total - w * 30)
    lo, hi = 6 * span / 30, 10 * span / 30
    if not (lo - 0.5 <= wins[w] <= hi + 0.5):
        bad.append((f'{w*30}-{w*30+span}', wins[w]))
print('[6] 30초 구간 컷', [wins[w] for w in sorted(wins)], '범위 밖', bad or '없음')
run, mx = 1, 1
for i in range(1, len(mats)):
    run = run + 1 if mats[i] == mats[i - 1] else 1
    mx = max(mx, run)
print('[6] 같은 재료 최대 연속', mx, '->', '맞음' if mx < 3 else '어김')
print(f'[8] 움직이는 장면 {moving}/{len(rows)} = {moving/len(rows)*100:.1f}% ->', '맞음' if moving / len(rows) >= 0.3 else '어김')
print('[2] 궁금증 갱신 ○', q, '->', '맞음' if q >= 3 else '어김')
print('[10] 썸네일 항목 위치', '파일 끝 쪽' if t4.rfind('썸네일') > len(t4) * 0.8 else '확인 필요')

# 완성 화면 id 사용 횟수 (04 전체 + 05 전체에서 장면별로)
pfx = 'A-SH' if EP['pre'] == 'P03-' else 'B-SH'
use = Counter()
for r in rows:
    for sid in set(re.findall(pfx + r'\d+', ' '.join(r))):
        use[sid] += 1
print('[6] 완성 화면 최대 사용(04 기준)', use.most_common(3))

# 05 그림목록
t5 = read(R + f'05_그림목록_{EP["n"]}.md')
h5, r5 = find_table(t5, '장면 id', '장수', '금지')
r5 = [r for r in r5 if r[0].startswith(EP['pre'])]
print('[7] 05 행', len(r5), 'id 일치', [r[0] for r in r5] == ids, '빈 칸 행', [r[0] for r in r5 if any(not c for c in r)])
hl, rl = find_table(t5, '자료', '라이선스', '장면 id')
lic_ids = set(re.findall(EP['pre'] + r'\d+', ' '.join(' '.join(r) for r in rl)))
ext = [r[ci] for r in rows if r[cm] in ('실사', '실영상', '문서')]
print('[7] 라이선스 표 행', len(rl), '외부 재료 장면', len(ext), '표에 없는 외부 장면', [e for e in ext if e not in lic_ids])

# 03 현지화
t3 = read(R + f'03_현지화_{EP["n"]}.md')
h3, r3 = find_table(t3, '장면 id', '영어', '한국어')
r3 = [r for r in r3 if r[0].startswith(EP['pre'])]
print('[9] 03 행', len(r3), 'id 일치', [r[0] for r in r3] == ids,
      '영어 칸=JSON', all(a[1].split() == b['text'].split() for a, b in zip(r3, js)))
