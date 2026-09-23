from math import inf
from rfs.frontier import finite_frontier, finite_frontier_audit, all_finite_frontier_checks_pass

def test_finite_frontier_definition():
    assert finite_frontier([(0,100.0),(2,20.0),(5,1.0)], range(7)) == [100,100,20,20,20,1,1]

def test_no_reachable_plan_is_infinite():
    assert finite_frontier([(2,1.0)], [0,1]) == [inf,inf]

def test_frontier_adversarial_cases():
    cases=finite_frontier_audit()
    assert len(cases)==6
    assert all_finite_frontier_checks_pass()
    assert all(c["nonincreasing"] for c in cases.values())
