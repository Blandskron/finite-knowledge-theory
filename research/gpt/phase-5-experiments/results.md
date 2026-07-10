# exp-001 results: tokenization locality controls

## Objective

Record the initial reproducible execution of the approved control experiment.

## Background

ADR-002 authorizes comparison of unit tokens, fixed-width blocks and delimiter grouping without promoting any grouping as universal.

## Hypothesis

The unit baseline preserves the unchanged suffix after a one-octet insertion, whereas fixed-width blocks can lose all exact shared suffix groups after the same insertion.

## Analysis

Executed on 2026-07-09 with the bundled Python runtime using `unittest` and `code/run_experiment.py`.

The initial five tests, expanded eight-test suite, and final nine-test suite passed. The expanded deterministic report was:

```text
insert/unit: before=8 after=9 prefix=1 suffix=7 changed=1
insert/fixed-4: before=2 after=3 prefix=0 suffix=0 changed=5
substitute/unit: before=8 after=8 prefix=3 suffix=4 changed=2
substitute/fixed-4: before=2 after=2 prefix=0 suffix=1 changed=2
delete/unit: before=8 after=7 prefix=2 suffix=5 changed=1
delete/fixed-4: before=2 after=2 prefix=0 suffix=0 changed=4
valid-delimiter/insert: before=2 after=2 prefix=0 suffix=1 changed=2
```

The delimiter control fell back to unit groups for the `abcdefgh` cases because those samples do not belong to its declared delimiter domain. The valid-domain insertion changed the first delimiter group and preserved the second. This is expected and confirms both the fallback and the conditional locality claim. The result is a control observation, not an estimate of average performance or a proof of a universal locality bound.

The final test exhaustively enumerated all binary inputs of lengths zero through six and every possible one-octet insertion position: 769 cases in total. In every case, unit grouping reconstructed the changed input, retained exactly the expected prefix and suffix counts, and reported one inserted group.

## Decision

Pending Investigation.

The execution supports the predicted difference between unit and fixed-width controls for the controlled inputs and closes the scope approved for `exp-001`. Its result remains pending human review before any promotion or new experiment.

## Impact

The experiment harness is now available for subsequent controlled cases without adding production code or dependencies.

## Next Investigation

¿Aprueba el usuario registrar `exp-001` como evidencia de control para planificar el siguiente experimento, sin promover todavía una agrupación universal?

## Status

Status: 🟡 Research
