# Scientific Claim Ledger

This file freezes the claim boundary for the closure/cost theory before manuscript drafting.

## Core model

For worlds W and decision map D, generation budget G determines a reachable experiment family C_G. Define the decision kernel

K_D(G) = {(w,w'): D(w) != D(w') and every e in C_G gives the same observation on w,w'}.

Let A_D^*(G) be the minimum residual acquisition/testing cost required to determine D using experiments in C_G (with the acquisition model stated explicitly: batch or adaptive).

The central chain is

G -> C_G -> K_D(G) -> A_D^*(G).

## Candidate contribution to defend

The candidate contribution is NOT costly information, sensor installation cost, Test Cover, or optimal decision trees individually.

The candidate is the joint decision-relative framework in which capability-generation expenditure changes the reachable experiment family, the induced decision kernel records which decision-incompatible worlds remain observationally inseparable, and the residual optimal testing cost is evaluated conditional on that generated closure.

This supports a distinction between:

- Null transition: kernel and residual cost unchanged.
- Intensive transition: kernel unchanged while residual acquisition cost falls.
- Extensive transition: the decision kernel strictly shrinks.
- Feasibility transition: a nonempty decision kernel becomes empty, moving exact residual acquisition cost from infinity to finite under the finite deterministic assumptions.

## Established mathematical results

1. Finite deterministic kernel characterization, under the stated finite-separation assumptions:
   K_D(G) is empty iff finite exact resolution is possible.

2. Persistence monotonicity:
   if C_G1 is a subset of C_G2 for G1 <= G2, then A_D^*(G2) <= A_D^*(G1).

3. Persistence is necessary for that monotonicity statement in this model; the repository contains an explicit nonpersistent counterexample.

4. Finite discrete frontier:
   for finitely many generated configurations gamma with generation thresholds g_gamma and residual costs a_gamma,

   A_D^*(G) = min { a_gamma : g_gamma <= G }.

   Hence the finite discrete frontier is a nonincreasing step function (with infinity before any resolving configuration, when applicable).

5. On intervals where 0 < A_D^*(G) < infinity and u(G)=-log A_D^*(G) is monotone/BV, its Lebesgue-Stieltjes measure decomposes into absolutely continuous, jump, and singular-continuous parts:

   log L_D(G) = integral lambda(g) dg + J(G) + S(G).

   Infinity-to-finite and finite-to-zero transitions are boundary regimes and are not inserted into the finite logarithmic decomposition.

## Prior-art boundaries: do not claim novelty for these

- Costly information acquisition or costly Blackwell experiments.
- Choosing an information structure subject to cost.
- Test Cover / Minimum Test Collection.
- Minimum-cost decision trees, hypothesis identification, or decision-function evaluation for a fixed test family.
- Sensor placement, sensor-network design, or value-of-information optimization.
- The existence of separate design/installation and operation/measurement costs.
- Lebesgue-Stieltjes decomposition as mathematics.

These are neighboring literatures and should be cited as foundations/inner problems.

## Safe manuscript positioning

A fixed-family acquisition problem may be solved by existing Test Cover / ODT / DFEP machinery. The present framework places that known inner problem behind an outer capability-generation map G -> C_G and asks a different structural question:

Does additional capability merely make an already-resolvable decision cheaper to resolve, or does it remove decision-critical indistinguishabilities that made the decision unresolved before?

Novelty language must remain conditional: targeted searches did not identify the exact combined formulation above; this is not proof that no equivalent formulation exists anywhere.

## Computational evidence

The repository contains:
- exact finite deterministic validation;
- exhaustive audit of all 256 subsets of the eight binary experiments on the chosen three-world audit universe, with zero counterexamples to the tested characterization;
- persistence and nonpersistence audits;
- finite-frontier adversarial cases;
- smooth, jump, mixed, and singular-continuous leverage-decomposition audits.

Computational enumeration is validation evidence, not the mathematical proof.
