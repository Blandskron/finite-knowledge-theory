# exp-005: exhaustive append-only control results

## Objective

Record an exhaustive short-input check of completed-prefix preservation for the fixed-width append-only derived view.

## Background

The append-only contract predicts that all complete blocks of the pre-append source remain identical after adding a nonempty suffix. This experiment checks that statement over a finite input space as a regression control, while the algebraic argument remains the general justification.

## Hypothesis

For widths one through four, every binary source of length zero through six and every nonempty binary suffix of length one through three will preserve exactly \(\lfloor |u|/w \rfloor\) leading groups.

## Analysis

The new invariant enumerates four widths, 127 binary source sequences, and 14 nonempty binary suffixes per source, for 7,112 append transitions. Each transition reconstructs its final bytes exactly and has a common group prefix equal to the number of complete groups in the original sequence.

The suite passed on 2026-07-09. The enumeration does not prove all finite byte sequences, widths, or suffixes; it guards the finite control implementation against regressions. The decomposition \(|u|=qw+r\) from the append-only contract supplies the length-independent argument.

## Decision

Accepted.

The finite control supports the domain-qualified prefix-preservation claim. It neither upgrades the claim to universal edit locality nor authorizes a shared specification.

## Impact

Later experimental changes must retain this invariant or explicitly revise the append-only contract. The result remains scoped to the experimental functions in this research workspace.

## Next Investigation

Should the append-only contract and its exhaustive control be reviewed together as a candidate constrained conclusion?

## Status

Status: 🟢 Approved
