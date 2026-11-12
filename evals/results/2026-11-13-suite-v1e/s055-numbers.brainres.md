<!-- Q: A test is 99% accurate and 1 in 1,000 people have the disease. If I test positive, what's the chance I actually have it? -->

0.99 × 0.001 / (0.99 × 0.001 + 0.01 × 0.999) ≈ 0.090, so about a **9%** chance you have the disease.

This assumes "99% accurate" means both 99% sensitivity (sick people test positive) and 99% specificity (healthy people test negative). If the test's two error rates differ, the answer changes.

The result is low because healthy people vastly outnumber sick ones. Out of 100,000 people:

| Group | People | Test positive |
|---|---|---|
| Have the disease (1 in 1,000) | 100 | 99 |
| Healthy | 99,900 | 999 (1% false positives) |

Of the 1,098 positives, only 99 are truly sick, and 99 / 1,098 ≈ 9%.

If you tested positive, the next step is a second, independent test. It would raise the odds sharply, to roughly 91%.
