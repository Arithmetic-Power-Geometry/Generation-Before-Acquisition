# Resolution-Frontier-Sort — Closure/Cost Validation Lab

This repository began as an attempt to find a genuinely new resource-aware sorting model. The unrestricted sorting branch was rejected after lower-bound and prior-art attacks. The repository is now retained as a reproducible **validation lab** for the surviving theory-level result: separating the cost of acquiring evidence inside an existing experimental closure from the cost of generating new decision-relevant capability.

## Core objects

For a finite deterministic decision problem:

- `C_G`: capability-generation cost.
- `C_A`: evidence-acquisition cost.
- `C_G` changes the reachable experiment closure.
- `K_D(G)`: decision kernel — decision-critical world pairs not separated by any experiment reachable after generation budget `G`.
- `A_D^*(G)`: exact minimum acquisition cost after generation budget `G`.

Under the finite deterministic assumptions used by the exact solver:

`A_D^*(G) < infinity` iff `K_D(G)` is empty.

## Three validated regimes

1. **Null expansion** — the experiment set expands but neither the decision kernel nor optimal acquisition cost changes.
2. **Intensive expansion** — the decision kernel is unchanged, but optimal acquisition cost falls.
3. **Extensive expansion** — the decision kernel strictly shrinks; if the last unresolved critical pair disappears, exact resolution changes from impossible to possible.

The code intentionally uses exhaustive finite search. Its purpose is theorem validation and auditability, not large-scale optimization.

## Reproduce locally

    python -m pip install -e .
    pytest -q
    python experiments/run_benchmarks.py

Generated outputs:

- `artifacts/closure_cost_frontier.csv`
- `artifacts/closure_cost_summary.json`

GitHub Actions uploads these as `closure-cost-artifacts`.

## Scientific positioning

This repository does **not** claim novelty for comparison sorting, sorting under partial information, Test Cover, Blackwell experiment comparison, costly information acquisition, rational inattention, active sensing, or fixed/variable information-production costs.

The candidate contribution being validated is narrower: the joint use of a **generated reachable experiment closure**, a **decision kernel**, and **residual exact acquisition complexity**, together with the distinction between null, intensive, and extensive capability expansion.

The manuscript should be written from frozen workflow artifacts rather than manually entered numbers.
