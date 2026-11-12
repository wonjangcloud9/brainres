<!-- Q: How many integers from 1 to 1000 inclusive are divisible by 3 or 5 but not by 7? Work it out without code. -->

**401** integers from 1 to 1000 are divisible by 3 or 5 but not by 7.

1. Multiples of 3 or 5: 333 + 200 − 66 = 467, where 66 counts multiples of 15 that were counted twice.
2. Multiples of 7 among them: 47 + 28 − 9 = 66, using multiples of 21, 35, and 105.
3. 467 − 66 = 401.

As a check, count without the overlap: multiples of 3 not divisible by 7 (286) plus multiples of 5 not divisible by 7 (172) minus multiples of 15 not divisible by 7 (57) also gives 401.
