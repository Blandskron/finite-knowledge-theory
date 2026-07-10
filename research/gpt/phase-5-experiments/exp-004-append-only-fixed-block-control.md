# exp-004: append-only fixed-block control

## Objective

Determine whether the fixed-width control has a valid locality guarantee when the admissible edit domain is restricted to appends.

## Background

Experiment 001 rejected fixed-width blocks as a universal insertion and deletion locality solution because an edit before a block boundary shifts later partitions. That counterexample does not apply to an append-only document history.

## Hypothesis

For fixed width \(w\), appending bytes preserves every complete pre-existing block; only the previous final partial block, when present, and newly added output can change.

## Analysis

For a byte sequence of length \(n=qw+r\), with \(0 \le r < w\), left-aligned fixed blocks contain \(q\) complete blocks followed by at most one partial block. Appending a sequence changes neither the first \(q\) blocks nor their boundaries. If \(r=0\), it adds blocks after them; if \(r>0\), it can replace only that last partial block and append further blocks.

The experimental case `b"abcdef"` with width four produces `(b"abcd", b"ef")`; appending `b"XY"` produces `(b"abcd", b"efXY")`. The regression assertion confirms one unchanged complete prefix group and two changed group instances under the experiment metric. Exact reconstruction and determinism are inherited from the fixed-block control.

## Decision

Accepted.

Fixed-width grouping is admissible only as a domain-qualified append-only view. It is not promoted as a universal FKT tokenizer, because arbitrary insertion and deletion remain outside this guarantee.

## Impact

Future specifications may expose append locality only when their data model formally prohibits interior edits and records width, alignment, and byte representation. They must not generalize this conditional result to mutable documents.

## Next Investigation

Can an append-only domain contract be stated independently of storage implementation and reviewed as a bounded derived-view specification?

## Status

Status: 🟢 Approved
