from __future__ import annotations
import csv,json
from pathlib import Path
from rfs.frontier import finite_frontier_audit

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    cases=finite_frontier_audit()
    summary={"theorem":"A_D^*(G)=min_{gamma:g_gamma<=G} a_gamma","cases":cases,
             "all_passed":all(c["passed"] for c in cases.values()),
             "interpretation":"Finite discrete capability frontiers are lower envelopes of finitely many plan costs; changes occur only at generation-cost thresholds. Infinite and zero boundaries are excluded from finite-log leverage."}
    with (out/"finite_frontier_theorem.json").open("w") as f: json.dump(summary,f,indent=2)
    with (out/"finite_frontier_cases.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["case","passed","nonincreasing","values"])
        for name,c in cases.items(): w.writerow([name,c["passed"],c["nonincreasing"],"|".join(map(str,c["values"]))])
    print(json.dumps(summary,indent=2))
    assert summary["all_passed"]

if __name__=="__main__": main()
