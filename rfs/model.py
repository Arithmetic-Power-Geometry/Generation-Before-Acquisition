from __future__ import annotations

from dataclasses import dataclass
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
    unresolved = []
    for a, b in problem.critical_pairs():
        if all(not e.separates(a, b) for e in exps):
            unresolved.append((a, b))
    return tuple(unresolved)


def minimum_acquisition_cost(problem: DecisionProblem, generation_budget: float) -> float:
    """Exact exhaustive solver for small deterministic instances.

    A subset resolves the decision iff it separates every decision-critical pair.
    The routine is deliberately exponential: its purpose is theorem validation
    and auditability, not scalable optimization.
    """
    exps = problem.experiments_at(generation_budget)
    critical = problem.critical_pairs()
    if not critical:
        return 0.0
    if any(all(not e.separates(a, b) for e in exps) for a, b in critical):
        return inf

    best = inf
    m = len(exps)
    for mask in range(1 << m):
        cost = 0.0
        chosen = []
        prune = False
        for j, e in enumerate(exps):
            if mask & (1 << j):
                cost += e.acquisition_cost
                if cost >= best:
                    prune = True
                    break
                chosen.append(e)
        if prune:
            continue
        if all(any(e.separates(a, b) for e in chosen) for a, b in critical):
            best = cost
    return best


def classify_transition(problem: DecisionProblem, g1: float, g2: float) -> str:
    k1 = set(decision_kernel(problem, g1))
    k2 = set(decision_kernel(problem, g2))
    a1 = minimum_acquisition_cost(problem, g1)
    a2 = minimum_acquisition_cost(problem, g2)
    if k1 != k2:
        return "extensive"
    if a2 < a1:
        return "intensive"
    return "null"
