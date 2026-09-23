from __future__ import annotations
import csv, json
from itertools import product
from math import isfinite, inf
from pathlib import Path
from rfs import Experiment, CapabilityStage, DecisionProblem, decision_kernel, minimum_acquisition_cost

def exhaustive_kernel_characterization():
    worlds=("w0","w1","w2")
    decisions={"w0":0,"w1":1,"w2":1}
    checked=0; failures=[]
    # all binary deterministic experiments on three worlds: 2^3 = 8
    universe=[]
    for bits in product((0,1), repeat=3):
        universe.append(Experiment("e"+"".join(map(str,bits)),1.0,dict(zip(worlds,bits))))
    # all experiment subsets: 2^8 = 256
    for mask in range(1<<len(universe)):
        exps=tuple(e for i,e in enumerate(universe) if mask&(1<<i))
        p=DecisionProblem(worlds,decisions,(CapabilityStage(0.0,exps),))
        k_empty=len(decision_kernel(p,0.0))==0
        finite=isfinite(minimum_acquisition_cost(p,0.0))
        checked+=1
        if k_empty != finite:
            failures.append(mask)
    return checked, failures

def persistence_audit():
    worlds=("a","b","c")
    decisions={"a":0,"b":1,"c":1}
    e1=Experiment("ab",4.0,{"a":0,"b":1,"c":1})
    e2=Experiment("cheap_ab",1.0,{"a":0,"b":1,"c":1})
    p=DecisionProblem(worlds,decisions,(
        CapabilityStage(0.0,(e1,)),
        CapabilityStage(1.0,(e1,e2)),
    ))
    costs=[minimum_acquisition_cost(p,g) for g in (0.0,1.0)]
    return costs, costs[1] <= costs[0]

def nonpersistent_counterexample():
    worlds=("a","b")
    decisions={"a":0,"b":1}
    cheap=Experiment("cheap",1.0,{"a":0,"b":1})
    costly=Experiment("costly",10.0,{"a":0,"b":1})
    p=DecisionProblem(worlds,decisions,(
        CapabilityStage(0.0,(cheap,)),
        CapabilityStage(1.0,(costly,)),
    ))
    costs=[minimum_acquisition_cost(p,g) for g in (0.0,1.0)]
    return costs, costs[1] > costs[0]

def finite_plan_step_frontier():
    worlds=("a","b")
    decisions={"a":0,"b":1}
    e100=Experiment("r100",100.0,{"a":0,"b":1})
    e20=Experiment("r20",20.0,{"a":0,"b":1})
    e1=Experiment("r1",1.0,{"a":0,"b":1})
    p=DecisionProblem(worlds,decisions,(
        CapabilityStage(0.0,(e100,)),
        CapabilityStage(2.0,(e100,e20)),
        CapabilityStage(5.0,(e100,e20,e1)),
    ))
    budgets=[0,1,2,3,4,5,6]
    values=[minimum_acquisition_cost(p,float(g)) for g in budgets]
    expected=[100,100,20,20,20,1,1]
    return budgets,values,values==expected

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
        w=csv.writer(f); w.writerow(["generation_budget","acquisition_cost"])
        w.writerows(zip(budgets,steps))
    print(json.dumps(summary,indent=2))
    assert not failures and pmono and nfails and step_ok

if __name__=="__main__": main()
