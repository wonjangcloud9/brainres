<!-- Q: What does idempotent mean in REST APIs? -->

An HTTP method is idempotent if sending the same request once or many times leaves the server in the same state.

The key point is that it concerns **server state**, not the response. A repeated `DELETE /users/42` may return `200` the first time and `404` the second, but the end state (user 42 gone) is identical.

| Method | Idempotent | Why |
|---|---|---|
| GET, HEAD, OPTIONS | Yes | Read-only |
| PUT | Yes | Replaces the resource with the same body every time |
| DELETE | Yes | The resource stays deleted |
| POST | No | Each call typically creates a new resource |
| PATCH | Not guaranteed | Depends on the operation: `{"name": "Bo"}` is safe to repeat, `{"increment": 1}` is not |

It matters because networks fail. If a client times out, it can't tell whether the server processed the request. With an idempotent method, it can retry safely. With `POST /payments`, a retry could charge the customer twice.

For non-idempotent operations, a common fix is an idempotency key: the client sends a unique header such as `Idempotency-Key: <uuid>`, and the server returns the stored result for any repeated key instead of acting again.

Next step: check which of your endpoints use POST for retry-prone actions, and consider adding idempotency keys there.
