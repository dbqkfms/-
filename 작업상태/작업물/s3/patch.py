# v2 → v3: 생성 그림 20% 초과분을 실사·도해로, 실사 비중 올림, 같은 사진 3회 사용 막음
from plan import PLAN
def setc(sid, i, code, mot, q=None):
    c = list(PLAN[sid][i]); c[0] = code; c[2] = mot
    if q is not None: c[3] = q
    PLAN[sid][i] = tuple(c)
setc('T14', 1, 'P', "실사: 짐을 가득 실어 아래가 불룩해진 트럭 타이어 근접 사진(무료 스톡) — 위에서 아래로 1회 눌리는 흔들림")
setc('T33', 1, 'P', "실사: 김 서린 돋보기 사진(무료 스톡) + 칩 'FAN SETTINGS: ?' — 김이 퍼지는 효과")
setc('T65', 0, 'P', "실사: 같은 김 서린 돋보기 사진(2회째, 콜백) — 짧은 줌")
setc('T43', 0, 'P', "실사: 스포츠카 속도계 사진(무료 스톡, 로고 없음) + 'Tesla claim: 0–60 < 0.59 s' 글자 층 — 바늘 쪽으로 빠른 줌인")
setc('T66', 0, 'P', "실사: 고급 식당 계산서 폴더 사진(무료 스톡, 손 없음) — 폴더 쪽으로 줌, 효과음 '띵'", 1)
setc('T70', 1, 'P', "실사: 차려진 저녁 한 접시 사진(무료 스톡) — 빠른 줌")
setc('T85', 0, 'D', "도해: 상자 셋 'CONFIRMED · TESLA SAYS · YOUR BILL'이 공중에서 바닥에 쾅 — 화면 1회 쿵")
setc('T89b', 0, 'P', "실사: 밤의 문 닫힌 자동차 전시장 사진(무료 스톡, 로고 없음) — 아주 느린 밀기(QUIET)")
setc('T77', 0, 'P', "실사: 카드 결제 단말기 사진(무료 스톡) + '$50,000 RESERVATION' 글자 층 → 예약 단계 3칸(RESERVE → WAIT → PRICE ?) 띠가 아래에 깔림")
setc('T88', 1, 'P', "실사: 'ROAD CLOSED' 표지판 사진(무료 스톡) — 툭 하고 들어옴")
setc('T48', 1, 'P', "실사: NASA 탄소섬유 감은 압력용기(COPV) 사진 A — 섬유 결을 따라 패닝, 칩 'Photo: NASA'")
setc('T52', 0, 'P', "실사 합성: 실제 차 조수석 사진 + NASA COPV 사진 B 누끼가 벨트를 매고 앉음 — BGM 뚝, 버클로 0.5초 급줌 정지, 칩 'photo collage'")
setc('T87', 0, 'P', "실사: 스톱워치 사진 + COPV 사진 A 누끼(2회째)가 'TESLA SAYS' 상자로 떨어짐")
PLAN['T22'] = [
 ('D', "Cheat code one.", "도해: CHEAT 1 카드가 오락기 메뉴에서 깜박이며 선택됨", 0),
 ('V', "The car rolls onto the ramp and keeps going upside down.", "실영상(Tesla 짧은 인용 Q5, 약 3.5초, Q3과 다른 구간): 거꾸로 주행 느리게, 칩 'Video: Tesla'", 0),
 PLAN['T22'][1]]
