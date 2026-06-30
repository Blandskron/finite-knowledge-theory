# 🛡️ Seguridad (SECURITY.md)

Este repositorio almacena la base teórica y experimental de FKT/FLM. Aunque es un proyecto de investigación, debe cumplir con estrictas normas de seguridad de la información y protección de propiedad intelectual.

---

## 1. Gestión de Secretos

*   **Sin Claves en Git:** Nunca agregues tokens de API (ej. `GEMINI_API_KEY`, `OPENAI_API_KEY`), credenciales de bases de datos o contraseñas al repositorio.
*   **Placeholders:** Si un script de prueba requiere una API key, usa variables de entorno locales (ej. `os.getenv("GEMINI_API_KEY")`) y documenta el requerimiento usando placeholders como `PLACEHOLDER_KEY`.
*   **Archivos Excluidos:** Asegura que `.env` y archivos `.secrets/` estén listados en `.gitignore`.

---

## 2. Propiedad Intelectual y Datos de Entrenamiento

Durante la Phase 7, evaluaremos el modelo en distintos "Universos de Conocimiento" (Derecho Civil, Derecho Penal, Medicina, Django, etc.):

*   **Fuentes de Dominio Público:** Prioriza siempre fuentes de datos de dominio público (ej. códigos civiles estatales públicos, textos históricos de medicina, proyectos de software bajo licencia permisiva MIT/Apache).
*   **Sin Datos Propietarios:** Está estrictamente prohibido subir conjuntos de datos con copyright, información personal identificable (PII) o información confidencial al repositorio.
*   **Registro de Licencias de Datos:** Cada dataset de prueba usado en experimentos debe incluir un archivo de texto con el origen y la licencia que permita su uso para fines de investigación.

---

## 3. Seguridad de Ejecución de Código

Como agente de IA, debes proteger el entorno local del usuario:
*   No descargues ni ejecutes binarios o scripts de origen desconocido.
*   Al instalar librerías adicionales para simulaciones (ej. NumPy, SymPy), verifica que provengan de fuentes oficiales del gestor de paquetes (PyPI).
