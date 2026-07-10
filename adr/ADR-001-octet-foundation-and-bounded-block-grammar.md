# ADR-001: Fundación de octetos y gramática de bloques acotados

## Status

Accepted — 2026-07-09

## Context

FKT necesita una base de representación finita, estable y determinista antes de definir un tokenizador teórico. La investigación GPT evaluó los octetos, la diferencia entre tipos finitos y documentos no acotados, y una gramática de bloques con longitud explícita.

## Decision

Se adopta, para la investigación posterior, el conjunto de octetos \(B = \{0, \ldots, 255\}\) como capa fundacional candidata de representación. Se acepta que la finitud se refiere a primitivas, tipos y niveles, no al conjunto de documentos. Se acepta como construcción matemática de referencia una gramática parametrizada por \(1 \leq M \leq 255\), cuyos bloques contienen una cabecera de longitud y una carga de hasta \(M\) octetos.

Esta decisión no fija \(M\), no define semántica, no establece un vocabulario aprendido y no autoriza software de producción.

## Consequences

Las fases siguientes pueden diseñar y contrastar reglas de segmentación sobre esta base. Toda especificación futura deberá diferenciar con precisión la gramática finita de la secuencia de documentos potencialmente no acotada. Cualquier cambio a esta base requiere un ADR posterior.

## Evidence

- [Fase 1: hipótesis de los octetos](../research/gpt/phase-1-primitive-definition/octet-foundation-hypothesis.md)
- [Fase 2: niveles finitos y documentos no acotados](../research/gpt/phase-2-levels-minimization/finite-levels-unbounded-documents.md)
- [Fase 3: finitud de gramática de bloques](../research/gpt/phase-3-mathematical-finiteness/bounded-block-grammar-finiteness.md)
