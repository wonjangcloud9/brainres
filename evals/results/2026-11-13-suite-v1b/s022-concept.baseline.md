<!-- Q: Explain eventual consistency. -->

**Eventual consistency** is a consistency model for distributed systems: if no new updates are made to a piece of data, all replicas will eventually converge to the same value. It doesn't promise *when*, only that they will.

## Why it exists

Data is replicated across multiple nodes for availability, fault tolerance, and low latency. Keeping every replica perfectly in sync on every write requires coordination (waiting for acknowledgments across nodes, possibly across regions), which is slow and fails when the network partitions. The CAP theorem says that during a partition you must choose between consistency and availability. Eventually consistent systems choose availability.

## How it behaves

1. A client writes `x = 5` to replica A.
2. A acknowledges immediately and propagates the write to B and C in the background.
3. For a short window, a read from B may still return the old value of `x`.
4. Once propagation completes, all replicas return `5`.

## Common mechanisms for convergence

- **Asynchronous replication**: writes are shipped to other replicas after acknowledgment.
- **Read repair**: when a read finds replicas disagreeing, the stale ones are fixed.
- **Anti-entropy / gossip**: background processes compare and sync data between nodes (e.g., Merkle trees).
- **Hinted handoff**: a node holds writes for an unreachable peer and delivers them later.
- **Conflict resolution**: concurrent writes to the same key need a rule, such as last-write-wins (timestamps), vector clocks, or CRDTs that merge automatically.

## Trade-offs

**Pros:** high availability, low write latency, good horizontal scalability, works across regions and during partitions.

**Cons:** stale reads, possible conflicting writes, and application code must tolerate anomalies, such as a user not seeing their own just-posted comment.

## Stronger variants

Many systems offer guarantees layered on top:
- **Read-your-writes**: you always see your own updates.
- **Monotonic reads**: you never see data go "backward" in time.
- **Causal consistency**: causally related operations are seen in order.
- **Tunable consistency** (Cassandra, DynamoDB): choose per-query how many replicas must respond (e.g., quorum reads/writes where R + W > N give strong consistency).

## Where you see it

DNS, DynamoDB (default reads), Cassandra, Riak, S3 (historically, now strongly consistent), social media feeds and like counts, CDN caches.

## When it's a good fit

Use it when availability and speed matter more than instantly-accurate reads: feeds, counters, caches, shopping carts. Avoid it (or use strong consistency) for things like bank balances, inventory that can't oversell, or uniqueness constraints.
