---
original_research: "file:///research/gpt/phase-4-tokenizer-design/phase-4-synthesis-and-phase-5-proposal.md"
adr_reference: "file:///adr/ADR-002-phase-5-tokenization-locality-experiment.md"
approved_by: "Human User"
date: "2026-07-09"
justification: "Aprobación explícita para usar τ1 como baseline experimental y abrir el experimento aislado de Fase 5."
---

# Baseline experimental de tokenización de Fase 4

## Consensus

El tokenizador unitario \(\tau_1\) es el baseline experimental canónico por ser determinista, reversible y local bajo las métricas investigadas. Las agrupaciones superiores son vistas derivadas: no redefinen las primitivas ni se aceptan como universales.

## Scope

Se autoriza el experimento aislado `exp-001-tokenization-locality` para comparar \(\tau_1\), \(\tau_M\) y \(A_P\). Este consenso no es una especificación ni una implementación de producción.

## Traceability

La decisión formal es [ADR-002](../../adr/ADR-002-phase-5-tokenization-locality-experiment.md).
