from __future__ import annotations
from itertools import product
from math import isfinite
from .model import Experiment, CapabilityStage, DecisionProblem, decision_kernel, minimum_acquisition_cost

def exhaustive_kernel_characterization():
    worlds=("w0","w1","w2"); decisions={"w0":0,"w1":1,"w2":1}
    universe=[Experiment("e"+"".join(map(str,bits)),1.0,dict(zip(worlds,bits))) for bits in product((0,1),repeat=3)]
    checked=0; failures=[]
    for mask in range(1<<len(universe)):
        exps=tuple(e for i,e in enumerate(universe) if mask&(1<<i))
        p=DecisionProblem(worlds,decisions,(CapabilityStage(0.0,exps),))
        if (len(decision_kernel(p,0.0))==0) != isfinite(minimum_acquisition_cost(p,0.0)):
            failures.append(mask)
        checked+=1
    return checked, failures

def persistence_audit():
    worlds=("a","b","c"); decisions={"a":0,"b":1,"c":1}
    e1=Experiment("ab",4.0,{"a":0,"b":1,"c":1}); e2=Experiment("cheap_ab",1.0,{"a":0,"b":1,"c":1})
    p=DecisionProblem(worlds,decisions,(CapabilityStage(0.0,(e1,)),CapabilityStage(1.0,(e1,e2))))
    costs=[minimum_acquisition_cost(p,g) for g in (0.0,1.0)]
    return costs,costs[1]<=costs[0]

def nonpersistent_counterexample():
    worlds=("a","b"); decisions={"a":0,"b":1}
    cheap=Experiment("cheap",1.0,{"a":0,"b":1}); costly=Experiment("costly",10.0,{"a":0,"b":1})
    p=DecisionProblem(worlds,decisions,(CapabilityStage(0.0,(cheap,)),CapabilityStage(1.0,(costly,))))
    costs=[minimum_acquisition_cost(p,g) for g in (0.0,1.0)]
    return costs,costs[1]>costs[0]

def finite_plan_step_frontier():
    worlds=("a","b"); decisions={"a":0,"b":1}
    e100=Experiment("r100",100.0,{"a":0,"b":1}); e20=Experiment("r20",20.0,{"a":0,"b":1}); e1=Experiment("r1",1.0,{"a":0,"b":1})
    p=DecisionProblem(worlds,decisions,(
        CapabilityStage(0.0,(e100,)),CapabilityStage(2.0,(e100,e20)),CapabilityStage(5.0,(e100,e20,e1))))
    budgets=list(range(7)); values=[minimum_acquisition_cost(p,float(g)) for g in budgets]
    return budgets,values,values==[100,100,20,20,20,1,1]
