# Manuscript Blueprint

## Working title
Generation Before Acquisition: Decision-Relative Capability Transitions in Costly Information Systems

## One-sentence thesis
Capability investment can either reduce the cost of resolving a decision within an unchanged distinguishability structure or change the distinguishability structure itself, including transitions from exact non-resolvability to resolvability.

## 1. Introduction
Problem: classical costly-testing and information-acquisition models optimize information use/choice, while capability design can change which experiments are reachable at all.
Do not claim that two cost types are new.
Contributions should be stated only after the related-work boundary is established.

## 2. Related work and exact boundary
2.1 Test Cover / Minimum Test Collection
2.2 Optimal Decision Trees / Decision Function Evaluation
2.3 Blackwell experiments and costly information acquisition
2.4 Sensor placement, monitoring design, and value of information
2.5 Relation to generated experimental reach

Key positioning:
Existing fixed-family testing is an inner problem. The framework studies the outer capability-generation map and its decision-relative structural consequences.

## 3. Model
Define W, D, generation configurations/operations, reachable authorized closure C_G, acquisition costs, and persistence.
Define critical decision pairs and K_D(G).
Define batch and adaptive residual acquisition costs separately; do not conflate them.

## 4. Kernel characterization
Theorem 1: finite deterministic kernel characterization.
State finite-world / finite-separation assumptions.
Proof: necessity by indistinguishability; sufficiency by selecting a finite separator for every decision-incompatible pair.
Corollary: nonempty kernel implies infinite exact residual acquisition cost.

## 5. Capability transitions
Definition: null, intensive, extensive.
Proposition: persistence monotonicity.
Counterexample: without persistence residual acquisition cost can increase.
Corollary: extensive transition to empty kernel is a resolvability-class transition.

## 6. Finite discrete capability frontier
Theorem 2:
A_D^*(G)=min_{gamma:g_gamma<=G} a_gamma.
Consequences: right-continuous nonincreasing step frontier after a convention on threshold inclusion; dominated configurations disappear from the lower envelope.
Finite positive portions have classical log derivative zero almost everywhere; leverage occurs at jumps.
Handle infinity and zero separately.

## 7. General BV leverage decomposition
On a finite-positive interval set u=-log A_D^*.
Theorem 3: Lebesgue-Stieltjes decomposition
du=lambda dG + du_jump + du_sing.
Therefore
log L_D(G)=integral lambda dG + J(G)+S(G).
Explain why singular-continuous leverage prevents a false smooth-versus-jump dichotomy.
Do not claim the measure decomposition itself is new.

## 8. Exact computational audits
Table A: canonical null/intensive/extensive cases.
Table B: exhaustive 256-subset finite audit.
Table C: persistence vs nonpersistence.
Table D: finite-frontier adversarial cases.
Table E: smooth/jump/mixed/singular decomposition identities.
All numbers must come from workflow artifacts.

## 9. Interpretation
Distinguish:
- more measurements;
- cheaper measurements;
- new measurement capability;
- new decision separability.
Explain why the same added sensor/test can be intensive for one decision map and extensive for another.

## 10. Limitations
Finite deterministic characterization does not automatically extend to stochastic exact identification.
For stochastic experiments use epsilon-resolution/error criteria.
Pairwise distinguishability in infinite W need not imply a finite resolving campaign.
Adaptive and batch acquisition are distinct inner optimization problems.
Targeted literature search cannot establish universal absence of equivalent prior formulations.

## 11. Conclusion
Capability generation should be evaluated not only by how much it lowers evidence-acquisition cost, but by whether it changes the decision-relative boundary of what can be resolved.

## Artifact discipline
No manually typed experimental result enters the manuscript if a workflow artifact can supply it.
Every theorem assumption gets a matching audit/counterexample where computationally meaningful.
Repository claim ledger governs novelty wording.
