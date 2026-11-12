<!-- Q: Each server handles 1,200 requests/second. Peak traffic is 9,500 requests/second and we need 30% headroom above peak. How many servers do we need? -->

You need **11 servers**.

With 30% headroom, the target capacity is 9,500 × 1.3 = 12,350 requests/second. Each server handles 1,200, so 12,350 ÷ 1,200 = 10.29. Round up to 11, because a partial server can't take the remaining load.

With 11 servers, capacity is 13,200 requests/second, which is about 39% above peak. That margin holds only if load is spread evenly across the servers. If one server fails, the remaining 10 handle 12,000 requests/second, which is still above peak but leaves only about 26% headroom. If you want full headroom during a single-server failure, plan for 12 servers.
