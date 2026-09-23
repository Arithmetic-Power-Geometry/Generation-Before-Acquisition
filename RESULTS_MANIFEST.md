# Results Manifest

## Validated computational base

- Validated commit: `c4ca4b037e8f729e4579844cd35b06fb3b12fffc`
- Validation date: 2026-09-23
- Status: all four repository workflows completed successfully on this commit.

## Workflow and artifact provenance

| Workflow | Run ID | Artifact | Artifact ID | SHA-256 digest |
|---|---:|---|---:|---|
| validate-closure-cost | 35883754474 | closure-cost-artifacts | 10762515410 | a21b328c059f7d09d2eec96fb8e817f6d5d0d186d4b7eada82422f41d9374c7e |
| exhaustive-assumption-audit | 35883754449 | assumption-audit-artifacts | 10761349698 | 106768cae8cc96961f4087073ba33f2dd8285a15be30babaff0946c44b03c7c3 |
| finite-frontier-theorem | 35883754708 | finite-frontier-theorem-artifacts | 10761541935 | e641bae902899b7d4a1252deda10cb95ac0de1afe72df05e1aa462022e7bae9b |
| leverage-decomposition | 35883754410 | leverage-decomposition-artifact | 10761174817 | 99d92634db9f738e13ed03b3b891eb03e100b7bb4950156489773d8c03e4f011 |

## Manuscript-facing result map

1. **Finite deterministic kernel characterization audit.** The exhaustive
   assumption audit checks all 256 subsets of the eight binary deterministic
   experiments on the three-world audit universe. This is computational
   validation, not a mathematical proof.

2. **Transition behavior.** Tests cover null, intensive, extensive, and
   nonpersistent regressive transitions. Persistence is checked using semantic
   experiment signatures rather than object hashability.

3. **Batch versus adaptive acquisition.** The code distinguishes exact
   nonadaptive subset cost from exact memoized worst-case adaptive
   decision-tree cost for small finite deterministic instances. A unit-tested
   four-world witness has batch optimum 3 and adaptive optimum 2. This is an
   explicit separating example, not a general performance theorem.

4. **Finite discrete frontier.** The finite-frontier workflow audits the
   step-frontier representation and adversarial/boundary cases under the
   finite-plan, fixed-residual-cost assumptions.

5. **Leverage decomposition.** The decomposition workflow audits smooth,
   jump, singular-continuous, and boundary guardrails. Lebesgue-Stieltjes
   decomposition is established mathematics used as structural machinery and
   is not claimed as novel mathematics.

## Claim discipline

Workflow success and finite exhaustive audits are reproducible computational
evidence; they do not establish universal novelty and do not replace
mathematical proof. The candidate contribution remains the joint
decision-relative framework linking generated reachable experiment closure,
decision-kernel evolution, and residual acquisition cost/frontiers.

Manuscript computational statements should be sourced from artifacts tied to
the validated commit above rather than manually retyped results.
