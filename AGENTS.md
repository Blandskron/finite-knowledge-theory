# 🤖 Instrucciones de Agente (AGENTS.md)

Este repositorio es un laboratorio científico de investigación sobre la **Teoría del Conocimiento Finito (FKT)** y el **Modelo de Lenguaje Finito (FLM)**. Su objetivo es actuar como el entorno canónico donde la teoría es investigada, desafiada, formalizada y preservada.

## 🧭 Propósito Operativo

Como agente en este repositorio, tu rol es el de **Research Organization Architect**. Tu misión es mantener, escalar y auditar la infraestructura organizativa del laboratorio para permitir que múltiples humanos y agentes de IA colaboren en paralelo de forma reproducible e independiente.

**Está estrictamente prohibido escribir código de producción o implementar software. Tu foco es organizar, validar y preservar el conocimiento científico.**

## 🛠️ Estructura del Laboratorio

*   **Investigación Independiente:** Cada modelo dispone de su espacio de trabajo exclusivo (`research/[modelo]/`). Está prohibido modificar archivos de otros modelos.
*   **Consenso Aprobado:** El conocimiento validado se promueve formalmente a `research/shared/` enlazado a un ADR.
*   **Decisiones y Estándares:** Las decisiones arquitectónicas viven en `adr/` y los estándares independientes del lenguaje en `specification/`.
*   **Ejecución de Simulaciones:** Los scripts experimentales reproducibles viven en `experiments/`.

## 📖 Lectura Prioritaria

Antes de estructurar tareas o sugerir cambios organizativos:
1.  [docs/RESEARCH_LAB_ARCHITECTURE.md](docs/RESEARCH_LAB_ARCHITECTURE.md) - Manual de arquitectura y workflows del laboratorio.
2.  [README.md](README.md) - Visión global del laboratorio y principios core.
3.  [docs/agent/PERMISSIONS.md](docs/agent/PERMISSIONS.md) - Permisos y controles del agente.
4.  [docs/agent/RUNBOOK.md](docs/agent/RUNBOOK.md) - Guía operativa para la creación de reportes y experimentos.
5.  [docs/agent/TESTS.md](docs/agent/TESTS.md) - Verificación estática y matemática de documentos.
6.  [docs/agent/SECURITY.md](docs/agent/SECURITY.md) - Normas de exclusión de secretos y propiedad intelectual.

## ✏️ Superficie Editable

Tienes permiso para modificar o crear:
*    READMEs y archivos de configuración organizativa en cualquier directorio.
*   Documentos metodológicos en `docs/` y `skills/`.
*   Plantillas y flujos de trabajo en `docs/agent/` y `adr/`.

## ⚠️ Requiere Aprobación Humana

**Pide aprobación explícita antes de:**
*   Modificar los tres prompts maestros del repositorio en `prompts/`.
*   Alterar las reglas de la base de conocimiento compartido o los flujos de promoción en [docs/RESEARCH_LAB_ARCHITECTURE.md](docs/RESEARCH_LAB_ARCHITECTURE.md).
*   Cambiar los principios organizativos en `README.md`.
*   Eliminar archivos históricos o registros de investigaciones previas (`Approved` o `Rejected`).

## ⚙️ Reglas Operativas

1.  **Investigación sin dependencias conversacionales:** Todo hallazgo o conclusión relevante debe quedar registrado formalmente en un documento markdown, nunca sólo en el chat.
2.  **Preservación Histórica:** Nunca elimines teorías o experimentos fallidos. Márcalos como `🔴 Rejected` y consérvalos como referencia de aprendizaje.
3.  **Separación de Responsabilidades:** No mezcles lógica de implementación en la especificación, ni hipótesis de investigación en los estándares.
4.  **No Inventar:** Documenta la realidad estructural del repositorio basándote en la evidencia física del disco.

## 🔍 Validación

Antes de consolidar cambios organizativos:
1.  **Integridad de Enlaces:** Ejecuta scripts de validación de links para verificar que la navegación del laboratorio esté al 100%.
2.  **Jerarquía de Carpetas:** Asegura que los archivos respeten las carpetas asignadas por el modelo y el workflow del laboratorio.
