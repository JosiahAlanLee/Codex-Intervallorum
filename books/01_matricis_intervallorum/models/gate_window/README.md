# Gate and window

A supplementary harm-accounting illustration. Its results are conditional on the specified arithmetic and chosen parameter grid. They do not establish the practical superiority, novelty or uselessness of the book's proposals.

## What is compared

- **A, universal gate:** each proposed action waits for review. The gate catches wrong proposals with probability `delta` and rejects correct ones with probability `phi`.
- **B, unreviewed action:** the operator acts immediately after diagnosis. This is a limiting comparator, not a representation of the full HRO approach.
- **C, window-bounded gate:** wait for review until the deadline, then execute without review. Execution is instantaneous in this model; an action at exactly the deadline avoids the late-action loss.

Table VIII proposes bounded standing dispatch authority with notification, safety coordination and independent review. C omits these safeguards and the time needed to carry out an action. Calling C a test of that intervention overstates the correspondence. HRO's deference to relevant expertise includes shared inquiry and cross-monitoring; it is not equivalent to B's absence of review.

## Assumptions and units

One incident, one operator, one gate, repeated attempts, one window `H = 1`. There are no incentives, learning, budgets, competing operators, organisational culture or observed allocation of blame. A wrong executed action has an additive cost and the incident continues. A correct action ends it. Total harm is:

`T + h_window * [T > 1] + h_wrong * (wrong actions executed)`.

Time is converted into harm at an assumed unit rate. The deadline loss is a step and execution takes no time. Wrong actions do not alter future diagnosis or damage the repair capacity. These assumptions need substantive defense before application to an institution.

| Parameter | Meaning | Grid | Evidence status |
| --- | --- | --- | --- |
| `eps` | Probability a proposed action is wrong | .05, .15, .30, .45, .60 | Assumed. A deployment's observed failure rate does not estimate this pre-review incident-proposal probability. |
| `delta` | Probability the gate catches a wrong proposal | 0, .10, .25, .50, .75, .95 | Assumed. DORA supplies no numerical bound on this conditional probability. |
| `phi` | Probability the gate rejects a correct proposal | 0, .25 | Assumed. |
| `lam` | Median approval latency relative to the window | .01, .03, .10, .30, 1, 3, 10 | Assumed; no observed incident-window calibration. |
| `sigma` | Log-standard deviation of latency | .75 | Assumed. |
| `d` | Diagnosis time per attempt | .10 | Assumed. |
| `h_wrong` | Harm of a wrong executed action | .1, .5, 1, 3, 10 | Assumed; no incident is assigned a measured value. |
| `h_window` | Additional harm after the deadline | 1, 3, 10 | Assumed. |

The **assumed scenario region** is `delta <= .25`, `.3 <= lam <= 10`, `.05 <= eps <= .6`. The historical JSON key `anchored_region` remains for compatibility. This region is not an estimate supported by DORA or VOID. DORA's change-delivery findings motivate examining review processes; they do not identify these parameters. Grid-cell percentages weight each selected cell equally and are not probabilities for real organisations.

The **gate's home** is the chosen subregion `delta >= .75`, `lam <= .1`. The name expresses a construction check, not an independently measured domain.

## The local rule and its limits

The numerical rule is published alongside the model and results. No independently verifiable preregistration is asserted. The criteria are read from `verdict.json`, with both that file and `verdict.py` hashed in the manifest. These digests check consistency.

`2_region` means C's estimated harm beats A by the .5% margin in at least two thirds of the assumed region (also after dropping the lowest `eps`), while A **holds** at least a quarter of the gate's home. Holds includes ties and differences below the margin. B does not decide this pairwise rule. Meeting it does not show that C is best, that A wins a quarter of its home, or that the book passed an empirical test. The exact other thresholds are in the JSON.

See [REPORT.md](REPORT.md) for the current counts, including strict A wins, ties and B comparisons. The original run's A-holds fraction was about 61%, with about 23% strict A wins; B beat C in nearly all of the assumed region. These are finite-sample summaries of the grid, not institutional prevalence estimates.

## Numerical uncertainty and regeneration

Common random numbers can reduce variance in a paired comparison; they do not remove sampling error. The .5% margin is a decision threshold, not a confidence interval. Single-seed minimum-latency tables have been withdrawn because boundary cells can change category with further draws. The raw rows remain inspectable. Any claimed boundary needs paired uncertainty estimates or a separate precision analysis; no such analysis is claimed here. The figure likewise shows estimated categories.

The model's arithmetic and grid are unchanged by this presentation revision. Regeneration uses the recorded seed and sample count. The manifest checks computational consistency, while tests check specified limits. Neither is empirical validation.

```sh
python -m unittest discover -s books/01_matricis_intervallorum/models/gate_window/tests -v
python books/01_matricis_intervallorum/models/gate_window/run.py
python books/01_matricis_intervallorum/models/gate_window/report.py
python books/01_matricis_intervallorum/models/gate_window/validate.py
```

## Sources and access

- AHRQ, [High Reliability](https://psnet.ahrq.gov/primer/high-reliability), citing Weick and Sutcliffe. Relevant primer directly read; *Managing the Unexpected* was not newly inspected.
- Fricke et al. (2025), [HRO implementation rapid review](https://pubmed.ncbi.nlm.nih.gov/41248244/). Abstract and findings read; evidence concerns healthcare and remains limited. It is not a calibration dataset for this model.
- DORA, [Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/). Relevant primary programme page read; its underlying 2019 report was not independently read.
- VOID's 2021 launch coverage was consulted in the original pass and supplied no durations. It supplies no parameter estimate here.
- Elish (2019), *Moral Crumple Zones*, motivates examining responsibility allocation. The model's booked-harm function assumes an accounting split; it does not measure that allocation or explain why gates persist.
- Book I-II, Tables VIII and XIII, are the proposal and evaluation discussion this illustration accompanies. Their historical and normative claims have separate evidential burdens.

Model and numerical rule developed with Claude; interpretation, source limits and consistency checks revised with ChatGPT/Codex. Public version prepared 18 October 2026. See the [evidence review](../../../../docs/research/evidence/README.md) and [pilot methods](../../../../docs/research/evidence/pilot-methods.md).
