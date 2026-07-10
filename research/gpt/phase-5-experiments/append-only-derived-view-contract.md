# Append-only derived-view contract

## Objective

Specify a bounded, canonical derived-view contract for append-only byte histories without prescribing storage, mutation mechanisms, or production code.

## Background

The strict-locality contract from Phase 4 evaluates universal edit classes. Experiment 004 shows that a left-aligned fixed-width view instead has a bounded update property when the only permitted transition is appending a finite byte suffix.

## Hypothesis

An append-only contract can state canonicity, reconstruction, finite bounds, and a constant update region while making its restriction to append transitions explicit.

## Analysis

Let the canonical source be the finite octet sequence \(u\). A conforming history is a sequence \(u_0, u_1, \ldots\) in which every transition has the form \(u_{t+1}=u_t \mathbin{\|} a_t\) for a finite suffix \(a_t\). Interior insertion, deletion, substitution, reordering, and parameter changes are outside the domain.

For a public integer width \(w \ge 1\), the derived view partitions each final \(u_t\) left-to-right into contiguous nonempty intervals of length at most \(w\). It is a pure function of \(u_t\) and \(w\); its concatenated intervals reconstruct \(u_t\) exactly. The maximum interval size is \(w\), and the view may have no reduction on short or adversarial inputs.

If \(|u_t|=qw+r\) with \(0 \le r < w\), appending affects no interval among the first \(q\) complete intervals. It replaces at most the single prior partial interval and adds intervals for the suffix. Therefore the pre-existing update region is bounded by one interval, independently of document length. This is a prefix-preservation bound, not the bidirectional suffix-locality metric used for arbitrary edits.

## Decision

Accepted.

The contract is a candidate description of a bounded derived view under an append-only domain. It does not alter the universal Phase 4 contract, does not authorize a tokenizer for mutable documents, and does not create an implementation requirement.

## Impact

The laboratory can distinguish a correct conditional guarantee from an invalid universal claim. Any later adoption must publish the source representation, width, alignment origin, permitted transition relation, reconstruction rule, and the exact one-interval pre-existing update bound.

## Next Investigation

Should the append-only contract be submitted for human review as a separate domain-qualified research conclusion?

## Status

Status: 🟢 Approved
