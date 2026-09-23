from __future__ import annotations
from math import exp, log, isfinite

def leverage_from_components(ac_integral: float, jump_log: float=0.0, singular_log: float=0.0) -> float:
    """L=exp(AC + jump + singular) on a finite positive frontier."""
    if not all(isfinite(x) for x in (ac_integral,jump_log,singular_log)):
        raise ValueError("decomposition components must be finite")
    return exp(ac_integral + jump_log + singular_log)

def jump_log_contribution(left: float, right: float) -> float:
    if not (isfinite(left) and isfinite(right) and left > 0 and right > 0):
        raise ValueError("finite-log decomposition requires positive finite frontier values")
    if right > left:
        raise ValueError("frontier must be nonincreasing")
    return log(left/right)

def decomposition_audit():
    smooth={"ac":2.0,"jump":0.0,"singular":0.0,"expected":exp(2.0)}
    jump={"ac":0.0,"jump":log(100/20)+log(20/1),"singular":0.0,"expected":100.0}
    mixed={"ac":1.0,"jump":log(4.0),"singular":0.5,"expected":exp(1.5)*4.0}
    # Cantor-function prototype: derivative zero a.e., no atoms, total singular mass one.
    singular={"ac":0.0,"jump":0.0,"singular":1.0,"expected":exp(1.0)}
    cases={"smooth":smooth,"pure_jump":jump,"mixed":mixed,"singular_continuous":singular}
    for c in cases.values():
        c["computed"]=leverage_from_components(c["ac"],c["jump"],c["singular"])
        c["passed"]=abs(c["computed"]-c["expected"]) < 1e-12
    boundaries={"infinity_to_finite":"separate feasibility transition","finite_to_zero":"separate zero-cost boundary"}
    return cases,boundaries
