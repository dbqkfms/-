import sys; sys.path.insert(0, '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1')
from ed import Ed
e = Ed('/home/user/-/results/02_대본_001_로드스터_v5.1.md')
H = '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/handoff'

# 맨 위
e.rep(e.s[e.s.index('**한 줄 결론:**'):e.s.index('---\n\n**[구조 (한국어)]**')],
"""**한 줄 결론:** 확정 대본 v5에서 10줄만 고친 v5.1 최종본이다. 첫판에서 고친 5줄(T02a·T18a·T44·T69·T84g)에, 검토 ④·⑤를 통합하면서 사실 차단 4줄(T23·T53·T59·T60)과 말맛 1줄(T70)을 더했고 T02a·T84g는 한 번 더 다듬었다. 결과는 1,540단어이고 끝인사는 고정 문구이며 금지된 오프닝 외침은 없다. 대사의 모든 주장은 01 사실표의 확정 행과 맞는다. T80 새 문장은 이번에도 넣지 않았다(보류).

**바로 쓸 것 3개**
1. 로컬: 아래 낭독본(v5.1 최종)으로 TTS를 실측한다. 9분 59초를 넘으면 A-7 순서대로 T31 대사, T38a, T71a를 뺀다. T44 둘째 문장은 DEADPAN(앞 쉼 0.4초)으로 따로 만든다.
2. 로컬: 실측 시간으로 04 장면표의 `시간(초)` 열을 다시 잡고 `check04.py`를 다시 돌린다. Tesla 인용 컷은 Tesla 원본 3.0초를 넘기지 않는다(넘는 부분은 다음 컷으로).
3. 로컬: Hagerty·Top Gear 원 영상으로 T48–T69의 Moravy 수치(보도 귀속)를 대조하고, tesla.com 캡처로 T74·T81 문구를 대조한다. 다르면 01을 고친 뒤 이 파일 변경표에 행을 더한다.

""")

# 구조: 비유 T60·T70
e.rep("  - T60 어른 세 명 무게 · 가스 질량 · 600 L, 5,500 psi, 293 K 이상기체로 약 261 kg. 실제 기체는 압축계수가 약 1.1이라 230 kg대가 된다. 대사가 이미 \"rough math … estimate\"로 추정 표기라 어김은 아니다. 어른 한 명은 약 80–87 kg으로 잡았다.",
      "  - T60 어른 두 명 반 무게 · 가스 질량 · NIST 실기체 밀도(질소, 20 °C, 5,500 psi = 37.92 MPa) 355.73 kg/m³ × 0.6 m³ = 약 213 kg(470 lb)이다. 압축계수는 약 1.23이라 이상기체 값(262 kg)보다 약 19% 가볍다. CDC 미국 성인 평균(남 199.0 lb, 여 171.8 lb, 평균 약 185 lb)으로 나누면 약 2.5명이다. 맞음. 질소는 보도로만 확인돼 T59 대사를 'If that's nitrogen' 조건문으로 썼다(검토 ⑤, 통합 반영).")
e.rep("  - T70 저녁 짓고, 먹고, 설거지 · 재충전 시간('몇 시간', v5.1 T69). 맞음.",
      "  - T70 저녁 짓고, 먹고, 설거지 · 재충전 시간(v5.1 T69 'hours', T70 'In those hours'). 보도된 2–7시간 어느 쪽에도 맞는 과장이다. 맞음.")

# 덩어리별 농담 표
e.rep("| 청구서: 좌석과 가스 | T66–T68 | T67a 옆집 수영장(T68 무대사 밈) |",
      "| 청구서: 좌석과 가스 | T66–T68 | T67a 옆집 수영장(T68 무대사 반응 정지 1.2초, 글자 없는 그림) |")
e.rep("| 끝 | T91–T92 | T91 shotgun 콜백 |",
      "| 끝 | T91–T92 | T91 shotgun 콜백(화면의 Trade offer 밈은 검토 ④에 따라 T68에서 T91-2로 옮겼다) |")

# 실존 인물 표·놀림
e.rep("| T02a | v5 \"Grok tends to hype its own boss\" | 회사 대표 조롱이라 고쳤다. 본문 9-1 예시 문장을 그대로 쓴다 |",
      "| T02a | v5 \"Grok tends to hype its own boss\" | 회사 대표 조롱이라 고쳤다. v5.1 최종은 수량·회사명·인물이 없는 중립 문장이다(메인 판단, 검토 ⑤) |")
e.rep("  - A-10의 화면 전용 T42 'TO MARS' 촛대를 넣으면 7곳이 되므로 빼는 쪽을 추천한다(서브 ③).",
      "  - A-10의 화면 전용 T42 'TO MARS'는 04에서 뺐다(메인 판단, 검토 ④·⑤). 화면까지 합쳐도 6곳이라 B-1 4–6 안이다.")
e.rep("  - T84a–T84d는 약 21초 안에 몰려 있다. 사용자가 정한 '9년 이야기'라 유지했고, 판정은 ④·⑤에 넘긴다.",
      "  - T84a–T84d는 약 19초 안에 몰려 있다. 사용자가 정한 '9년 이야기'이고, ④·⑤ 모두 경계로 봐서 v5 확정 판단대로 유지했다(메인 판단).")

# 판단한 곳
e.rep(e.s[e.s.index("  1. **T02a: 본문 9-1 예시 문장을 그대로 썼다.**"):e.s.index("  2. **T18a·T84g:")],
"""  1. **T02a: 수량 없는 중립 문장으로 바꿨다(통합, 메인 판단).** 첫판에 쓴 본문 9-1 예시 문장('Half of the internet…')도 v5의 'Half of X'처럼 수량 출처가 없었다(검토 ⑤ 차단). 그래서 "Plenty of people would just ask an AI chatbot."으로 바꿨다. 가정 표현이라 수치 주장이 아니고 회사·인물 언급도 없다. 둘째 문장 "chatbots can sound sure of themselves"는 2025-09 논문(Kalai 등, arXiv 2509.04664)이 받친다(01). 'AI에게 묻는 사람들 → 우리가 직접 확인'이라는 기능은 남았다(E-2 2절). 화면은 회사명 없는 'is this real?' 말풍선과 SlashGear 기사 제목 카드("Was The Tesla Roadster Flip Real, Or An AI-Generated Stunt?", 11단어)다. 'BOSS' 액자 컷은 쓰지 않는다.
""")
e.rep("  2. **T18a·T84g: 막 1과 막 4에 화자 1인칭을 넣었다.** B-1 §3.4 '막마다 1인칭 한 줄'이 v5에 빠져 있었다(메인 00 지시). 새 문장을 더하지 않고 기존 줄을 고쳐 단어는 +1, +3만 늘었다.",
      "  2. **T18a·T84g: 막 1과 막 4에 화자 1인칭을 넣었다.** B-1 §3.4 '막마다 1인칭 한 줄'이 v5에 빠져 있었다(메인 00 지시). 새 문장을 더하지 않고 기존 줄을 고쳐 단어는 +1, +2만 늘었다. T84g는 검토 ④에 따라 'Okay'를 뺐다. 6초 뒤 T85 'Okay, quick reality check.'와 말머리가 겹쳤기 때문이다.")
e.rep(e.s[e.s.index("  4. **T69: 수치를 빼고 'hours'로 바꿨다.**"):e.s.index("  5. **A-10 ③ T80")],
"""  4. **T69: 수치를 빼고 'hours'로 바꾼 v5.1 문장을 유지했다(메인 판단).** 'reportedly'로 보도 귀속이 문장에 드러난다. 'takes hours'와 '목표 약 30분'은 서로 다른 두 인터뷰의 보도 4곳(InsideEVs·AutoGuide·TeslaNorth·Deep News)이 모두 받친다(검토 ⑤ 재확인). 01에 v5.1 행을 더했고 상태는 '보도 원문 확인, 원 영상 대사 미대조'다. 원 영상 대조는 로컬 항목이다. T70은 검토 ④에 따라 'In those hours'로 바꿨다. 'In that time'은 바로 앞 '30분'을 가리키는 것처럼 들려 T71 펀치가 꼬였다(단어 수 같음). T88 'hours of refilling'과도 그대로 이어진다.
""")
e.rep("  6. **T84a 칩 날짜(Oct 30 ↔ 31):** 대사에는 날짜가 없다('last year'). 대본은 바꾸지 않았고 칩은 서브 ①·③이 정한다.",
      "  6. **T84a 칩 날짜:** 대사에는 날짜가 없다('last year'). 대본은 바꾸지 않았고, 04·05의 칩은 'Sam Altman on X · Oct 30, 2025'(미국·UTC 기준)로 고쳤다(검토 ⑤ 차단). B-1의 'Oct 31'은 KST 날짜다.")
e.rep("  7. **줄 방식:**",
"""  7. **검토 ⑤ 사실 차단 4줄(통합 반영):**
     - T23: tesla.com 페이지 원문을 이번에도 열지 못했다(403·429). 그래서 원문을 확인한 Tesla 특허(US 12,377,920 B1, 2025-08-05 등록)로 바꿨다. "Tesla's own patent shows fans under the car and skirts sealing the gap underneath."(−1단어). 화면도 특허 1면 문서 컷이고, '시연 차에 쓰였다'고 말하지 않는다. 로컬 캡처로 페이지 문구가 확인되면 v5 문장으로 돌려도 된다.
     - T53: 따옴표 안이 원문과 달랐다('with seating for one'). Tesla X 원문 "Rocket: air ready, seats 1"에 맞춰 "Tesla's own post lists Rocket as 'air ready, seats one.'"으로 바꿨다(−3단어). 카드 글자는 원문대로 `seats 1`이다.
     - T59: 260 kg는 이상기체 근사라 약 23% 컸다. NIST 실기체 값으로 "about two hundred ten kilograms, around four hundred seventy pounds"로 바꿨다. 'that pressure'가 앞 문장의 10,000 psi로 들리던 모호함도 '5,500 psi'로 없앴다. 가스 종류는 보도가 갈려(질소 보도, CNN은 'air') 'If that's nitrogen' 조건문으로 썼다(+2단어).
     - T60: 470 lb는 미국 성인 평균으로 약 2.5명이라 "the weight of about two and a half adults"로 바꿨다(+3단어).
  8. **줄 방식:**""")
e.rep("- **길이:** 1,541단어(v5는 1,534, +7). 추정 약 9분 57초다. v5 추정 9분 54초에 +7단어(약 2.6초)와 T44 앞 쉼 0.4초를 더했다. A-10의 T63 1초 박자는 클립 삭제로 뺐다. 실측으로 다시 맞춘다.",
      "- **길이:** 1,540단어(v5는 1,534, +6. v5.1 첫판 1,541에서 검토 반영으로 −1). 추정 약 9분 57초다(분당 161단어, DEADPAN 앞 쉼 포함). 04 장면표는 분당 165단어·쉼 없이 562.0초로 잡았다. A-10의 T63 1초 박자는 클립 삭제로 뺐다. 실측으로 다시 맞춘다.")

# 낭독본 형식 메모
e.rep("바뀐 줄은 T02a·T18a·T44·T69·T84g(변경표 참조).",
      "v5에서 바뀐 줄은 10줄이다(T02a·T18a·T23·T44·T53·T59·T60·T69·T70·T84g, 변경표 참조).")

# 낭독본 문장
L = [
 ("Half of the internet is already asking an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves.\n\nIt flips",
  "Plenty of people would just ask an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves.\n\nIt flips"),
 ("\nTesla's page lists a fan under the car and a seal around the gap underneath.\n", "\nTesla's own patent shows fans under the car and skirts sealing the gap underneath.\n"),
 ("\nTesla's own description of Rocket says it's 'air ready, with seating for one.'\n", "\nTesla's own post lists Rocket as 'air ready, seats one.'\n"),
 ("\nI did some rough math, so treat it as an estimate. At that pressure, a full load is about two hundred sixty kilograms of gas, around five hundred seventy pounds.\n",
  "\nI did some rough math, so treat it as an estimate. If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms, around four hundred seventy pounds.\n"),
 ("\nThat's about the weight of three adults, and it's all gas.\n", "\nThat's the weight of about two and a half adults, and it's all gas.\n"),
 ("\nIn that time, you could make dinner, eat dinner, and do the dishes.\n", "\nIn those hours, you could make dinner, eat dinner, and do the dishes.\n"),
 ("\nOkay, I'll admit it, that was a hell of a demo.\n\nBut Musk", "\nI'll admit it, that was a hell of a demo.\n\nBut Musk"),
]
for o, n in L: e.rep(o, n)

# 변경표
e.rep("| T02a | Half of X is already asking Grok. But Grok tends to hype its own boss, so let's check the physics ourselves. | Half of the internet is already asking an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves. | 본문 8번 금지와 9-1 위반이다(실존 회사 대표 조롱). 9-1 예시 문장으로 바꿔 사실 언급으로 낮췄다. +2단어 |",
      "| T02a | Half of X is already asking Grok. But Grok tends to hype its own boss, so let's check the physics ourselves. | Plenty of people would just ask an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves. | 본문 8번 금지와 9-1 위반이다(실존 회사 대표 조롱). 첫판은 9-1 예시 문장('Half of the internet…')이었는데, 수량 출처가 없어(10번 5, 검토 ⑤ 차단) 통합 때 수량 없는 가정 문장으로 다시 고쳤다(메인 판단). v5 대비 +1단어 |")
e.rep("""| T44 | That's your seat""", """| T23 | Tesla's page lists a fan under the car and a seal around the gap underneath. | Tesla's own patent shows fans under the car and skirts sealing the gap underneath. | 10번 5 사실 위반이다(검토 ⑤ 차단). 페이지 문구 원문을 열지 못했다(403·429). 원문을 확인한 Tesla 특허 US 12,377,920 B1 문장으로 바꿨다. −1단어 |
| T44 | That's your seat""")
e.rep("""| T69 | Refilling all six hundred liters""", """| T53 | Tesla's own description of Rocket says it's 'air ready, with seating for one.' | Tesla's own post lists Rocket as 'air ready, seats one.' | 10번 5 사실과 3-C '원문 그대로' 위반이다(검토 ⑤ 차단). Tesla X 원문은 "Rocket: air ready, seats 1"이다. −3단어 |
| T59 | I did some rough math, so treat it as an estimate. At that pressure, a full load is about two hundred sixty kilograms of gas, around five hundred seventy pounds. | I did some rough math, so treat it as an estimate. If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms, around four hundred seventy pounds. | 10번 3·5 위반이다(검토 ⑤ 차단). 260 kg는 이상기체 근사라 약 23% 크다. NIST 실기체 값 213 kg(470 lb)으로 고쳤다. 가스 종류는 보도가 갈려 조건문으로 썼다. +2단어 |
| T60 | That's about the weight of three adults, and it's all gas. | That's the weight of about two and a half adults, and it's all gas. | 10번 3·5 위반이다(검토 ⑤ 차단). 470 lb ÷ CDC 미국 성인 평균 약 185 lb = 2.5명. +3단어 |
| T69 | Refilling all six hundred liters""")
e.rep("확정 전 수치를 뺐다. −5단어 |",
      "확정 전 수치를 뺐다. 통합 때 메인 판단으로 이 문장을 유지했다('reportedly' 귀속, 01에 v5.1 행 추가). −5단어 |")
e.rep("""| T84g | Okay, that was a hell of a demo. | Okay, I'll admit it, that was a hell of a demo. | 3-H 말투, B-1 §3.4 위반이다(막 4에 화자 1인칭 없음). 감상 한 줄을 1인칭으로 바꿨다. +3단어 |""",
      """| T70 | In that time, you could make dinner, eat dinner, and do the dishes. | In those hours, you could make dinner, eat dinner, and do the dishes. | 10번 3·4 개선이다(검토 ④). v5.1 T69가 '30분'으로 끝나 'In that time'이 30분을 가리키는 것처럼 들렸다. 0단어 |
| T84g | Okay, that was a hell of a demo. | I'll admit it, that was a hell of a demo. | 3-H 말투, B-1 §3.4 위반이다(막 4에 화자 1인칭 없음). 감상 한 줄을 1인칭으로 바꿨다. 통합 때 검토 ④에 따라 'Okay,'를 뺐다(6초 뒤 T85 'Okay'와 겹침). v5 대비 +2단어 |""")
e.rep("| 대사에 날짜가 없다('last year'). Oct 30 ↔ 31은 화면 칩 문제라 서브 ①·③에 넘긴다 |",
      "| 대사에 날짜가 없다('last year'). 화면 칩은 04·05에서 'Oct 30, 2025'로 고쳤다(검토 ⑤) |")
e.rep("- 바꾼 줄은 5줄(T02a·T18a·T44·T69·T84g)이다. 장면 id와 순서는 v5 그대로이고, 장면 수는 100이다(대사 98 + 무대사 2).\n- 단어는 1,534에서 1,541로 늘었다(+7).",
      "- 바꾼 줄은 10줄(T02a·T18a·T23·T44·T53·T59·T60·T69·T70·T84g)이다. 첫판 5줄에 통합 때 5줄(T23·T53·T59·T60·T70)을 더했고, T02a·T84g는 한 번 더 고쳤다. 장면 id와 순서는 v5 그대로이고, 장면 수는 100이다(대사 98 + 무대사 2).\n- 단어는 1,534에서 1,540으로 늘었다(+6). v5.1 첫판 1,541에서 통합 반영으로 −1이다(T02a −1, T23 −1, T53 −3, T59 +2, T60 +3, T84g −1).\n- 반영하지 않은 것: T42 'per one report' 삭제(선택 권고, 원 게시물이 확인돼 틀린 말은 아니고 v5 확정 문장이라 그대로 둠), T80 새 문장(보류 유지).")

# 자막·납품
e.rep("한글 자막은 \"구독하고, / 다음 멘붕 때 만나요.\"로 하고, 모든 편에서 같은 문구로 고정하기를 추천한다.",
      "한글 자막은 '구독하고, 다음 멘붕 때 만나요.'로 고정한다(메인 판단, 03 마지막 행과 같음).")
e.rep("T84g는 따뜻하게 앞 쉼 0.3초(v5 그대로).", "T84g는 따뜻하게 앞 쉼 0.3초(v5 그대로, 'I'll admit it'로 시작).")

# 검증 출력 앞부분은 나중에 붙인다: 기존 절을 잘라 둔다
i = e.s.index('## 검증 출력')
e.s = e.s[:i].rstrip('\n') + '\n'
e.save()
print('02 편집 완료')
