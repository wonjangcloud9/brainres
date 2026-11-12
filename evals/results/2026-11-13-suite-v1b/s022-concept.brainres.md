<!-- Q: Explain eventual consistency. -->

Eventual consistency means that after a write, replicas of the data may briefly disagree, but if no new writes arrive, all replicas will converge to the same value.

**Why it exists:** A system with copies in several places (servers, regions) can either wait for every copy to confirm each write, or acknowledge the write after one copy and sync the rest in the background. Waiting is slow and fails when a node is unreachable. Syncing in the background stays fast and available, at the cost of temporarily stale reads. This is the trade-off the CAP theorem describes: during a network partition you pick availability or strict consistency, and eventual consistency picks availability.

**Example:** You change your profile photo.
1. The write lands on replica A and is acknowledged.
2. A reads from replica B a moment later and still sees the old photo.
3. A propagates the change to B in the background (usually milliseconds to seconds).
4. Now every replica returns the new photo.

**What it does not promise:** It gives no bound on how long convergence takes, and it does not guarantee you will read your own write. Many systems add weaker-than-strong but useful guarantees on top, such as read-your-writes or monotonic reads.

**Conflicts:** If two replicas accept different writes to the same item at the same time, the system needs a rule to pick a winner: last-write-wins by timestamp, vector clocks, or CRDTs that merge automatically.

**Where you see it:** DynamoDB (default reads), Cassandra, DNS, CDN caches, and social feed counters like "likes".

**When to avoid it:** Account balances, inventory that cannot oversell, and anything where a stale read causes real harm. Use strong consistency there.

If you want, I can show how Cassandra's tunable consistency levels (`ONE`, `QUORUM`, `ALL`) move you along this spectrum.
