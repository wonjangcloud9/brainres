<!-- Q: A test for a disease is 99% accurate and 1 in 1,000 people have it. I tested positive. How likely is it that I actually have it? -->

About **9%**, not 99%, assuming "99% accurate" means 99% sensitivity and 99% specificity.

Take 100,000 people:

- 100 have the disease. The test catches 99 of them.
- 99,900 do not. The test wrongly flags 1% of them, which is 999 people.
- Total positives: 99 + 999 = 1,098.
- Chance you are one of the true positives: 99 / 1,098 ≈ **9%**.

The disease is rare, so false positives from the large healthy group outnumber true positives about 10 to 1. This is Bayes' theorem: the low base rate (0.1%) pulls the result down far below the test's accuracy.

"Accurate" can mean different things. If the test's false-positive rate is not 1%, the answer changes. A 0.1% false-positive rate would give about 50%.

Next step: ask for a confirmatory test, ideally a different method. A second positive would raise your odds to roughly 90%, since the prior is now about 9% instead of 0.1%.
