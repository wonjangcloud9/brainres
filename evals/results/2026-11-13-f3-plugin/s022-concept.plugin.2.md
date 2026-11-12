<!-- Q: Explain eventual consistency. -->

Eventual consistency means that if no new writes arrive, all replicas of a piece of data will converge to the same value, but reads in the meantime may return stale data.

**Why it exists:** A distributed database keeps copies of data on several nodes. Waiting for every copy to confirm each write makes writes slow, and it blocks writes entirely if a node or network link fails. Eventual consistency lets a write succeed after one node accepts it. The write then propagates to the other replicas in the background.

**Where it's used:** DynamoDB (default reads), Cassandra, DNS, S3 (before 2020), and CDN caches. These systems favor availability and low latency over always-fresh reads, which is the trade-off the CAP theorem describes.

**Example:** You update your profile photo, and the write lands on replica A. You refresh immediately and your request hits replica B, which still shows the old photo. A few hundred milliseconds later B receives the update, and every read returns the new photo.

**What you give up:**
- Stale reads for a short window.
- Concurrent writes to the same key can conflict. The system must resolve them, usually with last-write-wins or version vectors, and last-write-wins can silently drop an update.
- Application code has to tolerate these anomalies.

**When it's a bad fit:** Account balances, inventory counts, and anything where a stale read causes real harm. Use strong consistency there, or a stronger middle ground such as read-your-writes or quorum reads (R + W > N).

Next step: if you have a specific system in mind, tell me which one and I can show how its consistency settings work.
