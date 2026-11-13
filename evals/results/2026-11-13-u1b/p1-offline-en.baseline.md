<!-- Q: Write an implementation plan for adding offline support to our React Native notes app. Notes sync to a REST API. -->

# Offline Support Implementation Plan: React Native Notes App

I haven't inspected your codebase, so this plan assumes a typical setup: REST API, some state layer (Redux, Zustand, or React Query), and no local persistence yet. Tell me what you actually use and I'll adjust it.

## Approach

Use a **local-first** model. The UI reads and writes only to a local database. A background sync engine reconciles that database with the API, so the app behaves the same online and offline.

## Phase 1: Local persistence

- **Storage:** SQLite via `op-sqlite` or `expo-sqlite`. WatermelonDB is an option if you want built-in sync primitives. Avoid AsyncStorage for notes because it has poor query support and size limits.
- **Schema changes to `notes`:**
  - `id` (client-generated UUID, so notes can be created offline)
  - `server_id` (nullable)
  - `title`, `body`
  - `updated_at` (local), `server_updated_at`
  - `deleted` (soft-delete flag)
  - `sync_status` (`synced | pending | conflict`)
- **Outbox table (`pending_ops`):** `op_id`, `note_id`, `type` (create/update/delete), `payload`, `created_at`, `attempts`.
- Create a repository layer (`NotesRepo`) so screens never call the API directly.

## Phase 2: Refactor reads and writes

- Point screens at `NotesRepo` and use live queries or subscriptions so the UI updates on local changes.
- Every write does two things in a single transaction: update the `notes` row and append to `pending_ops`.
- Coalesce ops for the same note, for example create followed by update becomes one create.
- Deletes become soft deletes until the server confirms.

## Phase 3: Connectivity and sync engine

- **Detect connectivity:** `@react-native-community/netinfo`. Treat "reachable" as a successful API ping, not just a connected network.
- **Triggers:** app foreground, connectivity regained, after a local write (debounced), and a periodic timer.
- **Background sync:** `expo-background-fetch` / `react-native-background-fetch` as a best effort.
- **Push phase:** process the outbox in order and retry with exponential backoff and jitter. Drop an op only on a 4xx that isn't retryable, and surface that error.
- **Pull phase:** fetch changes since the last sync cursor (`GET /notes?updated_since=`), and upsert them locally. Tombstones are needed for server-side deletes.
- **Idempotency:** send the client `op_id` or note UUID as an idempotency key so retries don't create duplicates.
- Run a single sync loop at a time (mutex) to prevent overlapping runs.

## Phase 4: Conflict resolution

- **Start simple:** last-write-wins using server timestamps, with the server as the authority.
- **Better option:** send a `version` or ETag with each update. On `409`, fetch the server copy and either:
  - auto-merge if different fields changed, or
  - mark `sync_status = conflict` and save both versions, letting the user choose.
- Decide this policy with product before building. It's the main risk area.

## Phase 5: API changes (if needed)

- Accept client-generated IDs on create.
- Add `updated_since` filtering and tombstones for deletes.
- Add versioning/ETags and return `409` on stale updates.
- Support idempotency keys.
- Optionally add a batch endpoint to reduce round trips.

## Phase 6: UX

- Show a global offline banner and a per-note sync indicator (synced, pending, conflict).
- Never block editing on network state.
- Provide a conflict resolution screen.
- Show non-intrusive error handling for failed syncs, with a manual "Sync now" action.

## Phase 7: Edge cases

- **Auth expiry while offline:** queue ops and refresh the token on reconnect. On an unrecoverable 401, keep local data and prompt re-login.
- **Logout:** clear the DB and outbox, or warn the user about unsynced changes first.
- **Migrations:** write a one-time migration that imports existing cached notes, and version the DB schema.
- **Large notes and attachments:** if attachments exist, they need a separate upload queue.
- **Clock skew:** prefer server-assigned timestamps and versions over device clocks.

## Phase 8: Testing

- **Unit:** the repo layer, op coalescing, and conflict logic.
- **Integration:** the sync engine against a mock server (MSW) with injected failures, timeouts, and duplicate deliveries.
- **Manual and E2E (Detox/Maestro):** airplane mode toggling, kill the app mid-sync, create/edit/delete offline then reconnect, and edit the same note on two devices.

## Suggested milestones

1. Local DB, repo layer, and UI refactor. The app works offline read-only, then read-write locally.
2. Outbox and push sync with retries and idempotency.
3. Pull sync with cursor and tombstones.
4. Conflict handling and UX indicators.
5. Hardening: background sync, auth and logout edge cases, E2E tests, and a staged rollout behind a feature flag.

## Open questions

- Which state and data layer do you use today?
- Can you change the API, or is it fixed?
- Is multi-device editing common (it affects how much conflict handling matters)?
- Are there attachments or only text?
- Expo or bare React Native?

Share the repo, or answer these, and I'll turn this into concrete file-level tasks.
