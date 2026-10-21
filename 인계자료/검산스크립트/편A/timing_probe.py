import json
J='/tmp/claude-0/-home-user--/f74f8fd9-d08b-56d5-a2e9-6c58b1e53757/scratchpad/작업/편A_장면순서.json'
d=json.load(open(J,encoding='utf-8'))
tot=0
for x in d:
    w=len(x['text'].split()); t=w/2.7; tot+=t
    print(x['id'],w,round(t,2))
print('words',sum(len(x['text'].split()) for x in d),'sec',round(tot,1))
