from __future__ import annotations
from math import inf, isinf

def finite_frontier(plans, budgets):
    """A*(G)=min{a_gamma: g_gamma<=G}; inf when no plan is reachable."""
    out=[]
    for G in budgets:
        vals=[a for g,a in plans if g<=G]
        out.append(min(vals) if vals else inf)
    return out

def finite_frontier_audit():
    cases={}
    # canonical structural jumps
    b=list(range(7)); p=[(0,100.0),(2,20.0),(5,1.0)]
    v=finite_frontier(p,b)
    cases["canonical"]={"passed":v==[100,100,20,20,20,1,1],"values":v}

    # duplicate generation cost: only lower residual cost survives envelope
    p=[(0,50.0),(2,30.0),(2,7.0),(4,9.0)]
    v=finite_frontier(p,[0,1,2,3,4])
    cases["duplicate_cost"]={"passed":v==[50,50,7,7,7],"values":v}

    # dominated later configuration must not create an upward jump
    p=[(0,10.0),(1,3.0),(2,8.0)]
    v=finite_frontier(p,[0,1,2,3])
    cases["dominated_plan"]={"passed":v==[10,3,3,3],"values":v}

    # feasibility boundary: no finite resolving plan until G=3
    p=[(0,inf),(3,5.0)]
    v=finite_frontier(p,[0,1,2,3,4])
    cases["feasibility_transition"]={"passed":all(isinf(x) for x in v[:3]) and v[3:]==[5,5],"values":["inf" if isinf(x) else x for x in v]}

    # zero residual acquisition cost is a boundary, not finite-log leverage
    p=[(0,8.0),(2,0.0)]
    v=finite_frontier(p,[0,1,2,3])
    cases["zero_boundary"]={"passed":v==[8,8,0,0],"values":v}

    # arbitrary plan order cannot change envelope
    p=[(5,1.0),(0,100.0),(2,20.0)]
    v=finite_frontier(p,b)
    cases["order_invariance"]={"passed":v==[100,100,20,20,20,1,1],"values":v}

    # theorem invariants on all finite-valued cases
    for name,c in cases.items():
        vals=c["values"]
        numeric=[inf if x=="inf" else x for x in vals]
        c["nonincreasing"]=all(numeric[i+1]<=numeric[i] for i in range(len(numeric)-1))
        c["passed"]=bool(c["passed"] and c["nonincreasing"])
    return cases

def all_finite_frontier_checks_pass():
    return all(x["passed"] for x in finite_frontier_audit().values())
