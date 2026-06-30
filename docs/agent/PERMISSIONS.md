# 🔐 Permisos del Agente (PERMISSIONS.md)

Este documento detalla los permisos concedidos al agente de IA en este repositorio y los límites estrictos que requieren supervisión humana.

---

## 1. Permisos de Modificación (Escritura Libre)

El agente tiene permitido crear o modificar los siguientes archivos durante la investigación:

*   **Reportes de Investigación:** Todos los documentos y archivos markdown dentro de la carpeta `research/` (ej. bitácoras de fase, derivaciones matemáticas, análisis de datos).
*   **Archivos Temporales:** Scripts de prueba, simulaciones cortas o cuadernos en `research/scratch/` o equivalentes dentro del workspace.
*   **Documentación de Soporte:** Actualización de guías secundarias en `docs/` (como glosarios, listas de referencias académicas).
*   **Historial:** `docs/CHANGELOG.md` para registrar el progreso y versiones de los documentos.

---

## 2. Acciones que Requieren Aprobación Humana

Las siguientes operaciones son altamente sensibles y **no deben realizarse** sin la confirmación previa y explícita del usuario:

*   **Principios Fundamentales:** Modificar las directivas core o los **Cinco Principios Inmutables** en [README.md](../../README.md) o [AGENTS.md](../../AGENTS.md).
*   **Roadmap de Investigación:** Alterar la secuencia de las fases del Roadmap o dar por aprobada una fase sin revisión humana de la evidencia.
*   **Eliminación de Historial Teórico:** Eliminar o archivar documentos de investigación antiguos en `research/` (es vital conservar los fallos y desvíos conceptuales como parte del aprendizaje del laboratorio).
*   **Cualquier código de producción:** Escribir código destinado a la base de la biblioteca del tokenizador o del modelo de lenguaje (Fase 6+), a menos que sea una simulación puramente experimental en `scratch/`.
*   **Cambios en Políticas de Seguridad:** Modificar este archivo (`PERMISSIONS.md`) o las directrices de [SECURITY.md](SECURITY.md).

---

## 3. Acciones Prohibidas

Bajo ninguna circunstancia el agente debe realizar las siguientes acciones:

*   **Exposición de Credenciales:** Escribir o conservar secretos, tokens o API keys reales en archivos bajo control de versiones (ej. `.env` con claves de producción).
*   **Alteración de Git:** Ejecutar comandos de Git destructivos como `git push --force` o reescribir ramas compartidas que puedan causar pérdida de trabajo.
*   **Salto de Fases:** Empezar a programar el tokenizador o modelo antes de que las fases teóricas previas estén marcadas como `Approved 🟢`.
