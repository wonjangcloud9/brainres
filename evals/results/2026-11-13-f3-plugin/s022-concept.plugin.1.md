<!-- Q: Explain eventual consistency. -->

Eventual consistency means that if no new writes arrive, all replicas of a piece of data will converge to the same value, but reads in the meantime may return stale data.

**Why it exists:** A distributed database keeps copies (replicas) on several machines. Waiting for every replica to confirm each write makes writes slow and blocks them if a node is unreachable. Eventual consistency accepts a short window of disagreement in return for speed and availability. This is the trade-off the CAP theorem describes: during a network partition, you choose between consistency and availability, and eventually consistent systems choose availability.

**Where it's used:** DynamoDB (default reads), Cassandra, S3 in its early years (it is now strongly consistent), DNS, and CDN caches.

**Example:** You update your profile photo. The write lands on replica A. For a few hundred milliseconds, replica B still holds the old photo. If a friend's request is routed to B, they see the old photo. After A propagates the change to B, every replica returns the new photo.

**Key points:**
- "Eventually" has no fixed bound. It is usually milliseconds, but it can be longer during failures.
- Concurrent writes to the same item can conflict. Systems resolve them with last-write-wins, vector clocks, or CRDTs (data types designed to merge without conflicts).
- Many systems offer tunable consistency. In Cassandra, for instance, you can require a quorum of replicas to agree on a read or write when you need stronger guarantees.

**Use it when** stale reads are tolerable, such as feeds, likes, or caches. **Avoid it when** they are not, such as account balances or inventory counts at checkout.

Next step: if you have a specific system in mind, tell me which one and I can show how it handles this.
