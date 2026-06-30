# 🔴 FKT Official Specification (docs/specification/)

> [!WARNING]
> **ESTADO: ESPECIFICACIÓN INCOMPLETA / FALTANTE**
> 
> Siguiendo el principio core de implementación de FKT:
> *"If the specification is incomplete, stop and document the missing information. Never invent."*
> 
> **Se ha detenido la fase de desarrollo de software hasta que la especificación oficial sea provista y cargada en este directorio.**

---

## 🔍 Diagnóstico de la Especificación

Para poder iniciar la **Fase 3 (Diseño de la Arquitectura)** y la **Fase 4 (Implementación de Referencia en Python)**, se requiere la definición formal y matemática de los siguientes componentes teóricos de la **Teoría del Conocimiento Finito (FKT)**:

### 1. Primitivas Fundamentales (Foundational Primitives)
*   **Información Requerida:** 
    *   ¿Cuál es el conjunto exacto de primitivas atómicas? (ej. bytes individuales `0x00-0xFF`, caracteres Unicode básicos u otra representación discrete).
    *   ¿Cuáles son las reglas algebraicas que garantizan que el conjunto de primitivas es acotado, numerable y estable?

### 2. Niveles Fundamentales (Foundational Levels)
*   **Información Requerida:**
    *   La jerarquía exacta de niveles (ej. Nivel 1: Primitivas, Nivel 2: Composiciones, Nivel 3: Estructuras Sintácticas).
    *   Las reglas de transición y composición que permiten construir el Nivel $N$ a partir del Nivel $N-1$ de forma determinista.
    *   Límites de crecimiento de cada nivel.

### 3. Algoritmo del Tokenizador Teórico
*   **Información Requerida:**
    *   La especificación formal del proceso de tokenización (decomposición de texto/código a la jerarquía finita).
    *   ¿Cómo se resuelve la ambigüedad en la composición (ej. algoritmo codicioso, optimización de entropía de Shannon, etc.)?
    *   Criterios de estabilidad: garantizar que cambios pequeños en la entrada no causen reestructuraciones masivas del árbol de composición.

### 4. Vectores de Prueba y Validación (Validation Suite Specs)
*   **Información Requerida:**
    *   Conjuntos de datos mínimos de prueba (cadenas de entrada) y sus decomposiciones exactas esperadas (secuencia de tokens e identificadores).
    *   Formato de serialización oficial para los tokens y el diccionario de composiciones.

---

## 🚦 Próximos Pasos

1.  **Carga de Documentos:** El usuario debe proveer o crear los documentos teóricos aprobados de las fases de investigación (Fases 1 a 4) bajo este directorio (`docs/specification/`).
2.  **Validación de Especificación:** Una vez cargados, el agente validará la especificación contra los 6 principios de implementación.
3.  **Inicio de Arquitectura:** Tras validar la completitud de la teoría, se procederá al diseño de los módulos en `docs/architecture/`.
