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
