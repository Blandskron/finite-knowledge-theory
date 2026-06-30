# 🗄️ Esquema de Datos y Contratos (DATA_SCHEMA.md)

Este documento detalla el esquema conceptual de las entidades de la Teoría del Conocimiento Finito (FKT) y el contrato de formato para los reportes del laboratorio.

---

## 1. Contrato de Documentación de Investigación

Todos los reportes de investigación en la carpeta `research/` deben seguir de forma estricta la estructura de 8 secciones que se detalla a continuación. Este esquema garantiza la consistencia del laboratorio para humanos y agentes.

### Estructura Requerida de Archivos

```markdown
# [Descripción del Objetivo / Título de la Investigación]

## Objective
[¿Qué problema teórico o práctico estamos resolviendo en esta investigación?]

## Background
[¿Qué se conoce actualmente sobre este problema? ¿Cómo lo resuelven las arquitecturas tradicionales?]

## Hypothesis
[La hipótesis o teoría propuesta para este problema bajo la filosofía FKT.]

## Analysis
[Análisis técnico profundo, matemáticas aplicadas, alternativas consideradas, limitaciones y riesgos.]

## Decision
[Accepted | Rejected | Pending Investigation]
[Justificación detallada de la decisión tomada.]

## Impact
[¿Cómo afecta esta decisión a la arquitectura global del FKT y las fases posteriores?]

## Next Investigation
[Exactamente una pregunta para la siguiente investigación. Ni más, ni menos.]

## Status
[🟢 Approved | 🟡 Research | 🔴 Rejected]
```

---

## 2. Entidades Conceptuales de FKT (Draft Inicial)

A medida que avance la investigación, estas entidades se formalizarán en código.

### A. Primitiva Fundacional (Foundational Primitive)
La unidad atómica indivisible del conocimiento.
*   **Propiedades obligatorias:**
    *   *Finitud:* El conjunto completo de primitivas es acotado y numerable.
    *   *Estabilidad:* Las primitivas no cambian ni se expanden dinámicamente con nuevos datos.
    *   *Determinismo:* La interpretación de una primitiva es única y predecible.

### B. Nivel Fundacional (Foundational Level)
Un estrato de la jerarquía de conocimiento.
*   **Propiedades:**
    *   Cada nivel superior se compone estrictamente de combinaciones ordenadas del nivel inmediatamente inferior.
    *   La cantidad de niveles debe ser el mínimo matemáticamente posible (a determinar en la Fase 2).

### C. Universo de Conocimiento (Knowledge Universe)
Una base de datos de conocimiento especializada (ej. Código Penal, Django) expresada como un grafo o secuencia composible de primitivas fundacionales.
*   **Propiedades:**
    *   No introduce primitivas nuevas; solo define relaciones de composición específicas sobre la fundación finita.
