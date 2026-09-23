from __future__ import annotations
import json
from pathlib import Path
from rfs.decomposition import decomposition_audit

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    cases,boundaries=decomposition_audit()
    result={
      "identity":"log L_D(G)=integral lambda dG + J(G) + S(G)",
      "domain":"0 < A_D^*(G) < infinity, with u=-log A_D^* monotone/BV on the interval",
      "cases":cases,
      "boundaries":boundaries,
      "all_passed":all(c["passed"] for c in cases.values()),
      "warning":"A smooth-plus-jump dichotomy is incomplete: singular-continuous leverage can be nonzero even when the classical derivative is zero almost everywhere and there are no jumps."
    }
    with (out/"leverage_decomposition.json").open("w") as f: json.dump(result,f,indent=2)
    print(json.dumps(result,indent=2))
    assert result["all_passed"]

if __name__=="__main__": main()
