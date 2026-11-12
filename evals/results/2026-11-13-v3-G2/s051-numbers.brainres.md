<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 req/s × 86,400 s/day = 10,368,000 requests per day (about 10.4 million).

This assumes 120/s holds around the clock. If traffic peaks in the daytime and drops at night, the real daily total is the same only if 120 is the true 24-hour average. If it is a business-hours average, the daily total will be lower.

Next step: if you're sizing capacity, check your peak requests per second, since that matters more than the average.
