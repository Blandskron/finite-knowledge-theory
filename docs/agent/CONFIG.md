# ⚙️ Configuración del Entorno (CONFIG.md)

Este documento detalla los requisitos del entorno de trabajo para investigadores y agentes que realicen experimentos y simulaciones en el laboratorio de FKT.

---

## 1. Entorno de Ejecución Recomendado

Para correr simulaciones matemáticas y experimentos de tokenización (Fase 5+):

*   **Runtime:** Python 3.10 o superior (necesario por el soporte avanzado de tipado y librerías matemáticas).
*   **Gestor de paquetes:** `pip`.

---

## 2. Configuración de Workspace de Simulación

Para iniciar el entorno virtual local de experimentos:

```bash
# Crear entorno virtual en la raíz de experimentos o en el directorio de la fase
python -m venv .venv

# Activar en Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Activar en Unix/macOS
source .venv/bin/activate
```

---

## 3. Librerías Científicas Comunes

Para validaciones teóricas y experimentación, se recomienda la instalación de:

*   `sympy`: Para validación simbólica y demostraciones algebraicas de finitud.
*   `numpy`: Para operaciones matriciales y simulaciones combinatorias de alta velocidad.
*   `matplotlib`: Para graficar y visualizar distribuciones de frecuencia de primitivas.

No agregues estas dependencias al repositorio principal hasta que empiece la Fase 5. Agrégalas localmente en tu carpeta de experimentación.

---

## 4. Estándar de Formato

*   **Archivos Markdown:** Codificación UTF-8, saltos de línea LF/CRLF consistentes.
*   **Scripts de Python:** Conforme al estándar PEP 8, utilizando tipado estático (`typing`) siempre que sea posible para reducir la ambigüedad conceptual.
