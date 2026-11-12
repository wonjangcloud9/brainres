<!-- Q: Five people each put a hat in a box and each takes one back at random. In how many of the possible outcomes does nobody get their own hat? -->

**44** of the 120 possible outcomes leave nobody with their own hat.

The count is the derangement number D₅. Inclusion-exclusion gives:

D₅ = 5! × (1 − 1/1! + 1/2! − 1/3! + 1/4! − 1/5!) = 120 − 120 + 60 − 20 + 5 − 1 = 44

If you want to check this by hand, list the 44 permutations with no fixed points, or run a short script that counts them.
