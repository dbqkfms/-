# 편 1 04 장면표 재생성 (통합 서브). s3/plan.py + s3/patch.py(장면 서브 원본)를 읽고,
# v5.1 최종 문장과 검토(④⑤) 반영 화면 변경을 덧입혀 gen.py와 같은 방식으로 시간을 다시 잡는다.
import os, sys, re, json, math
from collections import Counter, OrderedDict
S3 = '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/s3'
OUT = '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1'
os.chdir(S3); sys.path.insert(0, S3)
from plan import PLAN
import patch  # noqa: F401  (PLAN을 v3로 바꿈)

MAT = {'P': '실사', 'V': '실영상', 'D': '도해', 'C': '문서', 'G': '생성 그림', 'M': '움직이는 클립'}
WPM = 165.0

# ---- v5.1 최종 문장 (02 낭독본과 같아야 함) ----
TEXT = {
 'T02a': "Plenty of people would just ask an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves.",
 'T18a': "Now freeze on my favorite frame, the car halfway over that Semi.",
 'T23': "Tesla's own patent shows fans under the car and skirts sealing the gap underneath.",
 'T44': "That's your seat shoving you forward with about four and a half times your own body weight. Hope your coffee had a lid.",
 'T53': "Tesla's own post lists Rocket as 'air ready, seats one.'",
 'T59': "I did some rough math, so treat it as an estimate. If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms, around four hundred seventy pounds.",
 'T60': "That's the weight of about two and a half adults, and it's all gas.",
 'T69': "Refilling the tanks reportedly takes hours, with a goal of about half an hour.",
 'T70': "In those hours, you could make dinner, eat dinner, and do the dishes.",
 'T84g': "I'll admit it, that was a hell of a demo.",
}

# ---- 컷 계획 변경 ----
TQ = 'Tesla 짧은 인용'
def setmot(sid, i, mot):
    c = list(PLAN[sid][i]); c[2] = mot; PLAN[sid][i] = tuple(c)

setmot('T01', 1, "실사: Commons Tesla Semi 사진 — 3% 밀어 들어가며 'SEMI' 태그가 툭 붙음, 칩 'Tesla Semi prototype · 2018 · Korbitr'")
PLAN['T02a'] = [
 ('D', "Plenty of people would just ask an AI chatbot.", "도해: 로고·회사명 없는 답글창에 'is this real?' 말풍선이 폭포처럼 쌓이며 위로 흐름", 0),
 ('C', "But chatbots can sound sure of themselves, so let's check the physics ourselves.", "문서: SlashGear 기사 제목 카드 'Was The Tesla Roadster Flip Real, Or An AI-Generated Stunt?'(11단어) + 칩 'SlashGear · Oct 16, 2026' — 카드가 아래에서 튀어 오름", 0)]
# Q2: 화면 3.0초 이하로 고정(0.4배속이라 원본은 1.2초 안팎). 컷 경계는 'wheels' 직전, 실측 뒤 단어에 맞춤
dur03 = 15 / WPM * 60
PLAN['T03'] = [
 ('V', "It flips in mid-air and lands on its wheels,", "실영상(Tesla 짧은 인용 Q2, 약 3초): 공중 회전 → 바퀴 착지 0.4배속(원본 1.2초 안팎), 칩 'Video: Tesla' — 화면 3초 이하로 끊고 남는 말은 다음 컷에 걸침", 0, 2.9),
 ('G', "and I keep rewatching that landing.", "생성 그림 RS_141 소파에서 리모컨을 누르는 ROBO — 밀기 3% + 빈 팝콘 통 누끼가 툭 떨어짐", 0, dur03 - 2.9)]
# Q3: 3초 이하로 줄이고 남는 거꾸로 주행·착지는 재현 R1
PLAN['T05'] = [
 ('V', "And this one drives onto a ramp,", "실영상(Tesla 짧은 인용 Q3, 약 2.5초): 램프 진입 → 거꾸로 들어서는 순간까지(정상 속도), 칩 'Video: Tesla'", 0),
 ('M', "rolls along it upside down, and drops back onto its wheels.", "재현 클립 R1: 은빛 만화 차가 램프를 거꾸로 따라 돈 뒤 끝에서 떨어져 바퀴로 쿵 — 위쪽 각도, 먼지와 작은 임팩트", 0)]
setmot('T07a', 0, "실사: Commons Tesla Semi 사진(2회째, 칩 'Tesla Semi prototype · 2018 · Korbitr')에 'AI?' 도장이 찍혔다가 'REAL' 도장으로 덮임 — 거의 정지(QUIET)")
PLAN['T18a'] = [
 ('V', "Now freeze on my favorite frame,", "실영상(Tesla 짧은 인용 Q4, 약 2초): 킥플립 정점 0.5배속 → 'freeze'에서 정지(레코드 긁힘 효과음)", 0),
 ('G', "the car halfway over that Semi.", "생성 그림 RS_302B 일시정지 리모컨을 든 ROBO 누끼가 정지 화면 앞에 툭 등장", 0)]
setmot('T19', 0, "도해: 우리가 그린 정점 프레임(R2 재현 그림, Tesla 프레임 아님) 위 'GRIP = 0' 화살표 네 개가 바퀴에서 허공으로")
# Q5: 거꾸로 주행 구간만 2초 안쪽
PLAN['T22'] = [
 ('D', "Cheat code one. The car rolls onto the ramp", "도해: CHEAT 1 카드가 오락기 메뉴에서 깜박이며 선택되고, 램프 도해에 은빛 차 아이콘이 올라탐", 0),
 ('V', "and keeps going upside down.", "실영상(Tesla 짧은 인용 Q5, 약 2초, Q3과 다른 구간): 거꾸로 주행 느리게, 칩 'Video: Tesla'", 0),
 ('G', "Why doesn't it fall off?", "생성 그림 RS_150 베개를 안은 ROBO — 우리 UI 층만 180도 뒤집혔다 1초 뒤 툭 제자리(자막 층 제외)", 1)]
PLAN['T23'] = [
 ('C', "Tesla's own patent shows fans under the car", "문서: Tesla 특허 US 12,377,920 B1 1면(제목·도면) — 'fans'·'skirts'에 형광 밑줄, 칩 'US Patent 12,377,920 · Tesla · Aug 2025'(시연 차에 쓰였다고 쓰지 않음)", 0),
 ('P', "and skirts sealing the gap underneath.", "실사: 고무 실링 띠 근접 사진(무료 스톡) — 가장자리를 따라 패닝", 0)]
setmot('T34', 0, "실사: Commons BT46B 사진(Brabham BT46B NEC Aug 1994, Tony Hisgett, CC BY 2.0) — 왼→오 패닝, 칩 'Brabham BT46B · 1978 car · photo 1994'")
setmot('T40', 0, "문서: NASA 소형위성 기술 현황 냉가스 절 문구 카드 'There is no combustion in cold gas systems'(8단어) — 'no combustion' 형광, 칩 'NASA Small Spacecraft Tech · 2026'(NASA 보증처럼 쓰지 않음)")
setmot('T42', 0, "문서: Tesla X 게시물 문구 카드 'generates 4–5x the force the tires can'(원문 일부) + 칩 'Tesla on X · Oct 15, 2026'")
setmot('T42', 2, "실사: 레이스 타이어 트레드 근접 사진(무료 스톡, 로고 없음) — 'TIRES 1×' 칩이 붙고 사진이 뒤로 작게 밀려남")
PLAN['T44'] = [
 PLAN['T44'][0], PLAN['T44'][1],
 ('M', "Hope your coffee had a lid.", "움직이는 클립(새): 은빛 C판 차 실내, 컵홀더의 커피 컵이 뒤로 쭉 밀려 뒤 유리창에 철퍽 — 사람 없음, DEADPAN(펀치 뒤 0.5초 멈춤)", 0)]
setmot('T45', 0, "실영상: 디지털 타이머 근접(무료 스톡, 상표 없음, T90과 다른 클립) — 숫자는 우리 글자 층 '0.81 s'로 덮고 칩 'Tesla on X: 0-60 mph in 0.81 seconds'(Tesla 영상은 쓰지 않음)")
setmot('T50', 1, "문서: AutoGuide 보도 문구 카드 'in place of the front passenger seat'(재조판) + 칩 'AutoGuide · Oct 16, 2026' — 'passenger' 형광")
PLAN['T53'] = [
 ('C', "Tesla's own post lists Rocket as 'air ready, seats one.'", "문서: Tesla X 게시물 문구 카드 'Rocket: air ready, seats 1'(원문 그대로) + 칩 'Tesla on X · Oct 15, 2026' — '1'에 동그라미가 그려짐", 0)]
PLAN['T59'] = [
 ('P', "I did some rough math, so treat it as an estimate.", "실사: 연필과 계산기가 놓인 낙서 메모장 사진(무료 스톡, 손·로고 없음) — 'ROUGH MATH' 칩, 짧은 밀기", 0),
 ('D', "If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms,", "도해: 손글씨 계산 메모(600 L × 355.7 kg/m³ → '≈210 kg')가 줄마다 써짐, 칩 'calc · NIST N₂ · 600 L · 5,500 psi · 20 °C'·'estimate'", 0),
 ('G', "around four hundred seventy pounds.", "생성 그림 RS_233 탱크 쪽 저울 접시가 바닥을 뚫음 — 먼지 구름 퍽 + 화면 1회 쿵", 0)]
PLAN['T60'] = [
 ('M', "That's the weight of about two and a half adults,", "움직이는 클립 T60_s2(재편집): 덩치 로봇 둘과 같은 덩치 로봇을 반 크기로 줄인 하나가 한 좌석에 끼어 꿈틀(새 캐릭터 아님)", 0),
 ('G', "and it's all gas.", "생성 그림 RS_235 셋(덩치 둘 + 반 크기 하나)이 흰 가스 구름 모양으로 바뀜 — 구름이 살짝 부풂", 0)]
setmot('T68', 0, "생성 그림(새) RS_T68 옆집 수영장에 코부터 박힌 은빛 C판 차 옆에서 튜브를 낀 ROBO가 고개만 내밀고 무표정 — 글자 없음, 움직임 없이 정적(반응 멈춤), 효과음만")
PLAN['T69'] = [
 ('P', "Refilling the tanks reportedly takes hours,", "실사: 공기 압축기 사진(무료 스톡) + 'HOURS (reported)' 글자 층", 0),
 ('D', "with a goal of about half an hour.", "도해: 숫자 없는 긴 막대 'HOURS (reported)' 옆에 'GOAL ~0.5 h (reported)' 짧은 막대가 툭", 0)]
c = list(PLAN['T70'][0]); c[1] = "In those hours, you could make dinner,"; PLAN['T70'][0] = tuple(c)
setmot('T83', 0, "도해: 우리가 그린 착지 프레임(R2 재현 그림, Tesla 프레임 아님)이 2프레임 떨리고 버퍼링 아이콘(1.5초 이내) → 타임라인 '2028 PRODUCTION · Musk says', 칩 'via AP'")
setmot('T84a', 1, "문서: X 게시물 인용 카드 + 칩 'Sam Altman on X · Oct 30, 2025' — 'bounced'에서 봉투 아이콘이 카드 테두리에 튕김")
setmot('T84b', 0, "문서: 'MUSK'S REPLY' 띠 + Musk 답글 인용 카드(인용은 'you received a refund within 24 hours'만, 같은 답글의 인신 공격 문장은 넣지 않음) — 두 출처 칩을 같은 크기로 좌우 나란히")
setmot('T84f', 0, "실영상(Tesla 짧은 인용 Q8, 원본 3.0초 이하, Q1과 다른 구간): 앞부분 1.3초 안팎은 우리 안내판 그래픽의 'DEPARTED' 줄이 걷히고, 이어 원본 킥플립 3.0초 이하, 칩 'Video: Tesla'")
PLAN['T84g'] = [
 ('G', "I'll admit it, that was", "생성 그림 RS_254 소파 위에서 천천히 박수 치는 ROBO — 팝콘 효과가 흩어짐", 0),
 ('M', "a hell of a demo.", "움직이는 클립: 현관 예약자 ROBO(RS_250c)가 먼지를 털며 벌떡 일어나 누런 영수증을 하늘로 듦", 0)]
# 끝 구간(540–562초)이 20초를 넘어 판정에 들어가므로 T91을 콜백 컷으로 나눔(6 → 8)
PLAN['T91'] = [
 ('D', "So would you trade your passenger seat,", "도해: 투표 카드 'TRADE THE SEAT / KEEP THE SEAT' — 막대가 출렁", 0),
 ('P', "and whoever usually sits there,", "실사: T52의 그 실제 조수석 사진(2회째, 탱크 없이 빈 자리) — 좌석으로 짧은 줌, '?' 칩", 0),
 ('G', "for a few seconds of thrust? Tell us in the comments,", "생성 그림 RS_032 Trade offer 밈(기존, T68에서 옮김) — 밀기 3%, 그림 속 글자는 편집 층", 0),
 ('M', "and send this to the friend", "움직이는 클립: 탱크가 작은 팔로 세 번 손 흔들기, 배경 고정(RS_041 → RS_115 짝 그림 사이 직접 움직임)", 0),
 ('G', "who always calls shotgun.", "생성 그림 RS_243 연석의 BUDDY(2회째, T71a 콜백) — 손가락으로 조수석을 가리키는 효과, 밀기 3%", 0)]

# ④ 판정 2: 02 텐션 6번 시작점 T82a에 ○ 표시(388–501초 공백 해소)
c = list(PLAN['T82a'][1]); c[3] = 1; PLAN['T82a'][1] = tuple(c)

# ---- 시간 계산 (gen.py와 같은 방식) ----
a4 = json.load(open(os.path.join(S3, 'a4.json')))
for sc in a4:
    if sc['id'] in TEXT: sc['text'] = TEXT[sc['id']]
def wc(s): return len([w for w in s.split() if re.search(r'[A-Za-z0-9]', w)])
rows = []; t = 0.0; problems = []
for sc in a4:
    sid = sc['id']; cuts = PLAN.get(sid)
    if not cuts: problems.append(('계획 없음', sid)); continue
    dur = wc(sc['text']) / WPM * 60 + sc.get('silent_sec', 0)
    if sc['text']:
        joined = ' '.join(c[1] for c in cuts)
        if joined != sc['text']: problems.append(('구절 불일치', sid, joined, sc['text']))
    ws = [c[4] if len(c) > 4 else (max(wc(c[1]), 1.6) if sc['text'] else 1) for c in cuts]
    tot = sum(ws); acc = 0
    for i, c in enumerate(cuts):
        t0 = t + dur * acc / tot; acc += ws[i]; t1 = t + dur * acc / tot
        rows.append(dict(id=f'{sid}-{i+1}', scene=sid, n=len(cuts), mat=MAT[c[0]], code=c[0], frag=c[1], mot=c[2], q=c[3], t0=t0, t1=t1))
    t += dur
for r in rows: r['a'] = round(r['t0'], 1); r['b'] = round(r['t1'], 1)
for x, y in zip(rows, rows[1:]): y['a'] = x['b']
for r in rows:
    if TQ in r['mot']:
        r['mot'] = re.sub(r'약 [\d.]+초', f"{r['b']-r['a']:.1f}초", r['mot'])

def stats():
    n = len(rows); cnt = Counter(r['mat'] for r in rows)
    print('컷', n, {v: (cnt[v], round(100*cnt[v]/n, 1)) for v in MAT.values()})
    run = 1
    for x, y in zip(rows, rows[1:]):
        run = run + 1 if x['mat'] == y['mat'] else 1
        if run >= 3: print('  3연속', y['id'], y['mat'])
    sc = OrderedDict()
    for r in rows: sc.setdefault(r['scene'], []).append(r)
    mv = [s for s, cs in sc.items() if sum(c['code'] in 'VM' for c in cs) * 2 >= len(cs)]
    print('장면', len(sc), '움직이는', len(mv), round(100*len(mv)/len(sc), 1))
    end = rows[-1]['b']
    wins = [sum(1 for r in rows if w*30 <= r['a'] < (w+1)*30) for w in range(math.ceil(end/30))]
    print('30초 창', wins, '끝', end)
    vi = [i for i, r in enumerate(rows) if r['code'] == 'V']
    print('실영상 사이 3컷 미만:', [(rows[a]['id'], rows[b]['id'], b-a-1) for a, b in zip(vi, vi[1:]) if b-a-1 < 3])
    ids = Counter(m for r in rows for m in re.findall(r'(?:RS|P)_?\d+[a-z]?(?:_r\d)?', r['mot']) if r['code'] in 'GM')
    print('같은 그림 3회 이상:', [k for k, v in ids.items() if v > 2])
    print('0.5초 미만 컷:', [(r['id'], round(r['b']-r['a'], 2)) for r in rows if r['b']-r['a'] < 0.5])
    tq = [(r['id'], round(r['b']-r['a'], 1)) for r in rows if TQ in r['mot']]
    print('Tesla 인용:', len(tq), tq, '합계', round(sum(d for _, d in tq), 1))
    print('가장 긴 컷:', sorted([(round(r['b']-r['a'], 1), r['id']) for r in rows])[-4:])
    print('총 단어', sum(wc(s['text']) for s in a4))
    return mv

def table():
    out = ['| 장면 id | 시간(초) | 컷 수 | 화면 재료 | 내레이션 구절 | 움직임 한 줄 | 궁금증 갱신 |', '|---|---|---|---|---|---|---|']
    for r in rows:
        out.append(f"| {r['id']} | {r['a']:.1f}-{r['b']:.1f} | {r['n']} | {r['mat']} | {r['frag']} | {r['mot']} | {'○' if r['q'] else '—'} |")
    return '\n'.join(out)

if __name__ == '__main__':
    for p in problems: print('문제', p)
    mv = stats()
    open(os.path.join(OUT, 'table04.md'), 'w', encoding='utf-8').write(table() + '\n')
    open(os.path.join(OUT, 'json04.txt'), 'w', encoding='utf-8').write(json.dumps(a4, indent=2, ensure_ascii=False) + '\n')
    json.dump([dict(id=r['id'], scene=r['scene'], mat=r['mat'], code=r['code'], a=r['a'], b=r['b']) for r in rows],
              open(os.path.join(OUT, 'rows04.json'), 'w', encoding='utf-8'), ensure_ascii=False)
    print('moving', mv)
