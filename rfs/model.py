from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from math import inf
from typing import Hashable, Mapping, Tuple

World = Hashable
Outcome = Hashable


@dataclass(frozen=True)
class Experiment:
    name: str
    acquisition_cost: float
    outcomes: Mapping[World, Outcome]

    def separates(self, a: World, b: World) -> bool:
        return self.outcomes[a] != self.outcomes[b]


@dataclass(frozen=True)
class CapabilityStage:
    generation_budget: float
    experiments: Tuple[Experiment, ...]


@dataclass(frozen=True)
class DecisionProblem:
    worlds: Tuple[World, ...]
    decisions: Mapping[World, Hashable]
    stages: Tuple[CapabilityStage, ...]

    def critical_pairs(self) -> Tuple[Tuple[World, World], ...]:
        out = []
        for i, a in enumerate(self.worlds):
            for b in self.worlds[i + 1:]:
                if self.decisions[a] != self.decisions[b]:
                    out.append((a, b))
        return tuple(out)

    def experiments_at(self, generation_budget: float) -> Tuple[Experiment, ...]:
        candidates = [s for s in self.stages if s.generation_budget <= generation_budget]
        if not candidates:
            return tuple()
        stage = max(candidates, key=lambda s: s.generation_budget)
        return stage.experiments


def decision_kernel(problem: DecisionProblem, generation_budget: float):
    exps = problem.experiments_at(generation_budget)
    return tuple(
        (a, b) for a, b in problem.critical_pairs()
        if all(not e.separates(a, b) for e in exps)
    )


def minimum_batch_acquisition_cost(problem: DecisionProblem, generation_budget: float) -> float:
    """Exact minimum cost of one fixed (nonadaptive) experiment subset."""
    exps = problem.experiments_at(generation_budget)
    critical = problem.critical_pairs()
    if not critical:
        return 0.0
    if decision_kernel(problem, generation_budget):
        return inf

    best = inf
    m = len(exps)
    for mask in range(1 << m):
        cost = 0.0
        chosen = []
        for j, e in enumerate(exps):
            if mask & (1 << j):
                cost += e.acquisition_cost
                if cost >= best:
                    break
                chosen.append(e)
        else:
            if all(any(e.separates(a, b) for e in chosen) for a, b in critical):
                best = cost
    return best


def minimum_adaptive_acquisition_cost(problem: DecisionProblem, generation_budget: float) -> float:
    """Exact minimum worst-case cost of an adaptive deterministic decision tree.

    A state is the subset of worlds still compatible with observations. The
    policy stops when all remaining worlds have the same decision. An
    experiment that does not split the current state is never useful.
    """
    exps = problem.experiments_at(generation_budget)
    if not problem.worlds:
        return 0.0

    @lru_cache(maxsize=None)
    def value(state: Tuple[World, ...]) -> float:
        if len({problem.decisions[w] for w in state}) <= 1:
            return 0.0

        best = inf
        for e in exps:
            cells = {}
            for w in state:
                cells.setdefault(e.outcomes[w], []).append(w)
            if len(cells) <= 1:
                continue
            branch_values = [value(tuple(cell)) for cell in cells.values()]
            worst = max(branch_values)
            if worst != inf:
                best = min(best, e.acquisition_cost + worst)
        return best

    return value(tuple(problem.worlds))


# Backward-compatible name: historically this repository used the batch solver.
minimum_acquisition_cost = minimum_batch_acquisition_cost


def is_persistent(problem: DecisionProblem) -> bool:
    stages = sorted(problem.stages, key=lambda s: s.generation_budget)
    for left, right in zip(stages, stages[1:]):
        if not set(left.experiments).issubset(set(right.experiments)):
            return False
    return True


def classify_transition(problem: DecisionProblem, g1: float, g2: float, *, adaptive: bool = False) -> str:
    k1 = set(decision_kernel(problem, g1))
    k2 = set(decision_kernel(problem, g2))
    cost = minimum_adaptive_acquisition_cost if adaptive else minimum_batch_acquisition_cost
    a1, a2 = cost(problem, g1), cost(problem, g2)

    if k2 < k1:
        return "extensive"
    if k1 == k2:
        if a2 < a1:
            return "intensive"
        if a2 == a1:
            return "null"
        return "regressive"
    if k1 < k2:
        return "regressive"
    return "incomparable"
