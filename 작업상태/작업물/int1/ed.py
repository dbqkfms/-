# 공통: 정확히 한 번 나오는 문자열만 바꾼다
class Ed:
    def __init__(self, path):
        self.path = path; self.s = open(path, encoding='utf-8').read()
    def rep(self, old, new, count=1):
        n = self.s.count(old)
        if n != count: raise SystemExit(f'[{self.path}] 찾은 수 {n} (기대 {count}): {old[:80]!r}')
        self.s = self.s.replace(old, new)
    def save(self):
        open(self.path, 'w', encoding='utf-8').write(self.s)
