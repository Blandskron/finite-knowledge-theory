# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.4.0] - 2026-06-29

### Added
- **Arquitectura de Laboratorio Científico:** Restructurados todos los dominios de investigación a nivel raíz (`specification/`, `reference-implementation/`, `validation/`, `prompts/`, `adr/`, `experiments/`, `benchmarks/`, `examples/`, `scripts/`).
- **Manual de Arquitectura:** Creado el manual maestro [docs/RESEARCH_LAB_ARCHITECTURE.md](RESEARCH_LAB_ARCHITECTURE.md) cubriendo los 10 entregables metodológicos del laboratorio.
- **Aislamiento Multi-Agente:** Creados los subdirectorios de investigación aislada en `research/` (`gpt/`, `claude/`, `gemini/`, `deepseek/`, `future-models/`, `shared/`) junto con sus respectivas pautas operativas.

### Changed
- **Directrices de Agente:** Actualizado `AGENTS.md` adaptándolo al rol de **Research Organization Architect** y definiendo los límites de infraestructura y flujos de promoción.
- **Presentación del Proyecto:** Actualizado `README.md` detallando la estructura modular del laboratorio y el ciclo de vida de investigación científica.

## [0.3.0] - 2026-06-29

### Added
- **Auditoría de Entradas:** Creado `docs/specification/MISSING_RESEARCH.md` detallando las entradas y ADRs de investigación requeridas para poder iniciar el proceso de especificación.

### Changed
- **Directrices de Agente:** Actualizado `AGENTS.md` adaptándolo al rol de **Chief Specification Architect** y estableciendo las reglas para las 13 secciones obligatorias de especificación.
- **Presentación:** Actualizado `README.md` para reflejar la separación de responsabilidades (Investigación, Especificación, Implementación).

## [0.2.0] - 2026-06-29

### Added
- **Estructura de Referencia:** Creados los directorios para la implementación de referencia (`docs/specification/`, `docs/architecture/`, `docs/validation/`, `src/`, `tests/`, `benchmarks/`, `examples/`, `reference/`, `scripts/`).
- **Control de Especificación:** Creado `docs/specification/README.md` identificando la falta de especificación oficial de FKT y deteniendo el desarrollo en base a la regla de no invención.

### Changed
- **Directrices de Agente:** Actualizado `AGENTS.md` para reflejar el rol de Principal Software Architect y los Seis Principios Inmutables de desarrollo.
- **Presentación:** Actualizado `README.md` enfocándose en el desarrollo cross-language y el roadmap de implementación.

## [0.1.0] - 2026-06-29

### Added
- **Estructura Agents First:** Inicialización de la arquitectura documental optimizada para agentes de IA y humanos.
- **Entrada de Agente:** Creado `AGENTS.md` como punto de entrada de instrucciones de tareas y límites.
- **Documentación de Proyecto:** Creado `README.md` con la visión global, la hipótesis central, los Cinco Principios Inmutables y el Roadmap del laboratorio.
- **Instrucciones Gemini:** Creado `GEMINI.md` para guiar a los agentes basados en Gemini en el razonamiento de FKT.
- **Pautas de Seguridad y Permisos:** Creados `docs/agent/PERMISSIONS.md` (permisos y firmas humanas) y `docs/agent/SECURITY.md` (manejo de secretos y exclusión de datos con copyright).
- **Manuales Operativos:** Creados `docs/agent/RUNBOOK.md` (ciclo de investigación), `docs/agent/TESTS.md` (verificaciones teóricas y experimentales), `docs/agent/CONFIG.md` (entorno virtual y dependencias recomendadas) y `docs/agent/DATA_SCHEMA.md` (schema del reporte de 8 secciones).
- **Área de Investigación:** Creado el directorio `research/` y su respectiva introducción para almacenar bitácoras y demostraciones matemáticas.
- **Skill Especializado:** Creado `skills/research-document/SKILL.md` para automatizar y verificar la generación de reportes de investigación.
