<!-- Q: What does idempotent mean in REST APIs? -->

An operation is **idempotent** if performing it multiple times has the same effect on the server's state as performing it once. The response may differ between calls (e.g., a first `DELETE` returns 200, a repeat returns 404), but the resulting state is the same.

## By HTTP method

| Method | Idempotent | Notes |
|--------|-----------|-------|
| GET | Yes | Read-only (also "safe") |
| HEAD, OPTIONS | Yes | Read-only |
| PUT | Yes | Replaces the resource with the given representation; repeating yields the same state |
| DELETE | Yes | Resource is gone after the first call; later calls change nothing |
| POST | **No** | Typically creates a new resource each time, so retries can create duplicates |
| PATCH | **Not guaranteed** | Depends on the operation: `{"name": "x"}` is idempotent, `{"op": "increment"}` is not |

## Examples

- `PUT /users/42` with `{"name": "Ana"}`: run it 5 times, and user 42 is still named Ana. Idempotent.
- `DELETE /users/42`: the user is deleted once; repeats don't delete anything else. Idempotent.
- `POST /orders`: run it 5 times, and you get 5 orders. Not idempotent.

## Why it matters

Networks fail. If a client sends a request and the connection times out, it doesn't know whether the server processed it. With idempotent methods, the client can **safely retry**. With non-idempotent ones, a retry might cause duplicate charges, orders, etc.

## Making POST idempotent

A common pattern is an **idempotency key**: the client sends a unique ID in a header (e.g., `Idempotency-Key: 8f3a...`). The server stores the result of the first request with that key and returns the same result for any repeat, rather than processing it again. Stripe's API popularized this.

## Idempotent vs. safe

- **Safe**: doesn't modify server state (GET, HEAD, OPTIONS).
- **Idempotent**: repeating doesn't change the outcome beyond the first call.

All safe methods are idempotent, but not all idempotent methods are safe (PUT and DELETE modify state).
