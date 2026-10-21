# 편 1 로드스터 컷 계획 (서브 ③). 재료 코드: P 실사 / V 실영상 / D 도해 / C 문서 / G 생성 그림 / M 움직이는 클립
# 각 컷: (재료, 내레이션 구절, 움직임 한 줄, 궁금증 ○ 여부[, 가중치])
SYNC = '(v5.1 동기화 대기)'
PLAN = {
'T01': [
 ('M', "So that's a Tesla doing a kickflip", "재현 클립 R1: 은빛 만화 로드스터가 흰 SEMI 위로 공중제비(원본 타이밍만 따름) — 빨간 BREAKING 띠가 왼→오로 밀려 들어옴", 0),
 ('P', "over a Semi truck.", "실사: Commons Tesla Semi 사진 — 3% 밀어 들어가며 'SEMI' 태그가 툭 붙음", 0)],
'T02': [
 ('C', "And if your first thought was 'that's AI,'", "문서: Tesla X 행사 게시물 인용 카드('Do a kickflip!', 계정·날짜) — 흑백으로 바뀌며 빨간 'AI?' 손도장 쾅", 0),
 ('G', "you're not alone.", "생성 그림 RS_201 의심하는 로봇 관중석 — 왼→오 느린 패닝", 0)],
'T02a': [
 ('D', "Half of X is already asking Grok. " + SYNC, "도해: 로고 없는 답글창에 '@grok is this real?' 말풍선이 폭포처럼 쌓이며 위로 흐름", 0, 7),
 ('C', SYNC, "문서: 보도 인용 카드(문장은 v5.1 확정 뒤) — 카드가 아래에서 튀어 오르고 출처 칩 깜박", 0, 7),
 ('G', SYNC, "생성 그림 RS_101 ROBO가 폰을 내려놓고 돋보기를 듦 — 돋보기 쪽으로 4% 확대", 0, 7)],
'T03': [
 ('M', "It flips in mid-air and lands on its wheels,", "재현 클립 R2: 공중 회전 → 바퀴 착지 0.4배속, 착지 순간 먼지 퍽", 0),
 ('G', "and I keep rewatching that landing.", "생성 그림 RS_141 소파 ROBO 리모컨 — 밀기 3% + 빈 팝콘 통 누끼가 툭 떨어짐", 0)],
'T04': [
 ('G', "Tony Hawk is in shambles.", "생성 그림 RS_301B(또는 C) 스케이터 로봇 절 — 'KICKFLIP OVER SEMI' 콤보 점수 팝업이 쌓인 뒤 정지", 0)],
'T05': [
 ('M', "And this one drives onto a ramp, rolls along it upside down,", "재현 클립 R3: 램프 진입 → 거꾸로 주행, 카메라가 차를 따라 옆으로 흐름", 0),
 ('M', "and drops back onto its wheels.", "재현 클립 R4: 램프 끝에서 떨어져 바퀴로 쿵, 먼지와 작은 임팩트", 0)],
'T06': [
 ('C', "Here's what we know. Tesla posted this footage itself", "문서: Tesla X 게시물 2개 인용 카드(계정·날짜, 영상 칸은 '원본 링크는 설명란') — 카드 두 장이 차례로 착 붙음", 0),
 ('D', "from its Roadster event on October 15th.", "도해: 텍사스 지도에 핀 'McGregor, TX'이 떨어지고 날짜 칩 'Oct 15, 2026'", 0)],
'T07': [
 ('D', "The physics checks out.", "도해: 3칸 판 'POSTED BY TESLA ✓ · PHYSICS ✓'가 하나씩 켜짐", 0),
 ('C', "The numbers are Tesla's own,", "문서: tesla.com/roadster 사양 줄 인용 카드 — 숫자 칸에 'TESLA SAYS' 띠가 감김", 0),
 ('G', "and we haven't seen anyone measure them independently yet.", "생성 그림 RS_203 빈 심사위원석, 문틈의 ROBO — 문 쪽으로 천천히 밀기", 1)],
'T07a': [
 ('P', "Which is a very 2026 problem.", "실사: Commons Tesla Semi 사진(2회째)에 'AI?' 도장이 찍혔다 지워짐", 0),
 ('G', "Real footage now has to prove it isn't AI.", "생성 그림 RS_144 검문소에서 서류를 내미는 사진 액자 — 고정, 도장만 1회 흔들림", 0)],
'T09': [
 ('V', "Here's the problem. Tires only push against the road,", "실영상: 타이어가 노면을 미는 근접(무료 스톡, 로고·번호판 없음)", 0),
 ('D', "and no road is throwing a car over a truck.", "도해: SEMI 위 포물선에 'ROAD' 화살표가 차 밑에서 뚝 끊김", 1)],
'T10': [
 ('P', "So Tesla stopped relying", "실사: 텍사스 시골 도로 사진 — 빨간 X가 쾅 찍힘", 0),
 ('M', "on the road.", "움직이는 클립: 내비 경로선이 도로에서 떨어져 하늘로 솟아 궤도선이 됨, 칩 'Recalculating…'", 0)],
'T10a': [
 ('P', "To be fair, the last Roadster Musk took off-road", "실사: SpaceX Starman 사진(CC0) — 2.5D 시차로 차와 지구가 살짝 어긋나 움직임, 칩 'Photo: SpaceX · CC0 · Feb 2018'", 0),
 ('P', "is still orbiting the Sun.", "실사: 같은 묶음 둘째 Starman 사진(CC0)으로 하드컷 — 아주 느린 줌아웃", 0)],
'T11': [
 ('D', "So today, it's two cheat codes,", "도해: 오락기 메뉴풍 'CHEAT CODES: 2' — 커서가 깜박이며 내려감", 0),
 ('P', "one race car from 1978,", "실사: Commons Brabham BT46B 후면 사진(CC BY 2.0) — 팬 쪽으로 4% 밀기", 0),
 ('G', "and the reason the top version seats one person.", "생성 그림 RS_206 방수포 덮인 탱크가 조수석에서 눈만 빼꼼 — 정지 후 눈만 깜박(효과)", 0)],
'T13': [
 ('G', "So why not just bolt in a bigger motor?", "생성 그림 RS_146 ROBO가 큰 모터를 렌치로 조임 — 밀기 3% + 쿵 효과", 0),
 ('V', "Because tires only push back on the road,", "실영상: 출발하는 바퀴 슬로모션(무료 스톡)", 0),
 ('D', "and the road pushes the car forward.", "도해: 힘 화살표 둘(타이어→노면, 노면→차)이 차례로 그려짐", 0)],
'T14': [
 ('D', "And a tire can only push as hard as its grip,", "도해: 타이어 접지면 단면 + 손글씨 'F ≤ μN'이 써짐", 0),
 ('G', "which comes down to how hard it's pressed down", "생성 그림 RS_208 거대한 장갑 손이 타이어를 꾹 — 위에서 아래로 1회 눌리는 흔들림", 0),
 ('P', "and how grippy the surface is.", "실사: 빙판·고무 매트 바닥 사진 두 장 좌우 분할 — 가운데 선이 밀려 나옴", 0)],
'T15': [
 ('V', "Picture sprinting on ice in socks.", "실영상: 빙판에서 미끄러지는 발 근접(얼굴 없음, 무료 스톡)", 0),
 ('G', "Your legs give it everything,", "생성 그림 RS_007 양말 신은 ROBO 출발 자세 — 빠른 줌인", 0),
 ('M', "and you just vibrate aggressively in place.", "움직이는 클립 T15_s1(기존): ROBO 다리가 흐릿하게 파닥, 몸은 제자리", 0)],
'T16': [
 ('G', "That's not a skill issue.", "생성 그림 RS_148 트랙 위 ROBO 질주 자세 — 속도선 효과만 흐름", 0),
 ('P', "That's a floor issue.", "실사: 반들반들한 바닥 위 양말 사진(무료 스톡) — 바닥 쪽으로 툭 기울기", 0)],
'T17': [
 ('V', "Cars have the same problem. Too much power without enough grip", "실영상: 타이어 번아웃 연기(무료 스톡, 로고·번호판 없는 구간)", 0),
 ('G', "just makes smoke.", "생성 그림 RS_209 연기 속 노란 눈 ROBO와 작은 소화기 — 연기 효과가 눈 앞을 한 번 지나감", 0)],
'T18': [
 ('D', "Press the car down harder, though, and that limit goes up.", "도해: 누르는 화살표가 굵어지자 'GRIP LIMIT' 막대가 올라감", 0),
 ('P', "Racers call that downforce.", "실사: 큰 뒷날개 레이스카 사진(Commons) — 날개 쪽으로 밀기 + 'DOWNFORCE' 단어", 0)],
'T18a': [
 ('M', "Now put the car in the air,", "재현 클립 R1 정점 구간 0.5배속 → 정지(레코드 긁힘 효과음)", 0),
 ('G', "halfway over that Semi.", "생성 그림 RS_302B 일시정지 리모컨 누끼 ROBO가 정지 화면 앞에 툭 등장", 0)],
'T19': [
 ('D', "Up there, the tires aren't touching anything,", "도해: 정지 화면 위 'GRIP = 0' 화살표 네 개가 바퀴에서 허공으로", 0),
 ('M', "so there's nothing to grip.", "움직이는 클립 VL_T19: 은빛 차 네 바퀴가 만화처럼 헛돌고 리본이 펄럭이다 멈춤", 0)],
'T21': [
 ('M', "So Tesla needed two cheat codes.", "움직이는 클립: ROBO가 버튼 연타 → 화면 초록 → 만세(RS_010 → RS_010b 짝 그림 사이를 직접 움직임)", 0),
 ('D', "One presses the car down harder.", "도해: CHEAT 1 카드 — 차 위로 큰 화살표가 꾹 내려옴", 0),
 ('G', "The other pushes without the road at all.", "생성 그림 RS_212 절벽 끝을 지나 흰 가스로 떠가는 차 — 오른쪽으로 패닝", 0)],
'T22': [
 ('M', "Cheat code one. The car rolls onto the ramp and keeps going upside down.", "재현 클립 R5: 거꾸로 주행 느리게(R3과 다른 각도), 바닥 먼지 흩날림", 0),
 ('G', "Why doesn't it fall off?", "생성 그림 RS_150 베개를 안은 ROBO — 우리 UI 층만 180도 뒤집혔다 1초 뒤 툭 제자리(자막 층 제외)", 1)],
'T23': [
 ('C', "Tesla's page lists", "문서: tesla.com 문구 인용 카드 — 'fan'·'seal'에 형광 밑줄이 그어짐", 0),
 ('D', "a fan under the car", "도해: 차 바닥 투시 — 팬 위치가 빛나며 회전 표시", 0),
 ('P', "and a seal around the gap underneath.", "실사: 고무 실링 띠 근접 사진(무료 스톡) — 가장자리를 따라 패닝", 0)],
'T24': [
 ('D', "The fan pulls air out from under the car.", "도해: 단면 — 바닥 아래 공기 알갱이가 팬을 지나 밖으로 빠져나감", 0),
 ('D', "Now there's less air pushing up from below than pushing down from above.", "도해: 같은 단면 위·아래 화살표 수가 바뀜(위 많음, 아래 적음)", 0)],
'T25': [
 ('G', "And here's the part most people get backwards.", "생성 그림 RS_151 포스터를 거꾸로 든 ROBO — 포스터만 180도 돌아감", 0),
 ('G', "The fan isn't really pulling the car down.", "생성 그림 RS_214 '나 아님' 어깨 으쓱 팬 캐릭터 — 밀기 3%", 0)],
'T26': [
 ('D', "The fan just gets some air out of the way.", "도해: 팬이 공기 알갱이 몇 개를 옆으로 비켜 세움", 0),
 ('V', "The atmosphere does the shoving.", "실영상: ISS에서 본 지구 대기 테두리(NASA) — 칩 'Video: NASA'", 0)],
'T27': [
 ('P', "It's a suction cup phone mount.", "실사: 앞유리 흡착 거치대 사진(무료 스톡, 폰 화면 빈 면) — 거치대로 줌인", 0),
 ('G', "You don't pull it onto the windshield.", "생성 그림 RS_216 줄로 흡착컵을 당기는 ROBO — 줄 쪽으로 2회 덜컥", 0),
 ('D', "The air outside presses it there.", "도해: 흡착컵 단면 — 바깥 공기 화살표가 사방에서 누름", 0)],
'T28': [
 ('G', "Wait. It's the air doing the work?", "생성 그림 RS_013 밈 형식 1컷(우주인 로봇이 지구를 봄) — 정지, 아주 느린 줌", 0)],
'T29': [
 ('G', "Always has been.", "생성 그림 RS_014 밈 형식 둘째 컷 — 정지, 효과음 하나", 0)],
'T30': [
 ('D', "The catch is the seal. If air sneaks in around the edges,", "도해: 틈 단면 — 바깥 공기 알갱이가 가장자리로 스며듦", 0),
 ('M', "the push is gone.", "움직이는 클립: 공기 알갱이 캐릭터들이 틈으로 비집고 들어오자 누르는 손이 퐁 사라지고 차가 툭 처짐", 0)],
'T31': [
 ('P', "It's like a suction cup", "실사: 흡착컵 근접 사진(무료 스톡) — 살짝 흔들림", 0),
 ('G', "on a dusty dashboard.", "생성 그림 RS_061b 먼지 대시보드에서 떨어진 흡착컵, ROBO 한숨 — 먼지 효과 퍽", 0)],
'T32': [
 ('D', "Flip it upside down, and the outside air pushes the car up against the ramp instead.", "도해: 단면 전체가 180도 뒤집히고 공기 화살표 방향은 그대로 차를 램프 쪽으로 밂", 0),
 ('M', "That's cheat code one.", "재현 클립 R6: 거꾸로 램프에서 떨어져 나와 착지 + 자물쇠 P07이 딸깍 열림", 0)],
'T33': [
 ('D', "We can explain the pressure trick,", "도해: 단면 옆에 큰 ✓ 도장", 0),
 ('G', "but we couldn't confirm how Tesla ran its fan in this demo.", "생성 그림 RS_017 김 서린 돋보기를 든 ROBO — 돋보기 김이 퍼지는 효과", 0)],
'T34': [
 ('V', "Fun fact.", "실영상: 체커기 휘날림(무료 스톡)", 0),
 ('P', "A 1978 Formula One fan car used this same trick,", "실사: Commons BT46B 측면 사진(CC BY-SA 4.0) — 왼→오 패닝, 칩 'Brabham BT46B · 1978'", 0),
 ('G', "and it won the only race it ever ran.", "생성 그림 RS_217 트로피 들고 셔터를 내리는 로봇 레이서 — 셔터가 내려오는 효과", 0)],
'T37': [
 ('M', "That pressure holds a car against a surface,", "움직이는 클립: 차체가 두 번 들썩였다 바닥에 착 붙음(RS_020 → RS_103 짝 그림 사이 직접 움직임)", 0),
 ('D', "but it can't throw one over a truck.", "도해: SEMI 위 포물선이 그려지다 '?'에서 멈춤", 0),
 ('G', "That takes cheat code two.", "생성 그림 P08 두툼한 열쇠 — 툭 떨어져 반짝", 1)],
'T38': [
 ('D', "Cheat code two is pushing a car without the road.", "도해: CHEAT 2 카드 — 바닥 없는 곳에서 뒤로 뿜는 화살표", 0),
 ('P', "Picture letting go of a balloon at a birthday party.", "실사: 생일 파티 풍선 묶음 사진(사람 없음, 무료 스톡) — 풍선 하나로 줌인", 0),
 ('V', "Air rushes out the back,", "실영상: 바람 빠지는 풍선이 지그재그로 날아감(무료 스톡)", 0),
 ('G', "and the balloon shoots the other way.", "생성 그림 RS_218 풍선이 고깔을 날리고 펀치 그릇에 첨벙 — 물방울 효과", 0)],
'T38a': [
 ('M', "Congrats. You've demonstrated propulsion", "움직이는 클립 VO_T38a: 풍선이 부엌을 두 번 가로지르고 ROBO 눈이 따라가다 한숨", 0),
 ('G', "and annoyed the host.", "생성 그림 RS_104 크림 묻은 주인 로봇 — 크림이 한 방울 뚝", 0)],
'T39': [
 ('V', "That's a cold gas thruster.", "실영상: ISS 안 SPHERES 위성이 CO2 냉가스를 칙 뿜으며 움직임(NASA, 사람 없는 구간)", 0),
 ('D', "Squeeze gas into a tank, let it out through a nozzle,", "도해: Commons 드 라발 노즐(PD) 위로 탱크 → 밸브 → 노즐 알갱이 흐름", 0),
 ('M', "and the reaction shoves you the opposite way.", "움직이는 클립 VO_T39: 흰 가스가 뒤로 퓨, 스케이트보드 ROBO가 화면 밖으로 쌩", 0)],
'T40': [
 ('M', "There's no fire, and nothing burns.", "움직이는 클립 VL_T40: 노즐의 흰 찬 가스가 흐르며 마시멜로에 서리가 번짐", 0),
 ('C', "It even works in a vacuum,", "문서: NASA CR-198531 표지(1996 냉가스 개관) — 제목 줄로 밀기, 칩 'NASA CR-198531 · spacecraft'", 0),
 ('V', "which is why spacecraft use them.", "실영상: 우주에서 자세 제어 가스를 뿜는 NASA 실험 장면(사람 없는 구간)", 0)],
'T41': [
 ('D', "So here are the two cheat codes side by side. One needs a nearby surface.", "도해: 좌우 분할 — 왼쪽 팬+바닥, 오른쪽 노즐+허공, 왼쪽 바닥이 빛남", 0),
 ('M', "The other doesn't.", "움직이는 클립: 바닥이 쑥 빠지자 왼쪽 차는 떨어지고 오른쪽 차는 가스로 계속 감", 0)],
'T42': [
 ('C', "And per one report, Tesla said on X", "문서: 보도 인용 카드('four to five times', 매체 칩)", 0),
 ('D', "that its thrusters push four to five times harder", "도해: 막대 'TIRES 1×' 옆 'THRUSTERS 4–5× (reported)'가 솟다가 초록 촛대로 바뀌어 화면 위를 뚫음(종목·가격 없음)", 0),
 ('P', "than the tires can.", "실사: NASA/JPL 화성 표면 사진 위 촛대 끝에 탄 작은 은빛 차 누끼 'TO MARS' — 칩 'Mars photo: NASA/JPL-Caltech'", 0)],
'T43': [
 ('G', "Tesla's wildest claim is that the top version, Rocket,", "생성 그림 RS_220 커피잔을 떨어뜨리는 놀란 ROBO — 빠른 줌인", 0),
 ('V', "hits sixty in under point five nine seconds.", "실영상: 스톱워치 초침이 0.59에서 탁 멈춤(무료 스톡, 숫자는 우리 글자 층)", 0),
 ('G', "By our math,", "생성 그림 RS_221 계산기에서 연기 펑 — 연기 효과 1회", 0),
 ('D', "that averages about four point six Gs.", "도해: '4.6 G' 막대가 사람 그림 옆에서 솟음, 칩 'our math'", 0)],
'T44': [
 ('V', "That's your seat shoving you forward", "실영상: NASA 원심분리기 팔이 도는 외부 장면(사람 얼굴 없는 구간)", 0),
 ('G', "with about four and a half times your own body weight.", "생성 그림 RS_156 좌석에 파묻힌 ROBO — 좌석 쪽으로 눌리는 흔들림 1회", 0)],
'T45': [
 ('C', "Tesla's own demo clip shows a slower point eight one seconds,", "문서: Tesla X 0-60 게시물 인용 카드 '0.81'(영상 칸은 원본 링크 표시)", 0),
 ('D', "and since the two may be timed differently,", "도해: 0.59 vs 0.81 두 칸, 출발선 위치가 서로 다르게 표시", 0),
 ('G', "we can't compare them yet.", "생성 그림 RS_222 코를 맞대고 다투는 심판 로봇 둘 — 좌우로 1회 흔들림", 0)],
'T48': [
 ('D', "So how much gas does cheat code two need? The Thrust version reportedly carries", "도해: 차 측면 투시 — 좌석 뒤 200 L 탱크와 후방 노즐 4개가 차례로 켜짐", 0),
 ('P', "a two-hundred-liter carbon-fiber tank", "실사: NASA 탄소섬유 감은 압력용기(COPV) 사진 — 섬유 결을 따라 패닝, 칩 'Photo: NASA'", 0),
 ('G', "feeding four rear nozzles.", "생성 그림 RS_106 황동 노즐 근접 — 흰 가스 효과 칙", 0)],
'T49': [
 ('G', "Rocket wants more.", "생성 그림 RS_224 빈 그릇을 내미는 TANK — 그릇 쪽으로 밀기", 0),
 ('D', "So where do you fit another four hundred liters in a car built for two?", "도해: 2인승 평면도 위로 '400 L' 상자가 자리를 찾아 이리저리 움직이다 조수석 위에서 멈춤", 1)],
'T51': [
 ('G', "So picture it. Your buddy texts,", "생성 그림 RS_225 ROBO 어깨 너머 폰 근접 — 폰 쪽으로 줌인", 0),
 ('D', "'Bro, I saved you a seat.'", "도해: 문자 말풍선 'Bro, I saved you a seat.'이 통통 튀며 뜸(우리 UI)", 0),
 ('M', "You open the door.", "움직이는 클립: ROBO가 조수석 문을 끝까지 들어 올림, 안은 그림자(RS_107 → RS_108 짝 그림 사이 직접 움직임)", 0)],
'T52': [
 ('P', "The tank called shotgun.", "실사 합성: 실제 차 조수석 사진 + NASA COPV 사진 누끼가 벨트를 매고 앉음 — BGM 뚝, 버클로 0.5초 급줌 정지, 칩 'photo collage'", 0)],
'T50': [
 ('G', "And that's not a bit.", "생성 그림 RS_110 ROBO가 미리 맨 자기 벨트를 조용히 풂 — 버클 딸깍 효과", 0),
 ('C', "The extra tank reportedly sits right where your passenger would.", "문서: Hagerty 보도 문구 카드(재조판, 출처 칩) — 'passenger' 형광", 0)],
'T53': [
 ('C', "Tesla's own description of Rocket says it's 'air ready,", "문서: tesla.com 문구 인용 카드 'air ready, with seating for one'", 0),
 ('D', "with seating for one.'", "도해: 좌석 배치도 — 조수석 칸이 탱크 아이콘으로 바뀜", 0)],
'T54': [
 ('D', "The full Rocket kit, per the same reports,", "도해: 투시도 노즐이 4개에서 10개로 하나씩 켜짐", 0),
 ('G', "has ten nozzles in all", "생성 그림 RS_228 노즐이 고슴도치처럼 박힌 은빛 차 — 반짝 효과", 0),
 ('M', "and six hundred liters of gas.", "움직이는 클립: 만화 탱크 게이지가 '600 L'까지 꿀렁꿀렁 차오름", 0)],
'T54a': [
 ('C', "Back in 2018, Musk tweeted about a SpaceX package for this car", "문서: 2018 트윗 인용 카드('~10 small rocket thrusters', 칩 'Musk on Twitter · Jun 2018')", 0),
 ('D', "with roughly ten small thrusters.", "도해: 차 실루엣에 작은 노즐 아이콘 10개가 하나씩 찍힘", 0),
 ('P', "The car is years late,", "실사: NASA/JPL 화성 표면 사진 위 우주복 MUSK 이름표 로봇(2D 컷아웃)이 쌍안경으로 하늘을 보며 환호, 칩 'Mars photo: NASA/JPL-Caltech'·'parody'", 0),
 ('M', "but the nozzles showed up on time.", "움직이는 클립(2D 컷아웃만): 낙하산 상자가 먼지 일으키며 착지 → 열리면 노즐 10개뿐, 로봇이 하나를 번쩍 들자 흰 가스 퓩", 0)],
'T56': [
 ('C', "Reports say the tanks are built for up to ten thousand psi,", "문서: 보도 인용 카드 '10,000 psi'(매체 칩)", 0),
 ('V', "and an event screen reportedly showed", "실영상: 압력계 바늘이 쭉 오르는 근접(무료 스톡)", 0),
 ('D', "fifty-five hundred.", "도해: 게이지 숫자 '5,500 psi (reported)'가 바늘 끝에 붙음", 0)],
'T58': [
 ('D', "That's hundreds of times the air pressure", "도해: 사람 머리 위 공기 기둥 1개 vs 수백 개가 쌓이는 비교", 0),
 ('C', "around you right now.", "문서: NIST 압력 단위 표 — psi·atm 행으로 확대, 칩 'Source: NIST'", 0)],
'T58a': [
 ('P', "Pressure like that isn't new.", "실사: CNG 버스 사진(무료 스톡) — 지붕 탱크 쪽으로 밀기", 0),
 ('P', "Hydrogen cars like the Toyota Mirai already carry about ten thousand psi.", "실사: Commons Toyota Mirai 사진(CC0) — 왼→오 패닝, 칩 '≈10,000 psi'", 0),
 ('G', "What's new is a car built to let it out.", "생성 그림 RS_106 노즐(2회째) — 흰 가스가 길게 뿜어지는 효과", 0)],
'T59': [
 ('G', "I did some rough math, so treat it as an estimate.", "생성 그림 RS_158 손가락으로 셈하는 ROBO — 손가락 효과음 박자에 맞춰 살짝 흔들림", 0),
 ('D', "At that pressure, a full load is about two hundred sixty kilograms of gas,", "도해: 600 L 탱크 → 저울 눈금 '≈260 kg (estimate)'가 올라감", 0),
 ('G', "around five hundred seventy pounds.", "생성 그림 RS_233 저울이 바닥을 뚫음 — 먼지 구름 퍽 + 화면 1회 쿵", 0)],
'T60': [
 ('M', "That's about the weight of three adults,", "움직이는 클립 T60_s2(기존): 덩치 로봇 셋이 한 좌석에 끼어 꿈틀", 0),
 ('G', "and it's all gas.", "생성 그림 RS_235 셋이 흰 가스 구름 모양으로 바뀜 — 구름이 살짝 부풂", 0)],
'T61a': [
 ('P', "That leaves one seat for an actual human,", "실사: 빈 운전석 사진(무료 스톡, 로고 없음) — 좌석으로 줌인", 0),
 ('M', "and you're out on the curb", "움직이는 클립 VL_T61a: 멀리 은빛 차가 먼지와 떠나고 ROBO 고개만 따라감", 0),
 ('G', "holding a seatbelt you don't need anymore.", "생성 그림 RS_239 버클을 꽃다발처럼 든 ROBO — 마른 잎 효과가 지나감", 0)],
'T63': [
 ('D', "Reports differ on whether that kickflip car was steered remotely", "도해: 보도 두 갈래 화살표 'REMOTE?' / 'SELF-DRIVING?'", 1),
 ('G', "or drove itself.", "생성 그림 RS_160 혼자 도는 핸들 — 게임 경고창 'CONTROLLER DISCONNECTED'가 툭 뜸", 0)],
'T63a': [
 ('G', "Either way, nobody had to sit in it,", "생성 그림 RS_111 빈 운전석에 놓인 헬멧 — 밀기 3%", 0),
 ('P', "which I think was", "실사: 빈 의자 위 레이싱 헬멧 사진(무료 스톡) — 짧은 줌", 0),
 ('G', "the smartest call of the whole event.", "생성 그림 RS_237 비치 의자에서 쉬는 충돌 시험 인형 로봇 — 파라솔 그림자 흔들림", 0)],
'T64': [
 ('M', "Up there, there's no surface and no road, but thrown gas needs neither.", "움직이는 클립: 위아래 분할 — 위 'then: video games' 장난감 차가 파란 부스트로 공중 회전, 아래 'now: Texas, 2026' 재현 클립 R1 리플레이, 회전 시점 맞춤", 0),
 ('D', "That's cheat code two.", "도해: 궤적 위 가스 화살표 + 'CHEAT 2 ✓', 자물쇠 P07 열림", 0)],
'T65': [
 ('G', "Same caveat as before.", "생성 그림 RS_017 김 서린 돋보기(2회째, 콜백) — 김 효과", 0),
 ('D', "We couldn't confirm exactly how this demo used the thrusters.", "도해: 노즐 도해가 흐려지고 물음표 3개가 떠오름", 0)],
'T66': [
 ('G', "Okay, cool tricks. Now the bill.", "생성 그림 RS_238 은쟁반 계산서를 내미는 웨이터 로봇 — 쟁반 쪽으로 줌", 1),
 ('V', "If you buy Rocket,", "실영상: 영수증 프린터에서 종이가 쭉 나옴(무료 스톡)", 0),
 ('D', "you've already paid with your passenger seat.", "도해: 영수증 첫 줄 'PASSENGER SEAT' 도장", 0)],
'T67': [
 ('D', "Next on the bill is the gas.", "도해: 영수증 둘째 줄 'GAS'가 타자기처럼 찍힘", 0),
 ('M', "Reportedly, a full load gives you a few seconds of thrust.", "움직이는 클립: 만화 게이지 RS_042 바늘이 몇 초 만에 100→0으로 뚝", 0)],
'T67a': [
 ('M', "Picture flying to work. A few seconds later,", "움직이는 클립: 만화 현관 보안카메라 어안 화면('MON 7:58 AM' 글자 층) — 은빛 차가 울타리 위로 솟음 → 가스 픽 꺼짐 → 코가 숙여짐", 0),
 ('V', "you're in your neighbor's pool.", "실영상: 수영장 물기둥 첨벙(무료 스톡, 사람 없음)", 0)],
'T68': [
 ('G', "(무대사 1.2초)", "생성 그림 RS_032 밈 정지 — 움직임 없이 정적, 효과음만", 0)],
'T69': [
 ('P', "Refilling all six hundred liters reportedly takes six to seven hours,", "실사: 공기 압축기 사진(무료 스톡) + 타이머 '6–7 h' 글자 층", 0),
 ('G', "with a goal of about half an hour.", "생성 그림 RS_162 압축기 옆에서 밤새는 ROBO — 별 효과가 깜박", 0)],
'T70': [
 ('V', "In that time, you could make dinner,", "실영상: 냄비에서 김이 오르는 근접(무료 스톡)", 0),
 ('G', "eat dinner,", "생성 그림 RS_034 혼자 저녁 먹는 ROBO — 빠른 줌", 0),
 ('P', "and do the dishes.", "실사: 설거지 건조대 사진(무료 스톡) — 짧은 밀기", 0)],
'T71': [
 ('G', "And it would still be filling.", "생성 그림 RS_163_r2 아직 1%인 게이지 앞 ROBO — 바늘만 미세하게 떨림", 0)],
'T71a': [
 ('P', "Meanwhile, the friend you left on the curb texts you,", "실사: 휴대폰 잠금 화면 사진(무료 스톡, 빈 화면) 위로 알림 배너가 내려옴", 0),
 ('G', "'Need a ride?'", "생성 그림 RS_243 연석의 BUDDY가 의기양양하게 문자 — 말풍선 'Need a ride?' 툭", 0)],
'T73': [
 ('V', "Next up, the road. Picture Monday morning traffic,", "실영상: 아침 정체 고속도로 항공 장면(무료 스톡, 번호판 안 보임)", 0),
 ('G', "with ten nozzles and your thumb", "생성 그림 RS_164 부스트 버튼 위의 엄지 — 버튼으로 급줌", 0),
 ('M', "on the boost button.", "움직이는 클립: 만화 은빛 차가 정체 위로 훅 솟고 수배 별 다섯 개가 켜짐", 0)],
'T74': [
 ('D', "Tesla's own page says Rocket is", "도해: 직전 프레임이 흑백으로 정지 + 빨간 도장이 쾅", 0),
 ('C', "'not approved for public road use.'", "문서: tesla.com 문구 인용 카드 'not approved for public road use' + 출처 칩", 0)],
'T75': [
 ('V', "Clearing a truck", "실영상: 정체 속 운전석 시점(무료 스톡) — 위로 만화 은빛 차 누끼가 옆으로 돌며 넘어감, 'POV: 2036 commute'", 0),
 ('G', "doesn't clear you for the highway.", "생성 그림(새) ROBO 운전석 초저각 올려다보기 — 'HOLY MOLY' 글자가 튐", 0)],
'T76': [
 ('C', "As for the price, Reuters reported", "문서: Reuters 보도 문구 카드(재조판, 'Reuters · Oct 2026')", 0),
 ('G', "that Tesla didn't give one.", "생성 그림 RS_044 물음표 가격표와 딜러 로봇 — 가격표가 흔들림", 0)],
'T77': [
 ('D', "What you can do is reserve the Performance", "도해: 예약 단계 3칸(RESERVE → WAIT → PRICE?)이 하나씩 켜짐", 0),
 ('G', "for fifty thousand dollars.", "생성 그림 RS_246 돈 수레를 밀고 온 ROBO와 작은 종이 한 장 — 종이로 줌", 0)],
'T78': [
 ('P', "That's not the price.", "실사: 번호표 발급기 사진(무료 스톡) — 번호표가 툭", 0),
 ('G', "That's your place in line.", "생성 그림 RS_247 지평선까지 이어진 로봇 줄 — 줄 끝 ROBO까지 긴 패닝", 0)],
'T80': [
 ('M', "If all this sounds familiar, it should.", "움직이는 클립: 화면이 VHS 되감기처럼 감기며 연도 칩이 2026 → 2017로 내려감", 0),
 ('P', "Tesla first unveiled the new Roadster in 2017", "실사: Commons 2세대 로드스터 시제품 사진(Grand Basel 2018, CC BY-SA 4.0) — 칩 'unveiled Nov 2017 · photo 2018'", 0),
 ('C', "and promised it for 2020.", "문서: 2017 보도 문구 카드 + 'promised: 2020' 칩", 0)],
'T81': [
 ('P', "Back then, Tesla's page", "실사: Commons 시제품 실내 사진(2019, CC BY 2.0) — 좌석 쪽으로 밀기", 0),
 ('C', "listed four seats.", "문서: Wayback tesla.com/roadster(2017) 'Seating 4' 인용 카드", 0)],
'T82': [
 ('D', "Rocket has one.", "도해: 좌석 아이콘 4개를 선택 점선이 둘러싸고 '[SEAT DELETED]' — 3개가 사라지고 1개 남음", 0)],
'T82a': [
 ('V', "Then 2020 came and went,", "실영상: 일력이 빠르게 넘어감(무료 스톡) — '2020' 장에서 쿵", 0),
 ('G', "and the people who'd put down deposits", "생성 그림 RS_250a 현관 계단에서 영수증을 든 행복한 ROBO — 고정", 0),
 ('M', "kept waiting.", "움직이는 클립 VL_T82a: 몇 년 뒤 같은 현관 RS_250b, 낙엽이 화면을 가로지르고 거미줄이 흔들림", 0)],
'T84a': [
 ('G', "Even Sam Altman reserved one in 2018,", "생성 그림 RS_059 ALTMAN 이름표 로봇(2D 컷아웃) — 옆으로 살짝 밀려 들어옴", 0),
 ('C', "and last year he posted that his refund email", "문서: X 게시물 인용 카드 + 칩 'Sam Altman on X · Oct 31, 2025'", 0),
 ('G', "bounced after seven and a half years.", "생성 그림 RS_251 벽에 고무공처럼 튕기는 흰 봉투 — 튕김 곡선 효과", 0)],
'T84b': [
 ('G', "Musk replied", "생성 그림 RS_059b MUSK 이름표 로봇(2D 컷아웃) — 'MUSK'S REPLY' 띠가 깔림", 0),
 ('C', "that Altman got his money back within a day.", "문서: Musk 답글 인용 카드 — 두 출처 칩을 같은 크기로 좌우 나란히", 0)],
'T84c': [
 ('P', "Days later, Musk picked April Fools' Day", "실사: 일력 'APR 1' 장 사진(무료 스톡) — 쾅 하고 화면 1회 흔들림", 0),
 ('G', "for the demo,", "생성 그림 RS_253 달력과 파티 나팔을 든 MUSK 이름표 로봇(2D) — 색종이 효과", 0),
 ('C', "and said that gave him some deniability.", "문서: 인용 카드 두 토막 'I have some deniability…' → '…I was just kidding.' + 칩, 'deniability' 형광", 0)],
'T84d': [
 ('M', "(무대사 0.8초)", "움직이는 클립(2D 컷아웃만): 이름표 'MUSK'의 U가 뒤집혀 A로 끼워지고 가면이 척 — 0.6초부터 정지", 0)],
'T84e': [
 ('C', "April 1st got pushed before it even arrived.", "문서: TFL 기사 제목 띠 '…Reveal Date on April 1, Because Of Course It Is' + 칩 'TFL · Nov 7, 2025'", 0),
 ('V', "After that, the date just kept slipping.", "실영상: 공항 플랩 안내판이 촤르륵 넘어감(무료 스톡) — 위에 우리 글자 줄 'DELAYED' 세 줄이 차례로 합성", 0),
 ('D', "Then came a weather delay.", "도해: 안내판 마지막 줄 'OCT 1 → OCT 15 · WEATHER' + 칩", 0)],
'T84f': [
 ('D', "Until, finally, it showed up", "도해: 안내판 줄이 'OCT 15 · DEPARTED'로 바뀌며 초록불", 0),
 ('M', "and did a kickflip over a Semi.", "재현 클립 R7: 킥플립을 다른 각도(정면 낮은 시점)에서 다시, 착지 먼지", 0)],
'T84g': [
 ('G', "Okay, that was", "생성 그림 RS_254 소파 위에서 천천히 박수 치는 ROBO — 팝콘 효과가 흩어짐", 0),
 ('M', "a hell of a demo.", "움직이는 클립: 현관 예약자 ROBO(RS_250c)가 먼지를 털며 벌떡 일어나 누런 영수증을 하늘로 듦", 0)],
'T83': [
 ('D', "But Musk says", "도해: 착지 프레임이 2프레임 떨리고 버퍼링 아이콘(1.5초 이내)", 1),
 ('C', "production starts in 2028.", "문서: AP 보도 문구 카드 + 타임라인 '2028 PRODUCTION · Musk says', 칩 'via AP'", 0)],
'T84': [
 ('M', "Still waiting.", "움직이는 클립: 같은 현관에서 ROBO가 털썩 다시 앉고 같은 자세 해골 로봇(RS_303B)으로 바뀜, 거미줄만 흔들림", 0)],
'T85': [
 ('G', "Okay, quick reality check.", "생성 그림 RS_038 공중의 상자 셋이 바닥에 쾅 — 화면 1회 쿵", 0)],
'T86': [
 ('D', "What we can confirm is the physics,", "도해: 'CONFIRMED' 상자에 흡착컵·풍선 아이콘이 쏙 들어감", 0),
 ('C', "and that Tesla posted the demos.", "문서: Tesla X 게시물 카드 축소판이 같은 상자로 들어감", 0)],
'T87': [
 ('P', "The acceleration numbers, the tanks,", "실사: 스톱워치·COPV 사진 누끼가 'TESLA SAYS' 상자로 떨어짐", 0),
 ('D', "and the demo details are still Tesla's claims.", "도해: 상자 뚜껑에 'CLAIMS' 도장 쾅", 0)],
'T88': [
 ('G', "And your bill is a passenger seat,", "생성 그림 RS_226 분필 윤곽 좌석의 TANK — 밀기 3%", 0),
 ('G', "hours of refilling,", "생성 그림 RS_162 밤새는 ROBO(2회째) — 빠른 줌", 0),
 ('C', "no public roads,", "문서: 'not approved for public road use' 도장 카드(2회째) — 툭", 0),
 ('G', "and no price yet.", "생성 그림 RS_044 물음표 가격표(2회째) — 가격표 흔들림", 0)],
'T89': [
 ('D', "These cheat codes are old.", "도해: 오락기 메뉴 'CHEAT CODES: 2' 콜백 — 글자가 낡은 색으로 바램", 0),
 ('P', "A 1978 race car used one,", "실사: Commons BT46B 후면 사진(2회째) — 짧은 밀기", 0),
 ('V', "and spacecraft use the other.", "실영상: SPHERES 냉가스 분사(T39와 다른 구간, NASA)", 0),
 ('M', "If both really work on one car, that's wild engineering.", "움직이는 클립: 세 칸 분할(팬카·우주·재현 클립)이 하나로 합쳐지며 재현 킥플립 마지막 프레임", 0)],
'T89a': [
 ('V', "If it doesn't,", "실영상: 풍선이 바람 빠지며 날아감(T38과 다른 클립, 무료 스톡)", 0),
 ('M', "that's a very expensive balloon.", "움직이는 클립 VL_T89a: 풍선처럼 끈에 매달린 은빛 차가 둥실, 빈 가격표 달랑", 0)],
'T89b': [
 ('G', "Honestly, I want this to work.", "생성 그림 RS_114 밤 차고의 ROBO — 아주 느린 밀기", 0),
 ('M', "I just want to know when an amazing demo becomes", "움직이는 클립: 빈 운전석으로 손을 뻗다 멈춤(RS_114 → RS_060 짝 그림 사이 직접 움직임, 느리게)", 0),
 ('G', "something you'd actually sit in.", "생성 그림 RS_304B(또는 C) 처음 운전석에 앉은 ROBO — 고정, 작업등만 깜박", 0)],
'T90': [
 ('V', "Zero to sixty is fast.", "실영상: 스톱워치 탁(T43과 다른 구간, 무료 스톡)", 0),
 ('M', "Order to driveway is still pending.", "움직이는 클립 VL_T90: 모래시계 모래가 흐르고 ROBO가 한 번 깜박", 0)],
'T91': [
 ('D', "So would you trade your passenger seat,", "도해: 투표 카드 'TRADE THE SEAT / KEEP THE SEAT' — 막대가 출렁", 0),
 ('G', "and whoever usually sits there,", "생성 그림 RS_257 조수석의 BUDDY와 창밖에서 샘내는 TANK — 밀기 3%", 0),
 ('G', "for a few seconds of thrust? Tell us in the comments,", "생성 그림 RS_171 달려가는 TANK — 속도선 효과", 0),
 ('M', "and send this to the friend who always calls shotgun.", "움직이는 클립: 탱크가 작은 팔로 세 번 손 흔들기, 배경 고정(RS_041 → RS_115 짝 그림 사이 직접 움직임)", 0)],
'T92': [
 ('G', "Subscribe, and see you next meltdown.", "생성 그림 RS_305B 연석에서 음료를 나눠 마시는 ROBO와 TANK — 구독 버튼이 툭 튐", 0)],
}
