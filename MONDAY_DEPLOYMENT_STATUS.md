# Monday Master Plan Deployment Status

**Status:** PENDING LIVE VERIFICATION
**Target board:** `useSafeWeb.com` (`5102978580`)
**Board hierarchy:** `multi_level`
**API version:** `2026-07`

## Verified live evidence

- Authentication succeeded as monday user `61670350`.
- Target board was verified as `multi_level`.
- The board initially contained 4 active test/default items under one top-level root.
- Reset was explicitly confirmed with `RESET 5102978580`.
- The root was deleted and the board was re-queried with `0 active items` remaining.
- v2 schema creation failed at the first Status capability attempt because the live schema rejected `StatusCalculatedFunction.NONE`.
- v3 resumed successfully and created/reused the ordinary schema through `Notes` before the final Status-column creation returned `INTERNAL_SERVER_ERROR`.

## Root-cause correction for v4

monday's current Status API documentation states that the numeric color ID also serves as the status-label ID, so each color can be used only once inside a Status column. The v3 `Plan Status` definition reused `bright_blue` and `working_orange`, violating that constraint. v4 assigns nine unique colors to the nine `Plan Status` labels.

v4 also removes reliance on the failing typed Status-creation path:

- Status/Priority/Risk are created with the independently documented generic `create_column(column_type: status)` mutation.
- Custom label settings are supplied through `defaults` using monday's current Status settings schema.
- If custom defaults are rejected, the deployer re-queries the deterministic column ID, creates a base Status column only if still absent, then seeds missing labels using `change_simple_column_value(... create_labels_if_missing:true)` on a temporary leaf item.
- The temporary item is deleted and the board must verify as empty before the hierarchy import starts.
- Multi-level Status/Priority/Risk keep monday's default rollup behavior; parent rows omit native rollup values during `ingest_items` while exact source values remain preserved in dedicated text columns.

## Offline verification for v4

- 743 WBS items.
- 5 hierarchy levels.
- 975 dependency edges.
- 243 parent items receive blank native rollup-status cells during ingest.
- 500 leaf items receive native Status/Priority/Risk values.
- Exact Status/Priority/Risk source values remain preserved on all 743 rows.
- All required label names are <=30 characters.
- Every Status column now uses unique color IDs.
- Test suite: 11/11 passing.
- Deployment ZIP SHA-256: `c40b6443c254c21632d1f23b37778498192706dc9a9b7312edbe00fae04576fe`.

The deployment must not be marked complete until v4 reaches `DEPLOYMENT COMPLETE` and `output/monday_deployment_verification.json` confirms the 743-item hierarchy and 975 dependency edges.