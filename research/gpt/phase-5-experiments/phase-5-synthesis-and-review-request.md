# Phase 5: synthesis of tokenization-locality experiments

## Objective

Consolidate the approved experimental scope from ADR-002 and state the evidence, limits, and gate for any later phase.

## Background

Phase 4 established an admissibility contract requiring a canonical representation, exact reconstruction, finite bounds, and stated edit-locality guarantees. Phase 5 then evaluated three controlled constructions and a history-independence protocol without introducing production software.

## Hypothesis

The experimental controls will distinguish properties that can coexist under the contract from properties that only appear when canonicity, boundedness, or universal locality is relaxed.

## Analysis

Experiment 001 confirms that unit octet blocks are deterministic, reconstructable, and preserve the unchanged suffix under the aligned insertion metric; the exhaustive binary-string insertion check covers all inputs of length zero through six. Fixed blocks do not retain that suffix after an unaligned insertion or deletion.

Experiment 002 confirms the predicted limitation of a classical marker-window grouping with a forced maximum: a natural marker-separated input keeps its unaffected suffix, while an adversarial marker-free input undergoes a cascading repartition after insertion.

The history-dependent grouping analysis excludes persistent local regrouping as a canonical representation when equal final bytes can expose different boundaries. The finite-radius analysis further restricts shift-invariant local boundary rules with a fixed maximum on long constant inputs.

Experiment 003 confirms the multilayer history-independence protocol as a positive control: direct construction, insertion, concatenation, and editing yield identical observable layers for equal final bytes. Its recursive midpoint hierarchy nevertheless changes globally when the final length changes, so it is not a locality solution.

## Decision

Pending Investigation.

Phase 5 establishes negative and control evidence, not an approved universal nontrivial tokenizer. The unit-octet representation remains the only universal baseline validated in this scope. Phase 6 remains blocked until a formal candidate satisfies the Phase 4 contract and receives explicit human approval.

## Impact

The laboratory can reuse the three experiments and the construction-route protocol as regression controls for later theory. No shared promotion or production implementation follows from this synthesis, and existing approved foundations remain unchanged.

## Next Investigation

Does the user approve closing Phase 5 as evidence of constraints and keeping Phase 6 blocked until a canonical nontrivial construction is formally specified?

## Status

Status: 🟡 Research
