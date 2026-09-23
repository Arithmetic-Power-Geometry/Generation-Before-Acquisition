from experiments.assumption_audit import (
    exhaustive_kernel_characterization,
    persistence_audit,
    nonpersistent_counterexample,
    finite_plan_step_frontier,
)

def test_exhaustive_kernel_characterization():
    checked, failures = exhaustive_kernel_characterization()
    assert checked == 256
    assert failures == []

def test_persistence_monotonicity():
    costs, ok = persistence_audit()
    assert ok
    assert costs == [4.0, 1.0]

def test_nonpersistent_counterexample():
    costs, fails = nonpersistent_counterexample()
    assert fails
    assert costs == [1.0, 10.0]

def test_finite_plan_step_frontier():
    budgets, values, ok = finite_plan_step_frontier()
    assert ok
    assert values == [100.0,100.0,20.0,20.0,20.0,1.0,1.0]
