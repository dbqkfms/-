import sys, re, json
sys.path.insert(0, '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1')
from ed import Ed
from collections import OrderedDict
e = Ed('/home/user/-/results/06_모션계획_001_로드스터.md')
r = json.load(open('/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/int1/rows04.json'))
sc = OrderedDict()
for x in r: sc.setdefault(x['scene'], []).append(x)

e.rep("**한 줄 결론:** 움직이는 장면은 38개로 전체의 38%다(기준 30% 이상).",
      "**한 줄 결론:** 04 v5.1 최종 장면표 기준으로 움직이는 장면은 38개, 전체의 38%다(기준 30% 이상).")
e.rep("3. 무료 스톡·NASA 실영상 16개는", "3. 무료 스톡·NASA 실영상 17개는")
e.rep("거의 멈춘 장면은 T29·T68(무대사 밈 정지)과 T07a(QUIET 진심 줄)뿐이고",
      "거의 멈춘 장면은 T29(밈 둘째 컷)·T68(무대사 반응 정지)과 T07a(QUIET 진심 줄)뿐이고")
# 행 문구
def row(k, kind, text):
    ls = e.s.split('\n'); hit = [i for i, l in enumerate(ls) if l.startswith(f'| {k} | ')]
    assert len(hit) == 1, k
    old = ls[hit[0]].split(' | ')
    ls[hit[0]] = f"| {k} | {kind or old[1]} | {old[2]} | {text} |"; e.s = '\n'.join(ls)
row('T05', None, "램프 진입 실영상(Tesla 원본 2.5초)이 흐른다. 이어서 은빛 C판 만화 차가 램프를 거꾸로 따라 돈 뒤 끝에서 떨어져 바퀴로 쿵 내려앉고 먼지가 퍼진다(위쪽 각도, 재현 R1).")
row('T40', '텍스트 + 카메라(실영상)', "NASA 냉가스 문구 카드('There is no combustion in cold gas systems')가 붙고 'no combustion'에 형광이 그어진 뒤, ISS 안 SPHERES 위성이 CO2 가스를 칙 뿜으며 움직이는 실영상으로 넘어간다.")
row('T60', None, "덩치 로봇 둘과 같은 로봇을 반 크기로 줄인 하나가 한 좌석에 끼어 꿈틀거린다(기존 클립 T60_s2를 다시 편집, 새 캐릭터 아님). 다음 컷에서 셋이 가스 구름 모양으로 바뀌어 살짝 부푼다.")
row('T84f', None, "우리 안내판 그래픽의 'DEPARTED' 줄이 1.3초 동안 걷히고, 실제 킥플립 다른 구간이 Tesla 원본 3.0초 이하로 흐른다.")
row('T03', None, "실제 착지 장면을 0.4배속으로 흘린다(화면 2.9초, Tesla 원본 1.2초 안팎). 다음 소파 컷은 3% 밀기와 함께 팝콘 통 누끼가 떨어진다.")
row('T18a', None, "킥플립 정점 구간을 0.5배속으로 흘리다 'freeze'에서 정지한다(레코드 긁힘 효과음). 정지 화면 앞으로 일시정지 리모컨을 든 ROBO 누끼가 툭 들어온다.")
# 길이 열 다시 계산
ls = e.s.split('\n')
for i, l in enumerate(ls):
    m = re.match(r'\| (T\w+) \| (.*?) \| ([\d.]+) \| (.*) \|$', l)
    if m and m.group(1) in sc:
        L = sum(c['b'] - c['a'] for c in sc[m.group(1)] if c['code'] in 'VM')
        ls[i] = f"| {m.group(1)} | {m.group(2)} | {L:.1f} | {m.group(4)} |"
e.s = '\n'.join(ls)
e.rep("- `길이(초)`는 그 장면에서 실영상·움직이는 클립 컷의 길이를 더한 값이다(04 시간 기준, TTS 실측 뒤 다시 맞춤).",
      "- `길이(초)`는 그 장면에서 실영상·움직이는 클립 컷의 길이를 더한 값이다(04 v5.1 최종 시간 기준으로 통합 서브가 다시 계산, TTS 실측 뒤 다시 맞춤).")
e.rep("  - VL_T02a(비서 로봇 액자 닦기): T02a 문장이 v5.1로 바뀌는 중이라 클립 자체를 보류했다. 도해 답글 폭포와 문서 카드로 둔다.",
      "  - VL_T02a(비서 로봇 액자 닦기): 쓰지 않는다. T02a v5.1 최종 문장은 수량·회사명 없는 중립 문장이라 'BOSS' 액자 장면이 맞지 않는다(메인 판단). 도해 말풍선과 SlashGear 기사 제목 카드로 둔다.")
e.rep(e.s[e.s.index("- **Tesla 짧은 인용 8곳"):e.s.index("## 어지러움 막기")],
"""- **Tesla 짧은 인용 7곳(T01·T03·T05·T18a·T22·T32·T84f):** 실영상으로 셌다. 곳마다 Tesla 원본은 3.0초 이하다(B-1 '1–3초', 검토 ⑤). T45 0-60 클립(Q7)은 원본이 1.04초뿐이라 쓰지 않고 무료 스톡 디지털 타이머로 바꿨다(T45는 움직이는 장면이 아니다). 공정 이용 판단이 로컬에서 막히면 7곳은 재현 움직이는 클립으로 바뀐다. 어느 쪽이든 움직이는 장면으로 남으므로 38%는 바뀌지 않는다. 04의 배합 보정안(T61a-1·T87-1·T69-1을 실영상으로, T64-1·T89-3·T41-2를 도해로)을 함께 쓰면 37%다(T41·T64·T89가 빠지고 T69·T87이 들어온다, 통합 서브 계산).

""")
e.save(); print('06 편집 완료')
