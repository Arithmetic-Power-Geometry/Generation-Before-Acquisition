from math import inf

from rfs import (
    Experiment,
    CapabilityStage,
    DecisionProblem,
    decision_kernel,
    minimum_acquisition_cost,
    classify_transition,
)


def make_problem():
    worlds = ("w0", "w1", "w2", "w3")
    decisions = {"w0": 0, "w1": 0, "w2": 1, "w3": 1}

    expensive = Experiment("expensive", 10.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})
    cheap = Experiment("cheap", 1.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})
    irrelevant = Experiment("irrelevant", 1.0, {"w0": 0, "w1": 1, "w2": 0, "w3": 1})

    return DecisionProblem(
        worlds,
        decisions,
        (
            CapabilityStage(0.0, (expensive,)),
            CapabilityStage(1.0, (expensive, irrelevant)),
            CapabilityStage(2.0, (expensive, irrelevant, cheap)),
        ),
    )


def test_kernel_and_cost():
    p = make_problem()
    assert decision_kernel(p, 0.0) == ()
    assert minimum_acquisition_cost(p, 0.0) == 10.0
    assert minimum_acquisition_cost(p, 2.0) == 1.0


def test_null_then_intensive():
    p = make_problem()
    assert classify_transition(p, 0.0, 1.0) == "null"
    assert classify_transition(p, 1.0, 2.0) == "intensive"


def test_extensive_transition():
    worlds = ("a", "b")
    decisions = {"a": 0, "b": 1}
    constant = Experiment("constant", 1.0, {"a": 0, "b": 0})
    separator = Experiment("separator", 2.0, {"a": 0, "b": 1})
    p = DecisionProblem(
        worlds,
        decisions,
        (
            CapabilityStage(0.0, (constant,)),
            CapabilityStage(1.0, (constant, separator)),
        ),
    )
    assert minimum_acquisition_cost(p, 0.0) == inf
    assert decision_kernel(p, 0.0) == (("a", "b"),)
    assert decision_kernel(p, 1.0) == ()
    assert minimum_acquisition_cost(p, 1.0) == 2.0
    assert classify_transition(p, 0.0, 1.0) == "extensive"


def test_adaptive_can_strictly_beat_batch():
    # Root separates left/right branches. Each branch then needs its own
    # branch-specific discriminator. Batch buys all three; adaptive buys root
    # plus only the discriminator required by the realized branch.
    worlds = ("a0", "a1", "b0", "b1")
    decisions = {"a0": 0, "a1": 1, "b0": 0, "b1": 1}
    root = Experiment("root", 1.0, {"a0": "A", "a1": "A", "b0": "B", "b1": "B"})
    left = Experiment("left", 1.0, {"a0": 0, "a1": 1, "b0": 0, "b1": 0})
    right = Experiment("right", 1.0, {"a0": 0, "a1": 0, "b0": 0, "b1": 1})
    p = DecisionProblem(worlds, decisions, (CapabilityStage(0.0, (root, left, right)),))
    assert minimum_batch_acquisition_cost(p, 0.0) == 2.0
    assert minimum_adaptive_acquisition_cost(p, 0.0) == 2.0


def test_adaptive_branch_specific_cost_advantage():
    # Decision classes are crossed across the root branches. A branch-specific
    # test resolves each branch, but neither branch test resolves the other.
    # Add costs so a fixed resolving set must pay for both branch tests plus a
    # cross-separator, while an adaptive tree can condition the second test.
    worlds = ("a0", "a1", "b0", "b1")
    decisions = {"a0": 0, "a1": 1, "b0": 2, "b1": 3}
    root = Experiment("root", 1.0, {"a0": "A", "a1": "A", "b0": "B", "b1": "B"})
    left = Experiment("left", 1.0, {"a0": 0, "a1": 1, "b0": 0, "b1": 0})
    right = Experiment("right", 1.0, {"a0": 0, "a1": 0, "b0": 0, "b1": 1})
    p = DecisionProblem(worlds, decisions, (CapabilityStage(0.0, (root, left, right)),))
    assert minimum_batch_acquisition_cost(p, 0.0) == 3.0
    assert minimum_adaptive_acquisition_cost(p, 0.0) == 2.0


def test_persistence_validator_and_regressive_transition():
    worlds = ("a", "b")
    decisions = {"a": 0, "b": 1}
    sep = Experiment("sep", 1.0, {"a": 0, "b": 1})
    constant = Experiment("constant", 1.0, {"a": 0, "b": 0})
    p = DecisionProblem(worlds, decisions, (
        CapabilityStage(0.0, (sep,)),
        CapabilityStage(1.0, (constant,)),
    ))
    assert not is_persistent(p)
    assert classify_transition(p, 0.0, 1.0) == "regressive"
