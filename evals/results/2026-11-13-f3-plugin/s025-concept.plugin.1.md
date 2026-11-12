<!-- Q: What does idempotent mean in REST APIs? -->

An idempotent request leaves the server in the same state whether you send it once or many times in a row.

This matters because networks fail. If a client times out, it can safely retry an idempotent request without risking duplicate side effects.

| Method | Idempotent? | Why |
|---|---|---|
| GET, HEAD, OPTIONS | Yes | They only read. |
| PUT | Yes | It replaces the resource with the same data each time. |
| DELETE | Yes | After the first call the resource is gone, so later calls change nothing. |
| POST | **No** | Each call typically creates a new resource. |
| PATCH | Depends | `{"views": 5}` is idempotent, but "increment views by 1" is not. |

**Example:** `PUT /users/42` with `{"name": "Ana"}` sets the name to Ana. Sending it five times still leaves one user named Ana. `POST /orders` sent five times can create five orders.

Idempotent refers to server state, not the response. A repeated `DELETE` may return `204` the first time and `404` after, and it still counts as idempotent.

To make a POST safe to retry, such as for payments, have the client send an idempotency key header (for example `Idempotency-Key: <uuid>`). The server then ignores repeats of the same key.
