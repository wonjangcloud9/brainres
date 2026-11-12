<!-- Q: A test is 99% accurate and 1 in 1,000 people have the disease. If I test positive, what's the chance I actually have it? -->

About **9%**, assuming "99% accurate" means 99% sensitivity and 99% specificity.

Imagine 100,000 people:

- **Sick:** 100 people (1 in 1,000). The test catches 99 of them (true positives).
- **Healthy:** 99,900 people. The test wrongly flags 1% of them, about 999 (false positives).

Total positives: 99 + 999 = 1,098. Of those, only 99 are actually sick.

P(disease | positive) = 99 / 1,098 ≈ **9.0%**

Because the disease is rare, false positives from the huge healthy group outnumber the true positives. That's why a positive result from a very accurate test can still mean you're probably healthy, and why doctors usually confirm with a second test.
