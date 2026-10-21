import json, sys, re
lines = [l.strip() for l in open(sys.argv[1], encoding='utf-8').read().splitlines()]
sents = [l for l in lines if l]
merge_starts = {
 "I keep thinking about that stock chart, though.",
 "Okay, enter the AI.",
 "Has AI actually found a real superconductor, then?",
 "What would it take to convince you?",
}
scenes=[]; i=0
while i < len(sents):
    s = sents[i]
    if s in merge_starts:
        scenes.append(s + " " + sents[i+1]); i += 2
    else:
        scenes.append(s); i += 1
out = [{"id": f"S6-{n+1:02d}", "text": t} for n,t in enumerate(scenes)]
json.dump(out, open(sys.argv[2],'w',encoding='utf-8'), ensure_ascii=False, indent=2)
for o in out: print(o["id"], "|", len(o["text"].split()), "|", o["text"])
print("scenes:", len(out))
