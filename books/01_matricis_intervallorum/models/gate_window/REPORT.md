# Gate and window: conditional model report

Generated from 6300 assumed grid cells, 6000 samples per cell, seed 20261018. This is a supplementary illustration. The parameters are not empirically calibrated; grid-cell percentages are not probabilities for real organisations.

## Local rule outcome

**Outcome 2_region.** The assumed scenario-region C-win criteria and the gate-home A-holds criterion are satisfied. Holds includes ties and sub-margin differences; it does not require A superiority. This is satisfaction of a chosen A-versus-C rule, not empirical validation or selection of C over B.

The numerical criteria are preserved from the initial rule. Their provenance does not establish independently verifiable preregistration. They select an A-versus-C comparison; B is reported separately.

| Estimated grid fraction | Value |
| --- | --- |
| C beats A, all cells | 0.750 |
| C beats A, assumed scenario region (1800 cells) | 0.996 |
| C beats A, scenario without lowest eps | 0.994 |
| A holds in gate home, including ties (900 cells) | 0.607 |
| A strictly beats C by the margin, gate home | 0.226 |
| Neither beats the other by the margin, gate home | 0.381 |
| A strictly beats C by the margin, all cells | 0.061 |
| Neither beats the other by the margin, all cells | 0.189 |

The A-holds criterion is 0.250; it is a non-superiority criterion for C, not an A-win requirement. Strict A wins do not meet that fraction. The scenario C-win thresholds are 0.666667 and 0.666667; the construction-check thresholds are 0.950 overall or 0.900 in gate home.

## Include the third comparator

| Estimated grid fraction | Value |
| --- | --- |
| B beats C, all cells | 0.815 |
| B beats C, assumed scenario region | 0.996 |
| C beats B, all cells | 0.179 |
| C beats B, gate home | 0.656 |

C beats B outside the designated gate home in 540 cells. Its advantage over B is therefore not confined to that named region. B usually beats C in the selected scenario region. Neither result licenses treating C as the best practical arrangement.

B is immediate unreviewed action, not a full HRO implementation. C waits until the deadline and then acts unreviewed, with instantaneous execution. It omits the safeguards and execution time of Table VIII. A comparison among these constructions is not a test of that dispatch proposal.

## Booked accounting

With delta > 0, A has lower booked harm than C in 0.722 of cells; C has lower booked harm in 0.132.

Booked harm counts executed wrong actions and omits delay and missed-window losses by assumption. This is not an observation of blame, an explanation of why review gates persist, or evidence of their motives.

## Precision and reproducibility

The decision margin is 0.005. These are finite-sample estimates without paired uncertainty intervals. Common random numbers may reduce variance; they do not remove sampling error. The single-seed minimum-latency tables have been withdrawn because a first threshold crossing can change with additional draws. The raw results remain available. No precise boundary is established here.

`region.svg` shows estimated A-versus-C categories for selected slices; blank cells have neither estimated advantage at the margin. The dashed scenario region is assumed, not data-calibrated.

Largest truncated fraction: 0.00e+00. The validator checks hashes, regenerates a sample of cells, and verifies this complete generated report. These checks establish computational consistency, not empirical validity.

Further modeling is not required for the book. An operational superiority claim would require a specified increment, a credible comparator, appropriate observations and an evaluation capable of distinguishing them.
