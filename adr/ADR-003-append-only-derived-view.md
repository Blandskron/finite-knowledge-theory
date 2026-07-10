# ADR-003: Vista derivada de bloques para dominio append-only

## Status

Accepted — 2026-07-09

## Context

La Fase 5 confirmó que los bloques fijos no preservan localidad ante inserciones o borrados internos. También demostró que, con una secuencia canónica de octetos y transiciones exclusivamente de extensión, los bloques completos anteriores permanecen sin cambios.

## Decision

Se acepta una conclusión restringida: una vista derivada canónica de bloques fijos, parametrizada por un ancho público \(w \ge 1\) y alineada al inicio, es admisible para historiales append-only. En cada extensión, conserva todos los bloques completos preexistentes y puede modificar como máximo un bloque parcial previo.

La fuente canónica sigue siendo la secuencia de octetos. Esta decisión no adopta bloques fijos como tokenizador universal y no autoriza software de producción.

## Consequences

Las especificaciones o experimentos futuros pueden referir esta garantía solo si declaran expresamente el dominio append-only, el ancho y la alineación. Inserción, borrado, sustitución, reordenamiento y cambios de parámetros están excluidos. La pregunta de una agrupación canónica no trivial con localidad estricta para documentos mutables permanece abierta; la Fase 6 no se abre con esta decisión.

## Evidence

- [Control append-only](../research/gpt/phase-5-experiments/exp-004-append-only-fixed-block-control.md)
- [Contrato de vista derivada](../research/gpt/phase-5-experiments/append-only-derived-view-contract.md)
- [Control exhaustivo](../research/gpt/phase-5-experiments/exp-005-append-only-exhaustive-results.md)
- [Matriz de trazabilidad](../research/gpt/phase-5-experiments/append-only-contract-traceability-matrix.md)
