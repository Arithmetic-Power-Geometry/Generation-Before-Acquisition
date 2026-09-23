from math import exp, log
import pytest
from rfs.decomposition import leverage_from_components, jump_log_contribution, decomposition_audit

def test_smooth_component():
    assert leverage_from_components(2.0) == exp(2.0)

def test_jump_telescopes():
    j=jump_log_contribution(100.0,20.0)+jump_log_contribution(20.0,1.0)
    assert abs(j-log(100.0))<1e-12
    assert abs(leverage_from_components(0,j)-100.0)<1e-12

def test_singular_continuous_is_not_lost():
    cases,_=decomposition_audit()
    c=cases["singular_continuous"]
    assert c["ac"]==0 and c["jump"]==0 and c["singular"]==1
    assert c["computed"]>1

def test_invalid_log_boundaries():
    with pytest.raises(ValueError): jump_log_contribution(float("inf"),1.0)
    with pytest.raises(ValueError): jump_log_contribution(1.0,0.0)
    with pytest.raises(ValueError): jump_log_contribution(1.0,2.0)

def test_all_decomposition_cases():
    cases,boundaries=decomposition_audit()
    assert all(c["passed"] for c in cases.values())
    assert len(boundaries)==2
