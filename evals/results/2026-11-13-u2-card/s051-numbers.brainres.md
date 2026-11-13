<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 req/s × 86,400 s/day = **10,368,000 requests per day** (about 10.4 million).

This assumes 120 is a steady average over all 24 hours. If traffic peaks during the day, the peak-hour rate will be well above 120, so size capacity for the peak rather than this daily total.
