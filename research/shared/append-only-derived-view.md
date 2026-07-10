---
original_research: "file:///research/gpt/phase-5-experiments/append-only-derived-view-contract.md"
adr_reference: "file:///adr/ADR-003-append-only-derived-view.md"
approved_by: "Human User"
date: "2026-07-09"
justification: "Aprobación explícita de la conclusión restringida: los bloques fijos preservan los bloques completos previos únicamente para extensiones append-only, con evidencia experimental y trazabilidad contractual."
---

# Vista derivada append-only

## Consensus

Para una secuencia canónica de octetos y un ancho público \(w \ge 1\), la partición fija alineada al inicio se acepta como vista derivada para un historial append-only. Una extensión conserva todos los bloques completos preexistentes y puede modificar, como máximo, el bloque parcial final anterior.

## Scope

La garantía exige transiciones de la forma \(u' = u \mathbin{\|} a\). No cubre inserción, borrado, sustitución, reordenamiento ni cambios de parámetros. No constituye un tokenizador universal ni una implementación de producción.

## Traceability

La decisión formal es [ADR-003](../../adr/ADR-003-append-only-derived-view.md). La evidencia incluye los controles `exp-004` y `exp-005` y su matriz de trazabilidad en la investigación GPT.
