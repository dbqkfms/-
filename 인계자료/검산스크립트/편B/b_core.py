# -*- coding: utf-8 -*-
# 편 B 공통 계산: 시간·완성 화면 id·검산. b_build.py와 b_check.py가 함께 쓴다.
import json, math, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import b_data as D

JSON_PATH = "/tmp/claude-0/-home-user--/f74f8fd9-d08b-56d5-a2e9-6c58b1e53757/scratchpad/작업/편B_장면순서.json"

def load():
    order = json.load(open(JSON_PATH, encoding="utf-8"))
    assert [s["id"] for s in order] == [s["id"] for s in D.S], "장면 id 순서가 JSON과 다름"
    # 시간: 낭독 단어/2.7 + 박자, 누적 후 반올림 → 빈틈 없는 정수 경계
    t = 0.0; bounds = [0]
    for i, s in enumerate(order, 1):
        w = len(s["text"].split())
        t += w / 2.7 + D.EXTRA.get(i, D.DEFAULT_EXTRA)
        bounds.append(round(t))
    scenes = []
    sh_n = 0; sh_of_scene = {}
    for i, (s, d) in enumerate(zip(order, D.S)):
        start, end = bounds[i], bounds[i + 1]
        cuts = []
        for (mat, ref, desc) in d["cuts"]:
            if ref and ref.startswith("REUSE:"):
                src = ref.split(":", 1)[1]
                # 원본 장면의 같은 재료 첫 컷 id를 재사용
                sid = [c for c in sh_of_scene[src] if c[0] == mat][0][1]
                cuts.append((mat, sid, desc, True))
            elif ref and ref.startswith("B-SH"):
                sh_n += 1
                cuts.append((mat, ref, desc, False))
            else:
                sh_n += 1
                cuts.append((mat, "B-SH%03d" % sh_n, desc, False))
        sh_of_scene[s["id"]] = [(c[0], c[1]) for c in cuts]
        n = len(cuts)
        cnt = {}
        for c in cuts: cnt[c[0]] = cnt.get(c[0], 0) + 1
        top = max(cnt.values())
        tops = [m for m in cnt if cnt[m] == top]
        moving_cuts = sum(1 for c in cuts if c[0] in ("MC", "RV"))
        moving = moving_cuts * 2 >= n
        if len(tops) == 1:
            main = tops[0]
        else:
            # 동수: 움직이는 클립/실영상이 있으면 그것(움직이는 장면 판정과 일치), 없으면 첫 컷 재료
            mv = [m for m in tops if m in ("MC", "RV")]
            main = mv[0] if mv else [c[0] for c in cuts if c[0] in tops][0]
        scenes.append(dict(id=s["id"], text=s["text"], words=len(s["text"].split()), start=start, end=end,
                           cuts=cuts, n=n, cnt=cnt, main=main, moving=moving, data=d,
                           flag="○" if (i + 1) in D.FLAGS else "—"))
    return order, scenes, sh_n

def cut_starts(scenes):
    out = []
    for s in scenes:
        dur = s["end"] - s["start"]
        for k, c in enumerate(s["cuts"]):
            out.append((s["start"] + dur * k / s["n"], s["id"], c[0], c[1]))
    return out

def checks(scenes):
    total = scenes[-1]["end"]
    cs = cut_starts(scenes)
    windows = []
    w0 = 0
    while w0 < total:
        w1 = min(w0 + 30, total)
        inwin = [c for c in cs if w0 <= c[0] < w1]
        length = w1 - w0
        lo, hi = (6, 10) if length == 30 else (round(6 * length / 30), round(10 * length / 30))
        # 재료 바뀜(진단): 구간 안 컷 사이 재료가 바뀐 횟수(구간 첫 컷은 직전 컷과 비교)
        idx0 = cs.index(inwin[0]) if inwin else None
        changes = 0
        if inwin:
            for j in range(idx0, idx0 + len(inwin)):
                if j > 0 and cs[j][2] != cs[j - 1][2]:
                    changes += 1
        windows.append((w0, w1, len(inwin), lo, hi, lo <= len(inwin) <= hi, changes))
        w0 += 30
    # 재료 연속
    mats = [s["main"] for s in scenes]
    maxrun, run, runs = 1, 1, []
    for a, b in zip(mats, mats[1:]):
        run = run + 1 if a == b else 1
        maxrun = max(maxrun, run)
    # 움직이는 장면
    mv = [s["id"] for s in scenes if s["moving"]]
    # 완성 화면 사용 횟수(장면 수)
    use = {}
    for s in scenes:
        for c in set(c[1] for c in s["cuts"]):
            use.setdefault(c, []).append(s["id"])
    maxuse = max(len(v) for v in use.values())
    multi = {k: v for k, v in use.items() if len(v) > 1}
    # 시간 빈틈·겹침
    gaps = [(a["id"], b["id"]) for a, b in zip(scenes, scenes[1:]) if a["end"] != b["start"]]
    return dict(total=total, windows=windows, maxrun=maxrun, moving=mv, use=use, maxuse=maxuse, multi=multi,
                gaps=gaps, ncuts=len(cs), mats=mats)

if __name__ == "__main__":
    order, scenes, sh_n = load()
    r = checks(scenes)
    print("총 길이", r["total"], "초 / 컷", r["ncuts"], "/ 새 완성 화면", sh_n)
    for w in r["windows"]: print("구간 %d-%d: 컷 %d (기준 %d-%d) %s 재료바뀜 %d" % (w[0], w[1], w[2], w[3], w[4], "맞음" if w[5] else "어김", w[6]))
    print("재료 연속 최대", r["maxrun"])
    print("움직이는 장면", len(r["moving"]), "/", len(scenes), "= %.1f%%" % (100 * len(r["moving"]) / len(scenes)))
    print("완성 화면 최대 사용", r["maxuse"], r["multi"])
    print("빈틈", r["gaps"], "시작", scenes[0]["start"])
    print(" ".join(s["id"][4:] + ":" + s["main"] for s in scenes))
