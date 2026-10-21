import sys; sys.path.insert(0, '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1')
from ed import Ed
e = Ed('/home/user/-/results/03_현지화_001_로드스터.md')
e.rep("# 03 현지화 — 편 1 테슬라 로드스터 (v5.1 기준)", "# 03 현지화 — 편 1 테슬라 로드스터 (v5.1 최종 기준)")
e.rep(e.s[e.s.index('**한 줄 결론:**'):e.s.index('- 말투:')],
"""**한 줄 결론:** 한글 자막판에 쓸 한국어 자막을 장면 id 100개(A-4 순서 그대로, 대사 98 + 무대사 2) 전부 줄 단위로 썼다. 영어 원문은 v5.1 최종 문장(02와 같음)이고, 검토 통합 때 바뀐 7줄(T02a·T23·T53·T59·T60·T70·T84g)과 끝인사(T92)를 고쳤다. 밈·말장난·단위 21곳은 뜻이 살게 의역했고 아래 '의역 메모'에 이유를 적었다.

**바로 쓸 것 3개**
1. 로컬 편집: 이 표의 '한국어 자막' 칸을 한글 자막판의 한국어 자막 층에 장면 id별로 넣는다. ` / ` 자리에서 줄을 바꾸거나 다음 자막으로 넘긴다(화면에 굽지 않음).
2. 로컬 편집: TTS 실측 타이밍이 나오면 같은 장면 id의 영어 원문으로 영어 .srt를 만들어 자막 없음판에 동봉한다.
3. 로컬 편집: 그림 속 영어 글자(T91-2 Trade offer 밈 등)에 작은 한국어 번역을 붙일지 정한다. 붙이면 '의역 메모'의 T91 추천 문구를 쓴다.

""")
R = [
 ("| T02a | Half of the internet is already asking an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves. | 인터넷 절반은 벌써 / AI 챗봇한테 진짜냐고 묻는 중이죠. / 근데 챗봇은 / 말투만 자신만만할 때도 있으니 / 물리는 우리가 직접 따져 봐요. |",
  "| T02a | Plenty of people would just ask an AI chatbot. But chatbots can sound sure of themselves, so let's check the physics ourselves. | AI 챗봇한테 그냥 물어볼 사람도 많겠죠. / 근데 챗봇은 / 말투만 자신만만할 때도 있으니 / 물리는 우리가 직접 따져 봐요. |"),
 ("| T23 | Tesla's page lists a fan under the car and a seal around the gap underneath. | 테슬라 페이지엔 차 밑의 팬과 / 바닥 틈을 막는 밀봉이 나와요. |",
  "| T23 | Tesla's own patent shows fans under the car and skirts sealing the gap underneath. | 테슬라 특허엔 차 밑 팬들과 / 틈을 막는 스커트가 나와요. |"),
 ("| T53 | Tesla's own description of Rocket says it's 'air ready, with seating for one.' | 테슬라도 로켓을 이렇게 소개해요. / '공중 준비 완료, 좌석은 하나.' |",
  "| T53 | Tesla's own post lists Rocket as 'air ready, seats one.' | 테슬라 게시물엔 로켓이 / '공중 준비 완료, 좌석 1개'로 나와요. |"),
 ("| T59 | I did some rough math, so treat it as an estimate. At that pressure, a full load is about two hundred sixty kilograms of gas, around five hundred seventy pounds. | 대충 계산한 거라 / 추정치로 들어 주세요. / 그 압력이면 가득 채운 가스는 / 약 260킬로그램이에요. |",
  "| T59 | I did some rough math, so treat it as an estimate. If that's nitrogen at fifty-five hundred psi, a full load is about two hundred ten kilograms, around four hundred seventy pounds. | 대충 계산한 거라 / 추정치로 들어 주세요. / 그게 5,500 psi 질소라면 / 가득 찼을 때 약 210킬로그램이에요. |"),
 ("| T60 | That's about the weight of three adults, and it's all gas. | 어른 세 명 무게쯤인데, / 전부 가스예요. |",
  "| T60 | That's the weight of about two and a half adults, and it's all gas. | 어른 두 명 반 무게쯤인데, / 전부 가스예요. |"),
 ("| T70 | In that time, you could make dinner, eat dinner, and do the dishes. | 그 시간이면 저녁을 만들고, 먹고, / 설거지까지 할 수 있어요. |",
  "| T70 | In those hours, you could make dinner, eat dinner, and do the dishes. | 그 몇 시간이면 저녁을 만들고, 먹고, / 설거지까지 할 수 있어요. |"),
 ("| T84g | Okay, I'll admit it, that was a hell of a demo. | 인정할게요. / 그건 진짜 끝내주는 시연이었어요. |",
  "| T84g | I'll admit it, that was a hell of a demo. | 인정할게요. / 그건 진짜 끝내주는 시연이었어요. |"),
 ("| T92 | Subscribe, and see you next meltdown. | 구독하고, / 다음 멘붕 때 만나요. |",
  "| T92 | Subscribe, and see you next meltdown. | 구독하고, 다음 멘붕 때 만나요. |"),
 # 의역 메모
 ("| T02a | asking an AI chatbot / sound sure of themselves | 진짜냐고 묻는 중 / 말투만 자신만만할 때도 | 무엇을 묻는지(진짜냐고)를 덧붙여 'AI에게 진짜냐고 묻는 밈'의 뜻을 살렸다. 'sound sure of themselves'는 '말투만'으로 틀릴 수도 있다는 뉘앙스를 냈다 |",
  "| T02a | Plenty of people would just ask / sound sure of themselves | 그냥 물어볼 사람도 많겠죠 / 말투만 자신만만할 때도 | 'would'의 가정 느낌을 '-겠죠'로 살려 수량을 단정하지 않았다(v5.1 최종 문장). 'sound sure of themselves'는 '말투만'으로 틀릴 수도 있다는 뉘앙스를 냈다 |"),
 ("| T53 | air ready, with seating for one | '공중 준비 완료, 좌석은 하나.' | 'air ready'를 그대로 두면 뜻이 안 와서 풀어 썼다. Tesla 문구 인용이므로 뜻은 바꾸지 않았다 |",
  "| T53 | air ready, seats one | '공중 준비 완료, 좌석 1개' | Tesla X 원문 'air ready, seats 1'을 옮겼다. 'air ready'는 그대로 두면 뜻이 안 와서 풀어 썼고, 'seats 1'은 원문 숫자대로 '1개'로 했다 |"),
 ("| T59 | around five hundred seventy pounds | (생략) | 같은 양의 파운드 표기라 kg만 남겼다 |",
  "| T59 | If that's nitrogen / around four hundred seventy pounds | 그게 … 질소라면 / (생략) | 가스 종류를 단정하지 않는 조건문이라 '-라면'으로 옮겼다. 파운드는 같은 양의 다른 단위라 kg만 남겼다 |"),
 ("| T68 | (그림 속 Trade offer 글자) | (자막 없음) | 그림 속 영어 글자는 그림의 일부다. 한글 자막판에 작은 번역을 붙일지는 로컬이 정한다. 추천은 붙이는 쪽이고 문구는 '거래 제안 · 내가 받을 것: 네 조수석 · 네가 받을 것: 몇 초짜리 추력'이다 |",
  "| T68 | (무대사 반응 정지) | (자막 없음) | 검토 ④에 따라 글자 없는 반응 그림(수영장의 ROBO)으로 바꿨다. 번역할 글자가 없다 |"),
 ("| T84g | Okay, I'll admit it, that was a hell of a demo. | 인정할게요. 그건 진짜 끝내주는 시연이었어요. | 'hell of a'는 욕설 느낌을 빼고 감탄만 살렸다 |",
  "| T84g | I'll admit it, that was a hell of a demo. | 인정할게요. 그건 진짜 끝내주는 시연이었어요. | 'hell of a'는 욕설 느낌을 빼고 감탄만 살렸다. 영어에서 'Okay,'를 뺐는데 자막은 원래 '인정할게요'로 시작해 그대로다 |"),
 ("| T90 | Zero to sixty / Order to driveway", "| T70 | In those hours | 그 몇 시간이면 | 'those hours'는 복수라 바로 앞 '30분'을 가리키지 않는다. 자막에서도 '그 시간'만 쓰면 30분으로 읽혀서 '그 몇 시간'으로 했다(검토 ④) |\n| T90 | Zero to sixty / Order to driveway"),
 ("| T92 | see you next meltdown | 다음 멘붕 때 만나요 | 채널 고정 끝인사다. 'meltdown'(폭주·멘탈 붕괴)을 '멘붕'으로 옮겼다. 한국어 끝인사도 모든 편에서 같은 문구로 고정하기를 추천한다 |",
  "| T91 | (그림 속 Trade offer 글자, T91-2) | (자막 없음, 작은 번역 선택) | 검토 ④에 따라 Trade offer 밈 그림이 T68에서 T91-2로 옮겨 왔다. 그림 속 영어 글자는 그림의 일부다. 한글 자막판에 작은 번역을 붙일지는 로컬이 정한다. 추천은 붙이는 쪽이고 문구는 '거래 제안 · 내가 받을 것: 네 조수석 · 네가 받을 것: 몇 초짜리 추력'이다 |\n| T92 | see you next meltdown | 구독하고, 다음 멘붕 때 만나요. | 채널 고정 끝인사다. 'meltdown'(폭주·멘탈 붕괴)을 '멘붕'으로 옮겼다. 메인 판단으로 이 한 줄('구독하고, 다음 멘붕 때 만나요.')을 고정 문구로 정했고, 한 줄로 끊지 않고 쓴다 |"),
 ("  - T69(사실표가 600 L 6–7시간을 확정해 v5 문장으로 되돌릴 때):",
  "  - T69(통합 때 메인 판단으로 v5.1 문장을 유지했다. 원 영상 대조로 600 L 6–7시간이 확정되고 v5 문장으로 되돌릴 때만 쓴다):"),
]
for o, n in R: e.rep(o, n)
e.save(); print('03 편집 완료')
