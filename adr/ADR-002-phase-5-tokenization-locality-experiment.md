# ADR-002: Experimento de localidad de tokenización en Fase 5

## Status

Accepted — 2026-07-09

## Context

La Fase 4 definió un baseline unitario reversible, métricas de localidad y límites de agrupaciones fijas o clásicas. Se requiere evidencia experimental reproducible antes de considerar cualquier diseño adicional.

## Decision

Se autoriza exclusivamente el experimento GPT `exp-001-tokenization-locality` bajo `research/gpt/phase-5-experiments/`. Comparará tokens unitarios \(\tau_1\), bloques fijos \(\tau_M\) y agrupación delimitada \(A_P\), usando Python y la biblioteca estándar. El experimento medirá reconstrucción, determinismo, tamaño máximo, reducción de elementos y daño de grupos tras ediciones.

## Consequences

Esta decisión no crea una especificación, una API ni una implementación de referencia. No adopta una agrupación no trivial como universal. Los resultados deben documentarse y revisarse antes de cualquier promoción adicional.

## Evidence

- [Síntesis de Fase 4](../research/gpt/phase-4-tokenizer-design/phase-4-synthesis-and-phase-5-proposal.md)
- [Contrato de localidad estricta](../research/gpt/phase-4-tokenizer-design/strict-locality-admissibility-contract.md)
