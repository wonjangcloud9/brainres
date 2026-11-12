<!-- Q: How many trailing zeros does 125! have? -->

**125! has 31 trailing zeros.**

Each trailing zero needs one factor of 10, which is one factor of 2 paired with one factor of 5. Factors of 2 are more plentiful than factors of 5, so the count is set by the factors of 5:

- ⌊125/5⌋ = 25 multiples of 5
- ⌊125/25⌋ = 5 multiples of 25, each adding one more 5
- ⌊125/125⌋ = 1 multiple of 125, adding one more 5

Total: 25 + 5 + 1 = 31.
