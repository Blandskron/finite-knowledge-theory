---
original_research:
  - "file:///research/gpt/phase-1-primitive-definition/octet-foundation-hypothesis.md"
  - "file:///research/gpt/phase-2-levels-minimization/finite-levels-unbounded-documents.md"
  - "file:///research/gpt/phase-3-mathematical-finiteness/bounded-block-grammar-finiteness.md"
adr_reference: "file:///adr/ADR-001-octet-foundation-and-bounded-block-grammar.md"
approved_by: "Human User"
date: "2026-07-09"
justification: "Aprobación explícita del usuario tras investigación matemática de Fases 1 a 3."
---

# Fundación de octetos y gramática de bloques acotados

## Consensus

FKT adopta provisionalmente el conjunto \(B = \{0, \ldots, 255\}\) como una capa fundacional de representación. La finitud se atribuye al alfabeto, a los tipos de composición y a los niveles definidos, no al conjunto de documentos, que puede ser ilimitado en cantidad y longitud.

Una gramática de bloques de longitud explícita, parametrizada por \(1 \leq M \leq 255\), demuestra que un conjunto finito de tipos puede segmentar y reconstruir deterministamente cualquier secuencia finita de octetos. Cada bloque contiene una cabecera de longitud y una carga de hasta \(M\) octetos; un documento es una secuencia ordenada de bloques.

## Scope and limits

Este consenso no fija el valor de \(M\), no asigna semántica a los octetos o bloques, no garantiza estabilidad de edición local y no autoriza implementación de producción. Esas cuestiones continúan en la Fase 4.

## Traceability

La decisión formal es [ADR-001](../../adr/ADR-001-octet-foundation-and-bounded-block-grammar.md). La evidencia original permanece en los tres informes de investigación GPT referenciados en el frontmatter.
