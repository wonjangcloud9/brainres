<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 req/s × 86,400 s/day = 10,368,000 requests per day (about 10.4 million).

That assumes the 120/s average holds across all 24 hours. If traffic is bursty or has daily peaks, the peak-hour rate will be well above 120/s, so size capacity for the peak rather than the average.

Next step: if you want, give me your peak-to-average ratio and I'll work out the peak requests per second to plan for.
