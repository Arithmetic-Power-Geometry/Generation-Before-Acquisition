# Generation Before Acquisition

**Decision-Relative Capability Transitions in Costly Information Systems**

This repository is the reproducible computational companion to the theory of **generation before acquisition**. The central distinction is between spending resources to acquire evidence with capabilities that already exist and spending resources to generate new measurement capability that changes which experiments are reachable at all.

For a decision problem with worlds (W), decision map (D), and generation budget (G), the framework studies

[
G \longrightarrow \mathcal C_G \longrightarrow K_D(G) \longrightarrow A_D^\star(G),
]

where (mathcal C_G) is the reachable experiment family, (K_D(G)) is the decision kernel of decision-incompatible worlds that remain observationally indistinguishable, and (A_D^\star(G)) is residual exact acquisition cost.

## Main validated structures

- finite deterministic kernel characterization;
- null, intensive, extensive, regressive, and incomparable capability transitions;
- persistence monotonicity and an explicit nonpersistent counterexample;
- separate exact batch and adaptive acquisition solvers;
- finite discrete lower-envelope capability frontiers;
- bounded-variation leverage decomposition with smooth, jump, singular-continuous, and boundary cases.

The exact finite implementation is deliberately audit-oriented rather than scale-oriented.

## Reproduce

```bash
python -m pip install -e .
pytest -q
python experiments/run_benchmarks.py
python experiments/assumption_audit.py
python experiments/frontier_theorem_audit.py
python experiments/decomposition_audit.py
```

GitHub Actions independently run the validation, assumption audit, finite-frontier audit, and leverage-decomposition audit and upload their result artifacts.

## Scientific boundary

The work does not claim novelty for costly information acquisition, Test Cover, optimal decision trees, sensor placement, value of information, or Lebesgue--Stieltjes decomposition individually. The contribution being tested is their decision-relative outer structure: **generated reachable experiment closure + decision-kernel evolution + residual acquisition cost/frontier**.

See `CLAIM_LEDGER.md`, `MANUSCRIPT_BLUEPRINT.md`, and `RESULTS_MANIFEST.md` for the frozen claim boundary and reproducibility provenance.
