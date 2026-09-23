# Resolution-Frontier Sort (RFS)

**Research status:** experimental / candidate new model.

RFS reframes sorting as **eliminating unresolved ordering information at minimum resource cost**, not merely rearranging n objects.

## Research target

Classical comparison sorting has an Omega(n log n) lower bound for unrestricted arbitrary keys. RFS does not claim to beat that bound universally.

The candidate model is:

> Given multiple information-producing operations with heterogeneous resource costs (time, energy, writes, data movement, exact-comparison cost, oracle fee, reliability), choose operations adaptively so that the compatible set of total orders collapses to one at minimum aggregate cost.

Let Omega be the set of compatible permutations. Define unresolved ordering information as H_R = log2 |Omega|. For an action e with scalarized resource cost C_lambda(e), use the experimental score Gamma(e) = expected reduction in H_R divided by C_lambda(e).

## What is already known

This repository does **not** claim novelty for sorting under partial information, entropy/linear-extension lower bounds, adaptive ranking, noisy active ranking, non-uniform comparison costs, or learned/prediction-assisted sorting.

## Candidate gap

The narrow candidate gap is **resource-relative exact sorting under heterogeneous information-production costs**, with vector-valued physical resources and exact fallback.

## Included

- RFS prototype
- sound certificate partitioning
- exact fallback
- merge sort, quicksort, indirect sort and Python Timsort baselines
- property/correctness tests
- timing benchmarks
- resource-profile experiments
- GitHub Actions artifact generation

## Where RFS may matter

RFS is aimed at workloads where information and movement costs are heterogeneous: large database rows, persistent memory, distributed records, scientific objects with costly exact keys, sensor-derived ranking, and CPU/GPU/storage pipelines.

It is not intended to beat optimized library sorting on ordinary small in-memory scalar arrays.

## Reproduce

    python -m pip install -e .
    pytest -q
    python experiments/run_benchmarks.py

Artifacts are written to `artifacts/` and uploaded by GitHub Actions as `rfs-artifacts`.
