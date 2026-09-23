from __future__ import annotations

import csv
import json
from math import isinf
from pathlib import Path

from rfs import Experiment, CapabilityStage, DecisionProblem, decision_kernel, minimum_acquisition_cost, classify_transition


def problem_suite():
    worlds = ("w0", "w1", "w2", "w3")
    decisions = {"w0": 0, "w1": 0, "w2": 1, "w3": 1}

    expensive = Experiment("expensive_resolver", 100.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})
    irrelevant = Experiment("new_but_irrelevant", 1.0, {"w0": 0, "w1": 1, "w2": 0, "w3": 1})
    medium = Experiment("medium_resolver", 20.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})
    cheap = Experiment("cheap_resolver", 2.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})

    null_intensive = DecisionProblem(
        worlds,
        decisions,
        (
            CapabilityStage(0.0, (expensive,)),
            CapabilityStage(1.0, (expensive, irrelevant)),
            CapabilityStage(2.0, (expensive, irrelevant, medium)),
            CapabilityStage(3.0, (expensive, irrelevant, medium, cheap)),
        ),
    )

    constant = Experiment("constant", 1.0, {"w0": 0, "w1": 0, "w2": 0, "w3": 0})
    splitter = Experiment("new_separator", 5.0, {"w0": 0, "w1": 0, "w2": 1, "w3": 1})
    extensive = DecisionProblem(
        worlds,
        decisions,
        (
            CapabilityStage(0.0, (constant,)),
            CapabilityStage(1.0, (constant,)),
            CapabilityStage(2.0, (constant, splitter)),
        ),
    )
    return {"null_intensive": null_intensive, "extensive": extensive}


def main():
    outdir = Path("artifacts")
    outdir.mkdir(exist_ok=True)
    rows = []
    summary = {}

    for name, p in problem_suite().items():
        budgets = sorted({s.generation_budget for s in p.stages})
        prev = None
        summary[name] = {"budgets": budgets, "rows": []}
        for g in budgets:
            k = decision_kernel(p, g)
            a = minimum_acquisition_cost(p, g)
            regime = "initial" if prev is None else classify_transition(p, prev, g)
            row = {
                "problem": name,
                "generation_budget": g,
                "kernel_size": len(k),
                "acquisition_cost": "inf" if isinf(a) else a,
                "transition": regime,
            }
            rows.append(row)
            summary[name]["rows"].append(row)
            prev = g

    with (outdir / "closure_cost_frontier.csv").open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    with (outdir / "closure_cost_summary.json").open("w") as f:
        json.dump(summary, f, indent=2)

    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
