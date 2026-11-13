<!-- Q: Write an implementation plan for adding offline support to our React Native notes app. Notes sync to a REST API. -->

**Recommendation: make the local database the source of truth, and have the UI read and write only to it.** A background sync engine pushes queued changes to the REST API and pulls remote changes. I haven't seen your code, so I assume React Native with a REST API that has no sync endpoints yet. Check the API assumptions in Phase 0 first, because they decide the rest.

## Key decisions

| Decision | Choice | Why |
|---|---|---|
| Local store | SQLite (`expo-sqlite` or `op-sqlite`) | Queryable, transactional, survives app kills. AsyncStorage can't do atomic multi-row writes. |
| Write path | Outbox table of pending operations | Edits made offline survive restarts and replay in order. |
| IDs | Client-generated UUIDs | Notes can be created offline without waiting for a server ID. |
| Conflicts | Last-write-wins per note, using a server `version` | Simple. Switch to field-level merge or a conflict copy if users edit one note on two devices. |

## Phases

**Phase 0: API readiness (backend, blocks everything)**
1. Accept client UUIDs on `POST /notes`, and make creates idempotent (an `Idempotency-Key` header or upsert by ID).
2. Return `version` or `updated_at` on every note. Reject stale updates with `409`.
3. Soft-delete with tombstones, so deletions reach other devices.
4. Add `GET /notes?since=<cursor>` for delta pulls, including tombstones.

**Phase 1: Local database**
1. Add a `notes` table with `id`, `title`, `body`, `updated_at`, `server_version`, `deleted`, and `sync_state` (`synced | dirty | conflict`).
2. Add an `outbox` table with `op_id`, `note_id`, `type` (`create | update | delete`), `payload`, `attempts`, and `created_at`.
3. Put a repository layer (`NotesRepo`) in front of it. Screens call it instead of the API client.
4. Migrate existing in-memory or cached notes into SQLite on first launch.

**Phase 2: Write path**
1. Each user edit runs in one transaction: update the `notes` row and append to the `outbox`.
2. Coalesce operations in the outbox. For example, several updates to one note become one, and create followed by delete cancels out.
3. The UI updates immediately from local data, with no spinner waiting on the network.

**Phase 3: Sync engine**
1. Add a `SyncService` that runs on app foreground, on reconnect (`@react-native-community/netinfo`), after local writes (debounced), and on a timer.
2. Push: drain the outbox in order. Retry network errors and `5xx` with exponential backoff. Treat `4xx` as permanent and mark that note `conflict` or failed.
3. Pull: fetch `since=<cursor>`, apply changes in one transaction, then store the new cursor. Skip any note that is `dirty` locally and resolve it per the conflict rule.
4. Allow only one sync at a time (a mutex), or two concurrent runs will double-send.

**Phase 4: Conflicts and UI**
1. On `409`, refetch the server copy. Apply last-write-wins, or keep both as a "conflict copy" if data loss matters more than tidiness.
2. Add a small status indicator per note or in the header: offline, syncing, or failed (with retry).
3. Don't block the app when offline. Show a banner only.

**Phase 5: Testing and rollout**
1. Unit-test the outbox coalescing and the pull-merge logic. This is where bugs hide.
2. Integration-test with a mocked API that drops, delays, and returns `409`.
3. Test manually in airplane mode: create, edit, and delete offline, kill the app, reconnect, and check the server.
4. Put it behind a feature flag and roll it out gradually.

## Risks
- **Clock skew:** use server `version`, not device timestamps, to decide who wins.
- **Auth expiry while offline:** a `401` during a push must pause the sync and keep the outbox. It must not drop operations.
- **Attachments or images:** if notes have them, they need a separate upload queue. I left them out of this plan.

**Next step:** tell me whether the API can support Phase 0. If you share the repo, I'll check which data and networking libraries you already use and turn Phases 1 and 2 into concrete file-level tasks.
