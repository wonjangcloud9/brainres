<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 × 86,400 seconds/day = **10,368,000 requests per day** (about 10.4 million).

This assumes the 120 req/s average holds for all 24 hours. If traffic is lower overnight, the real daily total depends on your actual distribution, so check your request-count metric over a full day.
