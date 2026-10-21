# 사용: python3 -I wc_script.py <02_대본 파일 또는 낭독본 txt>
# **[낭독본 (영어)]** 아래(또는 ```text 블록)의 영어 낭독본 단어 수와 기본 규칙을 점검한다.
import re, sys
src = open(sys.argv[1], encoding='utf-8').read()
m = re.search(r'\*\*\[낭독본 \(영어\)\]\*\*(.*?)(?=\n\*\*\[|\Z)', src, re.S)
body = m.group(1) if m else src
cb = re.search(r'```(?:text)?\n(.*?)```', body, re.S)
if cb: body = cb.group(1)
lines = [l.strip() for l in body.splitlines()]
text_lines = [l for l in lines if l and not l.startswith('#') and not l.startswith('```')]
words = [w for w in re.split(r'\s+', ' '.join(text_lines)) if re.search(r'[A-Za-z0-9]', w)]
print(f'단어 수: {len(words)}  (기준 1,400–1,600) -> {"맞음" if 1400 <= len(words) <= 1600 else "어김"}')
print(f'문장 줄 수: {len(text_lines)}  덩어리(빈 줄로 나뉜 묶음) 수: {len([b for b in re.split(r"\n\s*\n", body) if b.strip()])}')
multi = [l for l in text_lines if len(re.findall(r'[.!?]["\'’”)]?\s+[A-Z]', l)) >= 1]
print(f"(참고) 한 줄에 두 문장 이상인 줄: {len(multi)} — v5는 장면 한 줄 방식이라 어김 아님. 새 편은 가능하면 한 줄 한 문장")
for l in multi[:15]: print('  -', l[:110])
print('끝인사 고정 문구:', '맞음' if text_lines and text_lines[-1] == 'Subscribe, and see you next meltdown.' else f'어김 (마지막 줄: {text_lines[-1] if text_lines else "없음"})')
HE = 'hold ' + 'everything'
pre_verify = src.split('## 검증 출력')[0]
print('금지 문구(H.E.) 낭독본 안:', '어김(있음)' if re.search(HE, body, re.I) else '없음',
      '/ 파일 본문(검증 출력 제외):', '있음(설명 문장인지 확인)' if re.search(HE, pre_verify, re.I) else '없음')
