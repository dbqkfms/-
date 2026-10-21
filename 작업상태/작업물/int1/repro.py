import os, sys, re
S3 = '/tmp/claude-0/-home-user--/56f55c83-9764-5580-8ba0-498367ae7c80/scratchpad/s3'
os.chdir(S3); sys.path.insert(0, S3)
import gen
tab = gen.table()
F = '/home/user/-/results/04_장면_001_로드스터.md'
cur = [l for l in open(F, encoding='utf-8').read().splitlines() if l.startswith('| T')]
new = [l for l in tab.splitlines() if l.startswith('| T')]
print(len(cur), len(new))
d = 0
for a, b in zip(cur, new):
    if a != b:
        d += 1
        if d <= 15: print('CUR', a[:230]); print('NEW', b[:230]); print()
print('diff rows', d)
