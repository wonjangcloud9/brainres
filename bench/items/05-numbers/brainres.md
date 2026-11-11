<!-- Q: A test for a disease is 99% accurate and 1 in 1,000 people have it. I tested positive. How likely is it that I actually have it? -->

About 9%, not 99%, assuming "99% accurate" means 99% sensitivity and 99% specificity (~85% sure that's the intended reading; the answer changes if the test's accuracy is defined differently).

Here is the worked example with 100,000 people:

- 100 have the disease. The test catches 99 of them (true positives).
- 99,900 don't have it. The test wrongly flags 1% of them, which is 999 (false positives).
- Total positives: 99 + 999 = 1,098.
- Chance you're truly sick given a positive: 99 / 1,098 ≈ **9%**.

The reason is the base rate. The disease is so rare that false positives from the huge healthy group outnumber true positives from the tiny sick group, roughly 10 to 1.

Next step: a second, independent test. If it's also positive, the odds jump to about 91%, because the first result raises your prior from 0.1% to 9%.
