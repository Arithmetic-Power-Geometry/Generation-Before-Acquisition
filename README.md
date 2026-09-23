# Generation Before Acquisition

**Decision-Relative Capability Transitions in Costly Information Systems**

This repository contains the computational development and exact finite validation of generation before acquisition: the distinction between acquiring evidence with capabilities that already exist and generating new measurement capability that changes which experiments are reachable.

The computational framework follows:

`G -> C_G -> K_D(G) -> A_D^*(G)`

Here `C_G` is the reachable experiment family, `K_D(G)` is the decision kernel of decision-incompatible worlds that remain observationally indistinguishable, and `A_D^*(G)` is residual exact acquisition cost.

## Validated structures

- finite deterministic kernel characterization;
- null, intensive, extensive, regressive, and incomparable capability transitions;
- persistence monotonicity and an explicit nonpersistent counterexample;
- separate exact batch and adaptive acquisition solvers;
- finite discrete lower-envelope capability frontiers;
- bounded-variation leverage decomposition with smooth, jump, singular-continuous, and boundary cases.

The implementation is deliberately audit-oriented rather than scale-oriented.

## Reproduction

The `experiments/` directory contains the benchmark, assumption-audit, frontier-audit, and decomposition-audit programs. The `tests/` directory contains exact finite validation tests. GitHub Actions run the validation and audit programs and preserve result artifacts.

## Scientific scope

Costly information acquisition, Blackwell experiments, Test Cover, optimal decision trees, sensor placement, value of information, and Lebesgue--Stieltjes decomposition are neighboring foundations. This repository studies the decision-relative outer structure formed by generated reachable experiment closure, decision-kernel evolution, and residual acquisition cost/frontiers.

See `CLAIM_LEDGER.md`, `RESULTS_MANIFEST.md`, and `docs/` for scientific scope, validation provenance, and interpretation.

## Citation

Akhtar, M. A. K. (2026). *Generation Before Acquisition: Decision-Relative Capability Transitions in Costly Information Systems* (Version V1). Zenodo. DOI: 10.5281/zenodo.22921931

Machine-readable citation metadata are provided in `CITATION.cff`.
