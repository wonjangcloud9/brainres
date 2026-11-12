<!-- Q: What does idempotent mean in REST APIs? -->

An idempotent request has the same effect on the server whether you send it once or many times, so retries are safe.

It matters when a network call times out and the client can't tell whether the server processed it. With an idempotent method the client can just retry.

| Method | Idempotent? |
|---|---|
| GET, HEAD, OPTIONS | Yes (also safe, since they don't change state) |
| PUT, DELETE | Yes |
| POST | **No** |
| PATCH | Not guaranteed. It depends on the operation. |

**Example:**
- `PUT /users/42` with `{"name": "Ana"}` sets the name to Ana. Sending it five times leaves the same result as sending it once.
- `DELETE /users/42` removes the user. The second call may return 404 instead of 204, but the server state is the same, and idempotency is about state, not response codes.
- `POST /orders` creates a new order on every call, so a retry can create duplicates.
- `PATCH /counter` with `{"op": "increment"}` is not idempotent. `PATCH` with `{"status": "shipped"}` is.

For POST, such as payments, APIs often add an `Idempotency-Key` header. The server stores the key and returns the original result if the same key arrives again.

Next step: check that your PUT and DELETE handlers are idempotent, and add idempotency keys to POST endpoints that clients retry.
