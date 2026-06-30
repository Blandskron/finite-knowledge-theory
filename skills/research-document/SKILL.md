---
name: research-document
description: Generar y validar documentos de investigación y decisiones teóricas siguiendo el formato estricto de 8 secciones de FKT.
---

# Skill: Research Document Generation & Audit

Usa esta skill cuando debas abrir una nueva investigación, documentar una propuesta teórica o registrar una decisión arquitectónica en el directorio `research/`.

## 📥 Entradas

*   **Identificación del Problema:** El objetivo o fase correspondiente del roadmap.
*   **Contenido Técnico:** La hipótesis, derivaciones matemáticas o análisis de alternativas.
*   **Propuesta de Decisión:** accepted, rejected o pending investigation, con su justificación.
*   **Pregunta Futura:** Exactamente una pregunta para la siguiente línea de investigación.

## 📝 Procedimiento de Generación

1.  **Ubicación Correcta:** Elige la subcarpeta adecuada en `research/` (ej. `research/phase-1-primitive-definition/`).
2.  **Estructura Obligatoria:** Escribe el documento respetando exactamente las 8 secciones definidas en [DATA_SCHEMA.md](../../docs/agent/DATA_SCHEMA.md):
    *   `# [Título]`
    *   `## Objective`
    *   `## Background`
    *   `## Hypothesis`
    *   `## Analysis`
    *   `## Decision`
    *   `## Impact`
    *   `## Next Investigation`
    *   `## Status`
3.  **Restricción de Pregunta Única:** En la sección `Next Investigation`, formula una única pregunta concisa y clara. Está prohibido listar múltiples preguntas.
4.  **Marcado de Status:** Indica el status al final usando los badges:
    *   `Status: 🟢 Approved` (Aprobado por el usuario).
    *   `Status: 🟡 Research` (Investigación activa o propuesta pendiente).
    *   `Status: 🔴 Rejected` (Hipótesis descartada o rechazada).

## 🔍 Procedimiento de Validación

Antes de guardar el archivo, verifica:

1.  **Conteo de Secciones:** Confirma que las 8 cabeceras de sección (`##`) estén presentes con el nombre exacto en inglés.
2.  **Límite de Preguntas:** Asegura que la sección `Next Investigation` contenga exactamente una sola pregunta terminada en `?`.
3.  **Consistencia de Status:** Si la decisión es `Accepted`, el status final debe ser `Approved 🟢` (siempre que el usuario haya dado su consentimiento explícito). Si la decisión es `Pending Investigation`, el status debe ser `Research 🟡`.
4.  **Integridad de Enlaces:** Si enlazas a otros documentos teóricos o al README, comprueba que las rutas relativas sean correctas.
