<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 req/s × 86,400 s/day = **10,368,000 requests per day** (about 10.4 million).

This assumes the 120 req/s average holds across all 24 hours. If your traffic peaks during the day, the peak rate will be well above 120, so size capacity for the peak, not the average.
