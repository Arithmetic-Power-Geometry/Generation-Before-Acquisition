# Novelty audit

## Established neighboring results

- Sorting under partial information already targets the number of compatible linear extensions.
- Active ranking already chooses pairwise queries adaptively.
- Non-uniform comparison-cost problems already exist.
- Learned/prediction-assisted sorting already exploits imperfect side information.

## What RFS does not claim

RFS does not claim novelty for entropy-guided sorting, sorting a known partial order, adaptive pairwise comparisons, scalar comparison costs alone, learned ranks, or exploiting presortedness.

## Surviving candidate gap

Each information-producing action e has a vector cost such as

    c(e) = (time, energy, writes, movement, comparisons, fee, reliability).

The goal is exact recovery of one total order while minimizing a chosen aggregate or Pareto criterion over those physical resources. The working progress variable is compatible-permutation entropy H_R = log2 |Omega|.

**Status:** candidate model. Broader theory search and formal lower/upper bounds are still required before claiming foundational novelty.
