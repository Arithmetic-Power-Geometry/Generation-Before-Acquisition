# Results Manifest

## Validated computational base

- Validated commit: `eab0fff418f4072f196c9c3e0148a52f79692948`
- Validation date: 2026-09-23
- Status: all four repository workflows completed successfully on this commit after the repository was aligned to **Generation Before Acquisition**.

## Workflow and artifact provenance

| Workflow | Run ID | Artifact | Artifact ID | SHA-256 digest |
|---|---:|---|---:|---|
| validate-closure-cost | 35886143111 | closure-cost-artifacts | 10761624768 | 3d9ef092c00396d3f78304fdb8676da060fcbcd92c9656db1c5eee6c0d924a36 |
| exhaustive-assumption-audit | 35886143190 | assumption-audit-artifacts | 10763040648 | 989f6f1d03d1ca243ddb86107a0c84edf05ce284d005fae2ac1b04e881218e50 |
| finite-frontier-theorem | 35886143081 | finite-frontier-theorem-artifacts | 10762588764 | fb7e5d7e36a0991e8f602f3e66f097ae066a95a3f6e2bd841d50acd70df50d98 |
| leverage-decomposition | 35886143088 | leverage-decomposition-artifact | 10761893792 | 3f0424bc7287a2dc8465b7f513abab329faf8b073711e44b28d85803894449e2 |

## Manuscript consistency audit

The fresh workflow artifacts were compared against the submission manuscript
`Generation Before Acquisition: Decision-Relative Capability Transitions in Costly Information Systems`.

Exact matches include:

- null/intensive frontier: residual costs 100, 100, 20, 2 with kernel size 0;
- extensive case: kernel sizes 4, 4, 0 and residual costs infinity, infinity, 5;
- exhaustive kernel audit: 256 experiment-family subsets, 0 failures;
- persistent monotonicity audit: 4 -> 1;
- nonpersistent counterexample: 1 -> 10;
- finite step frontier: 100, 100, 20, 20, 20, 1, 1;
- all six finite-frontier adversarial/boundary cases;
- leverage decomposition values for smooth, pure-jump, mixed, and singular-continuous cases.

The batch/adaptive witness (batch optimum 3, adaptive optimum 2) is checked by
the repository unit-test suite executed by the validation workflow.

## Claim discipline

Workflow success and finite exhaustive audits are reproducible computational
evidence; they do not establish universal novelty and do not replace
mathematical proof. The contribution remains the joint decision-relative
framework linking generated reachable experiment closure, decision-kernel
evolution, and residual acquisition cost/frontiers.

Manuscript computational statements should be sourced from artifacts tied to
the validated commit above rather than manually retyped results.
