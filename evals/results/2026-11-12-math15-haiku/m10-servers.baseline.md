<!-- Q: Each server handles 1,200 requests/second. Peak traffic is 9,500 requests/second and we need 30% headroom above peak. How many servers do we need? -->

Required capacity with 30% headroom:

9,500 × 1.30 = 12,350 requests/second

Servers needed:

12,350 ÷ 1,200 = 10.29 → **11 servers** (rounding up, since you can't deploy a fraction of a server)
