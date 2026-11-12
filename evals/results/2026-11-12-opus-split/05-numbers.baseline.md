<!-- Q: A test for a disease is 99% accurate and 1 in 1,000 people have it. I tested positive. How likely is it that I actually have it? -->

# About 9%

That's assuming "99% accurate" means the test catches 99% of people who have the disease and correctly clears 99% of people who don't.

## Picture 100,000 people

| | Have the disease | Don't have it |
|---|---|---|
| **Total** | 100 | 99,900 |
| **Test positive** | 99 (true positives) | 999 (false positives) |

About 1,098 people test positive, and only 99 of them actually have the disease:

**99 ÷ 1,098 ≈ 9%**

## Why it's so low

The disease is rare. The 1% error rate applies to a huge pool of healthy people, so it produces about 10 times more false positives than there are real cases.

The formal version is Bayes' theorem:

$$P(\text{disease} \mid +) = \frac{0.99 \times 0.001}{0.99 \times 0.001 + 0.01 \times 0.999} \approx 0.090$$

## In real life

- **Your starting odds may not be 1 in 1,000.** That figure applies to random screening. If you were tested because of symptoms, exposure, or family history, your odds before the test were higher, and so are your odds now.
- **A second, independent test changes a lot.** If a follow-up test is also positive, the probability rises to about **91%**. This is why doctors usually confirm a positive screening result before diagnosing.
- **"Accuracy" can be split differently.** The rate of catching real cases and the rate of false alarms are often not equal, and the false-alarm rate matters most here.

If this is about a real result, ask your doctor whether a confirmatory test is recommended. A single positive screen for a rare condition is a reason to follow up, not a diagnosis.
