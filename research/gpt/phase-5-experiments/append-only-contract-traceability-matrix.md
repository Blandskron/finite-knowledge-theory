# Append-only contract traceability matrix

## Objective

Provide a review-ready mapping from the append-only candidate to each Phase 4 admissibility obligation and its supporting evidence.

## Background

The append-only contract and experiments 004 and 005 establish a conditional fixed-width derived view. A concise trace is needed to prevent that conditional result from being mistaken for compliance with the universal mutable-document contract.

## Hypothesis

The candidate satisfies the structural clauses of the Phase 4 contract only after replacing its universal edit domain with an explicitly restricted append-only transition relation.

## Analysis

| Phase 4 obligation | Append-only candidate evidence | Scope outcome |
| --- | --- | --- |
| Domain | Finite octet histories with transitions \(u_{t+1}=u_t \mathbin{\|} a_t\) | Satisfied only for append-only histories |
| Parameters | Public finite width \(w \ge 1\) and left alignment | Satisfied |
| Canonicity | Fixed left-to-right partition is a pure function of final bytes and width | Satisfied |
| Reconstruction | Concatenation of nonempty contiguous groups returns the source bytes | Satisfied by experiment controls |
| Bounds | Every group has length from one through \(w\) | Satisfied |
| Locality | At most one pre-existing partial group changes; completed prefix remains unchanged | Satisfied only for append transitions |

Experiment 004 supplies the direct representative control. Experiment 005 checks 7,112 finite append transitions and confirms the completed-prefix count \(\lfloor |u|/w \rfloor\) for widths one through four. The Phase 4 universal domain requires arbitrary permitted edits; the candidate fails that broader locality criterion under interior insertion and deletion, as experiment 001 records.

## Decision

Accepted.

The candidate is traceable as a domain-qualified derived view and is not traceable as a universal strict-locality tokenizer. No ADR, shared promotion, or implementation follows from this matrix.

## Impact

Human review can approve, reject, or refine one narrow claim without reopening settled counterexamples for mutable documents. Any future proposal must state whether it claims the restricted append-only row or the universal Phase 4 row.

## Next Investigation

Should a human reviewer accept the append-only derived-view claim as a restricted conclusion while retaining the universal tokenizer question as unresolved?

## Status

Status: 🟢 Approved
