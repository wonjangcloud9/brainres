<!-- Q: A test is 99% accurate and 1 in 1,000 people have the disease. If I test positive, what's the chance I actually have it? -->

0.001 × 0.99 / (0.001 × 0.99 + 0.999 × 0.01) = 0.00099 / 0.01098 ≈ **9%**, so a positive result leaves you at roughly a 1-in-11 chance of having the disease.

This assumes "99% accurate" means both sensitivity and specificity are 99% (1% false negatives, 1% false positives). Check the test's actual figures, because if they differ the answer shifts.

The intuition: in 100,000 people, about 100 have the disease and 99 of them test positive. Of the 99,900 healthy people, 1% (about 999) also test positive. So about 99 of every 1,098 positives are real.

The rare disease is the reason: false positives from the large healthy group swamp the true positives from the small sick group.

Next step: a second, independent test would raise the odds sharply, to about 90% if it is also 99% accurate.
