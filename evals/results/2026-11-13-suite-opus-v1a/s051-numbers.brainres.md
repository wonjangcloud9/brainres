<!-- Q: My API handles 120 requests per second on average. How many requests is that per day? -->

120 × 86,400 seconds/day = **10,368,000 requests per day** (about 10.4 million).

That figure assumes the 120/s average holds across all 24 hours. Real traffic usually peaks during business hours. If you're sizing capacity, measure your peak requests per second from your logs and plan for that number.
