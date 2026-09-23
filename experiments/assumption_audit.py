from __future__ import annotations
import csv, json
from pathlib import Path
from rfs.audit import (
    exhaustive_kernel_characterization,
    persistence_audit,
    nonpersistent_counterexample,
    finite_plan_step_frontier,
)

def main():
    out=Path("artifacts"); out.mkdir(exist_ok=True)
    checked,failures=exhaustive_kernel_characterization()
    pcosts,pmono=persistence_audit()
    ncosts,nfails=nonpersistent_counterexample()
    budgets,steps,step_ok=finite_plan_step_frontier()
    summary={
      "exhaustive_kernel_characterization":{"systems_checked":checked,"failures":len(failures),"passed":not failures},
      "persistent_monotonicity":{"costs":pcosts,"passed":pmono},
      "nonpersistent_counterexample":{"costs":ncosts,"monotonicity_fails":nfails},
      "finite_plan_step_frontier":{"budgets":budgets,"acquisition_costs":steps,"passed":step_ok},
    }
    with (out/"assumption_audit.json").open("w") as f: json.dump(summary,f,indent=2)
    with (out/"step_frontier.csv").open("w",newline="") as f:
        w=csv.writer(f); w.writerow(["generation_budget","acquisition_cost"]); w.writerows(zip(budgets,steps))
    print(json.dumps(summary,indent=2))
    assert not failures and pmono and nfails and step_ok

if __name__=="__main__": main()
