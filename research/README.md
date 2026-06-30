# 📓 Espacio de Investigación (research/)

Bienvenido al núcleo teórico del laboratorio. Este directorio almacena todas las investigaciones, hipótesis, pruebas matemáticas y registros de experimentos del proyecto de **Teoría del Conocimiento Finito (FKT)**.

---

## 📝 Regla de Oro Documental

Cada archivo de investigación o decisión aquí almacenado **debe seguir estrictamente** la estructura de 8 secciones definida en [docs/agent/DATA_SCHEMA.md](../docs/agent/DATA_SCHEMA.md) y apoyarse en el skill en [skills/research-document/SKILL.md](../skills/research-document/SKILL.md).

Las 8 secciones son:
1.  **Objective:** Propósito del estudio.
2.  **Background:** Estado del arte y contexto previo.
3.  **Hypothesis:** Teoría planteada bajo FKT.
4.  **Analysis:** Derivaciones, alternativas y límites matemáticos.
5.  **Decision:** Estado de la propuesta (Accepted | Rejected | Pending).
6.  **Impact:** Repercusión en la arquitectura.
7.  **Next Investigation:** Exactamente una pregunta abierta para el siguiente paso.
8.  **Status:** Estado de ciclo de vida (`🟢 Approved`, `🟡 Research`, `🔴 Rejected`).

---

## 🗺️ Fases de Investigación Activas

Las investigaciones se organizarán por subcarpetas numeradas correspondientes a las fases del roadmap:

*   `research/phase-1-primitive-definition/` - Definir qué es una primitiva fundacional (Fase activa actual).
*   `research/phase-2-levels-minimization/` - Mapear y acotar los niveles jerárquicos.
*   `research/phase-3-mathematical-finiteness/` - Demostraciones formales de finitud matemática.
*   `research/phase-4-tokenizer-design/` - Diseño lógico del tokenizador sin código.
*   `research/phase-5-experiments/` - Simulaciones en Python y validaciones numéricas.
*   `research/phase-6-tokenizer-prototype/` - Programación del prototipo base.
*   `research/phase-7-knowledge-universes/` - Modelos entrenados sobre dominios finitos.

---

## 🗄️ Archivo Histórico

Los desvíos conceptuales, ideas que resultaron incorrectas o demostraciones fallidas **no deben ser eliminadas**. Deben marcarse con `Status: 🔴 Rejected` y conservarse en este directorio como evidencia fundamental para que futuros investigadores (humanos o agentes) no tropiecen con los mismos obstáculos.
