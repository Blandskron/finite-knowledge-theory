# 🧪 Pruebas y Validación (TESTS.md)

Este documento especifica cómo verificar la integridad y corrección tanto de la documentación de investigación como del código experimental del laboratorio.

---

## 1. Verificación Documental (Estática)

Cada vez que se modifique o añada documentación o reportes en `research/`:

*   **Validación de Estructura:** Comprueba que todos los documentos de decisión contengan las 8 secciones del estándar FKT:
    1.  Objective
    2.  Background
    3.  Hypothesis
    4.  Analysis
    5.  Decision
    6.  Impact
    7.  Next Investigation
    8.  Status
*   **Validación de Enlaces:** Todos los enlaces relativos (ej. un enlace apuntando a `../../archivo.md`) deben resolver a archivos existentes en el repositorio.
*   **Formato de Código:** Asegura que los bloques de código y las fórmulas matemáticas en LaTeX estén correctamente formados y cerrados.

---

## 2. Validación Teórica y Matemática

Para reportes teóricos y demostraciones (Fases 1 a 4):

*   **Verificación de Primeros Principios:** Revisa que las afirmaciones matemáticas (ej. teoremas de finitud, cálculos de entropía de la información, límites asintóticos) no contengan errores de lógica formal.
*   **Comprobación Doble:** Si el agente realiza una derivación matemática larga, debe escribir un script en Python (guardado en `research/scratch/`) que verifique numéricamente los resultados (ej. tamaños de conjuntos, combinatorias) para aportar evidencia sólida.

---

## 3. Validación Experimental (Fases 5+)

Cuando se introduzca código y prototipos (ej. el primer tokenizador):

*   **Suite de Pruebas:** Todos los experimentos deben contar con pruebas unitarias que verifiquen el comportamiento determinista y composible de las primitivas.
*   **Ejecución de Tests:** Si se usa Python, ejecuta la suite con:
    ```bash
    pytest research/phase-5-experiments/tests/
    ```
*   **Regla de Integridad de Tests:** Está **estrictamente prohibido** omitir, deshabilitar o relajar pruebas unitarias para forzar la aprobación de un cambio. Si un test falla, la teoría o la implementación están rotas y deben revisarse.
