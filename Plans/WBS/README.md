# Authoritative Executable WBS

`master-wbs.csv` is the authoritative executable task register migrated from source Section 6.7.4. It preserves the original task IDs and every source field.

Hierarchy is deterministic through `Parent_ID`, `Phase_ID`, `Deliverable_ID`, `Work_Package_ID`, `Package_ID`, and `Lifecycle_Stage`. Structured phase/deliverable/work-package definitions remain authoritative in the linked registers; task dependencies and execution metadata remain authoritative in the CSV.
