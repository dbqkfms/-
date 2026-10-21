import sys; sys.path.insert(0, '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1')
from ed import Ed
e = Ed('/home/user/-/results/01_사실표_001_로드스터.md')
D = '2026-10-21'
NIST = "https://webbook.nist.gov/cgi/fluid.cgi?Action=Data&Wide=on&ID=C7727379&Type=IsoTherm&Digits=5&PLow=37.92&PHigh=68.95&PInc=31.03&T=293.15&RefState=DEF&TUnit=K&PUnit=MPa&DUnit=kg%2Fm3"
CNN = "https://abc11.com/story/can-new-tesla-roadster-fly-elon-musk-unveils-what-he-says-is-flying-car/19944143/"

e.rep("# 01 사실표 — 편 1 테슬라 로드스터 (낭독본 v5 전수 대조)", "# 01 사실표 — 편 1 테슬라 로드스터 (낭독본 v5 전수 대조 + v5.1 최종 행)")
e.rep(e.s[e.s.index('**한 줄 결론:**'):e.s.index('## 확인 방법과 판단 기준')],
"""**한 줄 결론:** 낭독본 v5의 사실 주장은 대부분 1차 출처(Tesla·Musk·Altman 원 게시물, 특허, Reuters·AP·CNN 원문, JPL·NASA·NIST)로 확정됐다. v5에서 근거가 없거나 틀렸던 5곳(T02a·T23·T53·T59·T60)은 v5.1 최종에서 고쳤고, 고친 문장과 T69 v5.1 문장의 행을 2절에 더했다(통합 서브, 2026-10-21). 그래서 v5.1 최종 대사의 주장은 모두 확정 행이 있다. Moravy 인터뷰 수치(T48–T69)는 '보도 원문 확인'으로 확정이고 원 영상 대사는 미대조다.

**바로 쓸 것 3개:**
1. 로컬: Hagerty(`22rvpUecLts`)·Top Gear 원 영상으로 T48·T50·T56·T67·T69의 Moravy 수치를 대조한다. 보도와 다르면 이 파일 1·2절과 02 변경표를 함께 고친다.
2. 로컬: tesla.com/roadster를 브라우저로 열어 캡처하고 T74('not approved for public road use')·T81('Seating 4')을 원문과 대조한다. T23은 특허 문장으로 바꿨으므로 대조가 필요 없다(페이지 문구가 확인되면 v5 문장으로 되돌릴 수 있다).
3. 메인: 99 요약의 10번 5(사실) 근거로 2절의 v5.1 행(T02a·T23·T53·T59·T60·T69)을 쓴다.

""")

def after(anchor_start, newrows):
    # anchor_start로 시작하는 표 줄 바로 뒤에 행을 넣는다
    ls = e.s.split('\n'); hit = [i for i, l in enumerate(ls) if l.startswith(anchor_start)]
    if len(hit) != 1: raise SystemExit(f'앵커 {anchor_start!r}: {len(hit)}')
    ls[hit[0]+1:hit[0]+1] = newrows; e.s = '\n'.join(ls)

e.rep("tends to)'는 일반화이고, 본문 9-1에 따라 실존 대표를 조롱하는 문장이라 사실 언급으로 바꿔야 한다 | https://mobilesyrup.com/2025/11/21/grok-elon-musk-sycophancy/ | 2026-10-21 | 추정 → 수정 권고 |",
      "tends to)'는 일반화이고, 본문 9-1에 따라 실존 대표를 조롱하는 문장이라 사실 언급으로 바꿔야 한다 | https://mobilesyrup.com/2025/11/21/grok-elon-musk-sycophancy/ | 2026-10-21 | 추정 — v5.1에서 대사에서 뺌 |")
after("| [T02a] \"Grok tends to hype its own boss\"", [
 f"| [T02a v5.1 첫판] \"Half of the internet is already asking an AI chatbot.\" — 'Half of X'처럼 수량을 뒷받침하는 집계·보도가 없다(검토 ⑤). v5.1 최종에서 다시 고쳤다 | 없음 | {D} | 미확인·대본 제외 |",
 f"| [T02a v5.1 최종] \"Plenty of people would just ask an AI chatbot.\" — 가정 표현이라 수량 주장이 아니다. 이 영상을 AI로 의심한 사람들은 실제로 있었다(SlashGear 10-16 기사 제목 \"Was The Tesla Roadster Flip Real, Or An AI-Generated Stunt?\") | https://www.slashgear.com/2288900/was-tesla-roadster-flip-stunt-real-or-ai-generated/ | {D} | 확정 |",
 f"| [T02a v5.1 최종] \"But chatbots can sound sure of themselves\" — 언어 모델은 불확실할 때 추측해 그럴듯하지만 틀린 말을 한다. 논문 \"Why Language Models Hallucinate\"(Kalai·Nachum·Vempala·Zhang, arXiv 2025-09-04) 초록 첫 문장: \"large language models sometimes guess when uncertain\". 회사·인물은 말하지 않는다 | https://arxiv.org/abs/2509.04664 | {D} | 확정 |",
])
e.rep("| 2026-10-21 | 추정 → 로컬 캡처 대조 또는 문장 교체(권고 참조) |", "| 2026-10-21 | 추정 — v5.1에서 대사에서 뺌(아래 v5.1 행) |")
after("| [T23] \"Tesla's page lists a fan under the car", [
 f"| [T23 v5.1] \"Tesla's own patent shows fans under the car and skirts sealing the gap underneath.\" — Tesla 특허 US 12,377,920 B1(출원 2025-04-29, 등록 2025-08-05) 초록에 \"multiple fans\", \"deployable skirts\", 차 밑의 \"fully sealed bounded region\"이 있다. 시연 차에 쓰였다고는 말하지 않는다 | https://patents.google.com/patent/US12377920B1/en · https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12377920 | {D} | 확정 |",
])
after("| [T53] Tesla의 Rocket 설명이", [
 f"| [T53 v5.1] \"Tesla's own post lists Rocket as 'air ready, seats one.'\" — Tesla X 게시물 원문 \"Rocket: air ready, seats 1\"(2026-10-16 01:28 UTC = 10-15 미국). 'one'은 '1'을 소리 내어 읽은 것이고 화면 카드는 원문대로 `seats 1`이다 | https://x.com/Tesla/status/2110905588402295283 | {D} | 확정 |",
])
e.rep("10,000 psi라면 약 297 kg이라 이 경우에도 맞지 않는다 | " + NIST + " | 2026-10-21 | 추정 → 수정 권고 |",
      "10,000 psi라면 약 297 kg이라 이 경우에도 맞지 않는다 | " + NIST + " | 2026-10-21 | 추정 — v5.1에서 고침(아래 행) |")
after("| [T59] \"At that pressure", [
 f"| [T59 v5.1] \"If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms, around four hundred seventy pounds.\" — NIST 질소 밀도(20 °C, 37.92 MPa = 5,500 psi) 355.73 kg/m³ × 0.6 m³ = 213 kg = 470 lb. 대사는 가스 종류를 조건문으로 두고 'estimate'로 표시했다. 질소는 Moravy 발언 보도(1절, 추정)이고 CNN은 Musk의 'air tanks'를 썼다. 600 L·5,500 psi는 보도 수치다(T54·T56) | {NIST} · {CNN} | {D} | 확정(계산·조건문) |",
])
e.rep("570 lb일 때만 약 3명이 된다 | https://www.cdc.gov/nchs/fastats/body-measurements.htm | 2026-10-21 | 추정 → 수정 권고 |",
      "570 lb일 때만 약 3명이 된다 | https://www.cdc.gov/nchs/fastats/body-measurements.htm | 2026-10-21 | 추정 — v5.1에서 고침(아래 행) |")
after("| [T60] \"about the weight of three adults\"", [
 f"| [T60 v5.1] \"That's the weight of about two and a half adults\" — 470 lb ÷ CDC 미국 성인 평균(2021-08–2023-08, 남 199.0 lb·여 171.8 lb, 둘의 평균 185.4 lb) = 2.53명 | https://www.cdc.gov/nchs/fastats/body-measurements.htm | {D} | 확정(계산) |",
])
e.rep("| [T69] 보도에 따르면 600 L 전체를 채우는 데 6–7시간, 목표는 약 30분(Hagerty 인터뷰 보도 2곳).",
      "| [T69 v5] 보도에 따르면 600 L 전체를 채우는 데 6–7시간, 목표는 약 30분(Hagerty 인터뷰 보도 2곳). v5.1에서 이 수치는 대사에서 뺐다.")
after("| [T69 v5] 보도에 따르면", [
 f"| [T69 v5.1] \"Refilling the tanks reportedly takes hours, with a goal of about half an hour.\" — 서로 다른 두 인터뷰의 보도 4곳이 '몇 시간'과 '목표 약 30분'을 전한다(InsideEVs·AutoGuide: Thrust 200 L \"two to six hours\"·\"bring that down to 30 minutes\" / TeslaNorth·Deep News: 600 L 6–7시간·목표 약 30분). 대사는 'reportedly'로 귀속했다(메인 판단으로 유지) | https://insideevs.com/news/812205/tesla-roadster-replenishes-air-tanks/ · https://www.autoguide.com/auto/manufacturers/tesla-manufacturers/the-reality-behind-tesla-s-roadster-thruster-system-44640505 · https://teslanorth.com/2026/10/16/tesla-roadster-moravy-hagerty-engineering-interview/ · https://www.itiger.com/news/1173352184 | {D} | 확정(보도 원문 확인) / 원 영상 대사 미대조(로컬 대조 항목) |",
])
e.rep("| [T70·T71] 그동안 저녁을 만들고 먹고 설거지해도 아직 채우는 중 — 6–7시간 기준이면 사실과 맞는 과장이다 | https://teslanorth.com/2026/10/16/tesla-roadster-moravy-hagerty-engineering-interview/ | 2026-10-21 | 확정(보도 수치 기준) |",
      "| [T70·T71] 그 몇 시간 동안(v5.1 'In those hours') 저녁을 만들고 먹고 설거지해도 아직 채우는 중 — 보도된 2–7시간 어느 쪽에도 맞는 과장이다 | https://insideevs.com/news/812205/tesla-roadster-replenishes-air-tanks/ · https://teslanorth.com/2026/10/16/tesla-roadster-moravy-hagerty-engineering-interview/ | 2026-10-21 | 확정(보도 수치 기준) |")
e.rep("[T59] 고압 기체 무게에 이상기체 식을 쓴 것은 틀린 근사다. 379 bar에서 질소는 압축계수 약 1.23이라 실제 질량은 이상기체 값의 약 81%다 |",
      "[T59] 고압 기체 무게에 이상기체 식을 쓴 것은 틀린 근사다. 379 bar에서 질소는 압축계수 약 1.23이라 실제 질량은 이상기체 값의 약 81%다. v5.1 최종은 NIST 실기체 값(약 210 kg)으로 고쳤다 |")
e.rep("필수는 4건이다(대본에 미확인·틀린 수치가 남지 않게). 선택은 2건(더 정확해지지만 지금 문장도 틀리지 않음)이다. 단어 수 영향은 필수 4건 합계 약 0단어다(T02a +2, T53 −3, T59 +1, T60 0).",
      "필수는 4건이다(대본에 미확인·틀린 수치가 남지 않게). 선택은 2건(더 정확해지지만 지금 문장도 틀리지 않음)이다. 단어 수 영향은 필수 4건 합계 약 0단어다(T02a +2, T53 −3, T59 +1, T60 0).\n\n**반영 결과(통합 서브, 2026-10-21):** 필수 4건(T02a·T53·T59·T60)과 조건부 T23(특허 문장)을 v5.1 최종에 넣었다(2절 v5.1 행). 실제 문장은 아래 권고와 조금 다르다. T02a는 ①안('Grok called Musk fitter than LeBron James')이 실존 인물 놀림으로 읽힐 수 있어, 메인 판단으로 수량·인물 없는 중립 문장 \"Plenty of people would just ask an AI chatbot. But chatbots can sound sure of themselves, …\"을 썼다. T59는 질소를 단정하지 않도록 \"If that's nitrogen at fifty-five hundred psi, …\" 조건문으로 썼다(검토 ⑤). T60은 \"That's the weight of about two and a half adults\"로 썼다. 선택 2건 가운데 T42는 넣지 않았다(v5 확정 문장이고 틀리지 않음). T54a 칩은 04에 'Jun 2018'로 둔다. v5.1 최종 단어 수는 1,540이다.")
e.rep("권고하지 않은 것(근거 부족): T69 '6–7 hours'는 그대로 둔다(보도 귀속 'reportedly'가 있고, 보도 2곳이 일치한다).",
      "권고하지 않은 것(근거 부족): T69는 v5.1 문장('reportedly takes hours, with a goal of about half an hour')을 메인 판단으로 유지했다. 보도 4곳이 받치고, v5의 '6–7 hours'는 Hagerty 쪽 보도 2곳뿐이다(검토 ⑤). v5 문장으로 되돌리려면 원 영상 대조가 먼저다.")
e.rep("`NASA CR-198531 · 1996 · microthruster options incl. cold gas`로 바꾸거나, NASA 소형위성 기술 현황(2026 판) 냉가스 절(\"There is no combustion in cold gas systems\")로 대체한다.",
      "`NASA CR-198531 · 1996 · microthruster options incl. cold gas`로 바꾸거나, NASA 소형위성 기술 현황(2026 판) 냉가스 절(\"There is no combustion in cold gas systems\")로 대체한다. → 통합 때 04 T40은 냉가스 절 문구 카드로 바꿨고, CR-198531 표지는 쓰지 않는다.")
e.rep("| NASA CR-198531 \"Chemical Microthruster Options\"(1996) 표지 | https://ntrs.nasa.gov/citations/19970001472 | NTRS 표기 'GOV_PUBLIC_USE_PERMITTED' | 칩 문구를 정정 8번대로 고친다 | T40, T89 |",
      "| NASA CR-198531 \"Chemical Microthruster Options\"(1996) 표지 | https://ntrs.nasa.gov/citations/19970001472 | NTRS 표기 'GOV_PUBLIC_USE_PERMITTED' | 04에서 쓰지 않는다(정정 8, T40은 냉가스 절 문구 카드) | — |")
e.rep("| NASA 소형위성 기술 현황 '4.6.1 Cold Gas' 절 | https://www.nasa.gov/smallsat-institute/sst-soa/in-space_propulsion/ | 미국 정부 저작물(NASA 미디어 지침상 대체로 자유 사용 — 페이지별 예외는 미확인) | 'NASA' 표기, 보증처럼 보이게 쓰지 않는다 | T39, T40 |",
      "| NASA 소형위성 기술 현황 '4.6.1 Cold Gas' 절 | https://www.nasa.gov/smallsat-institute/sst-soa/in-space_propulsion/ | 미국 정부 저작물(NASA 미디어 지침상 대체로 자유 사용 — 페이지별 예외는 미확인) | 'NASA' 표기, 보증처럼 보이게 쓰지 않는다. 04 T40-1 문구 카드로 쓴다 | T39, T40 |")
e.rep("| Brabham BT46B 사진(Calreyn88, A-9 기존) | https://commons.wikimedia.org/wiki/File:1978_Brabham-Alfa_Romeo_BT46B_Fan_Car.jpg | CC BY-SA 4.0 | 표기 + 동일조건. 위 CC BY 2.0 사진을 권장 | T34 |",
      "| Brabham BT46B 사진(Calreyn88, A-9 기존) | https://commons.wikimedia.org/wiki/File:1978_Brabham-Alfa_Romeo_BT46B_Fan_Car.jpg | CC BY-SA 4.0 | 표기 + 동일조건. 04에서 쓰지 않는다(T34는 Tony Hisgett CC BY 2.0 사진으로 바꿈) | — |")
e.rep("| A-9와 같다: 짧은 인용(2–3초, 'Video: Tesla' 칩, 논평 목적) 여부는 사용자 결정. 허용이 없으면 그림으로 재현한다 | T01, T03, T05, T18a, T22, T32, T45, T64, T84f, T89 |",
      "| A-9와 같다: 짧은 인용(곳당 원본 3.0초 이하, 'Video: Tesla' 칩, 논평 목적) 여부는 사용자 결정. 허용이 없으면 그림으로 재현한다. 04 v5.1 최종은 7곳만 쓰고 0-60 클립(T45)은 쓰지 않는다 | T01, T03, T05, T18a, T22, T32, T84f |")
e.save(); print('01 편집 완료')
