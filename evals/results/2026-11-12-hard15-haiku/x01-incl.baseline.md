<!-- Q: How many integers from 1 to 1000 inclusive are divisible by 3 or 5 but not by 7? Work it out without code. -->

**401**

Let A be the multiples of 3, B the multiples of 5, and C the multiples of 7, all in 1 to 1000.

1. Multiples of 3 or 5: |A| + |B| − |A∩B| = 333 + 200 − 66 = 467 (since ⌊1000/15⌋ = 66).
2. Of those, the ones also divisible by 7 are multiples of 21 or 35: |A∩C| + |B∩C| − |A∩B∩C| = 47 + 28 − 9 = 66 (using ⌊1000/21⌋ = 47, ⌊1000/35⌋ = 28, and ⌊1000/105⌋ = 9).
3. Subtract: 467 − 66 = 401.
