# Authoritative Executable WBS

`master-wbs.csv` is the authoritative executable task register migrated from source Section 6.7.4. It preserves the original task IDs and every source field.

Hierarchy is deterministic through `Parent_ID`, `Package_ID`, `Lifecycle_Stage`, and any retained `Phase_ID`, `Deliverable_ID`, or `Work_Package_ID`. Intermediate phase/deliverable/work-package levels are optional: retain them only when they group multiple related children or carry an independent lifecycle, gate, traceability, authority, risk, recovery, waiting/blocking, interface, or acceptance function. `Parent_ID` always points to the nearest retained governed ancestor; blank intermediate-ID cells mean that layer was intentionally normalized away. Structured retained phase/deliverable/work-package definitions remain authoritative in the linked registers; task dependencies and execution metadata remain authoritative in the CSV.
