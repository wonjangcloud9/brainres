<!-- Q: A 2 TB disk (2,000 GB) is 35% full and grows by 18 GB per day. After how many whole days will usage first exceed 90%? -->

**62 days.** Usage starts at 700 GB (35% of 2,000 GB). The 90% threshold is 1,800 GB, so the disk must gain 1,100 GB.

- Day 61: 700 + 61 × 18 = 1,798 GB (89.9%), still below the threshold.
- Day 62: 700 + 62 × 18 = 1,816 GB (90.8%), the first day above 90%.

Since 1,100 ÷ 18 ≈ 61.1, the exact crossing falls partway through day 62. If you want an alert before it happens, set it for around day 60 to leave margin.
