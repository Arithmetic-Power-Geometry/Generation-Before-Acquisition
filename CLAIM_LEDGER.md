# Scientific Scope and Claim Ledger

## Core model

For worlds W and decision map D, generation budget G determines a reachable experiment family C_G. The decision kernel is

K_D(G) = {(w,w'): D(w) != D(w') and every e in C_G gives the same observation on w,w'}.

A_D^*(G) denotes the minimum residual acquisition/testing cost required to determine D using experiments in C_G, with batch and adaptive acquisition treated separately.

The central chain is

G -> C_G -> K_D(G) -> A_D^*(G).

## Structural contribution

The framework combines capability-generation expenditure, reachable experiment families, decision-relative indistinguishability, and residual optimal testing cost. A fixed-family acquisition problem is an inner optimization problem; generation changes the experiment family on which that inner problem is defined.

This produces the following transition structure:

- Null: kernel and residual cost are unchanged.
- Intensive: kernel is unchanged while residual acquisition cost falls.
- Extensive: the decision kernel strictly shrinks.
- Feasibility: a nonempty decision kernel becomes empty, moving exact residual acquisition cost from infinity to finite under the finite deterministic assumptions.
- Regressive or incomparable behavior can occur without persistence.

## Established mathematical structures

1. **Finite deterministic kernel characterization.** Under the stated finite-separation assumptions, K_D(G) is empty if and only if finite exact resolution is possible.

2. **Persistence monotonicity.** If C_G1 is a subset of C_G2 for G1 <= G2, then A_D^*(G2) <= A_D^*(G1).

3. **Nonpersistence counterexample.** Without persistence, residual acquisition cost can increase.

4. **Finite discrete frontier.** For finitely many generated configurations gamma with generation thresholds g_gamma and residual costs a_gamma,

   A_D^*(G) = min { a_gamma : g_gamma <= G }.

   The resulting frontier is a nonincreasing step function, with infinity before any resolving configuration when applicable.

5. **Bounded-variation leverage decomposition.** On intervals where 0 < A_D^*(G) < infinity and u(G) = -log A_D^*(G) is monotone/BV, its Lebesgue--Stieltjes measure separates into absolutely continuous, jump, and singular-continuous parts:

   log L_D(G) = integral lambda(g) dg + J(G) + S(G).

   Infinity-to-finite and finite-to-zero transitions are separate boundary regimes.

## Relation to neighboring foundations

Neighboring foundations include costly information acquisition, costly Blackwell experiments, information-structure choice under cost, Test Cover / Minimum Test Collection, minimum-cost decision trees, hypothesis identification, decision-function evaluation, sensor placement, monitoring design, value-of-information optimization, installation/operation cost models, and Lebesgue--Stieltjes decomposition.

The repository's organizing object is the joint decision-relative chain linking generated reachable experiment closure, decision-kernel evolution, and residual acquisition cost/frontiers.

## Computational evidence

The repository contains exact finite deterministic validation; exhaustive evaluation of all 256 subsets of eight binary experiments on the three-world audit universe; persistence and nonpersistence audits; finite-frontier adversarial and boundary cases; and smooth, jump, mixed, and singular-continuous leverage-decomposition audits.

Computational enumeration validates the implementation and tested assumptions. Mathematical results are established separately from the computational checks.
