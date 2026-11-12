<!-- Q: How many 4-digit numbers have digits that add up to 9? -->

There are **165** such numbers.

The first digit must be 1–9, and the other three can be 0–9. Subtract 1 from the first digit so it ranges over 0–8. Then the four digits form a nonnegative solution to $x_1 + x_2 + x_3 + x_4 = 8$, and no digit can exceed 9 because the total is only 8. By stars and bars, that gives $\binom{11}{3} = 165$.

As a check: there are $\binom{12}{3} = 220$ four-digit strings (leading zeros allowed) with digits summing to 9. Of those, $\binom{11}{2} = 55$ start with 0, leaving $220 - 55 = 165$.
