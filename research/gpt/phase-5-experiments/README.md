# exp-001: Tokenization locality

## Scope

Experimento aislado aprobado por [ADR-002](../../../adr/ADR-002-phase-5-tokenization-locality-experiment.md). Compara tokens unitarios, bloques fijos y agrupación delimitada como controles teóricos.

## Run

Desde este directorio, ejecutar `./run.ps1`. Requiere Python 3.10 o superior disponible como `python` o `py`.

## Files

- `code/tokenization_locality.py`: funciones puras del experimento.
- `code/run_experiment.py`: salida de mediciones reproducibles.
- `tests/test_tokenization_locality.py`: invariantes de reconstrucción, determinismo y localidad.
- `results.md`: registro de la primera ejecución reproducible.
- `exp-001-conclusion.md`: cierre pendiente de revisión humana.
- `exp-002-classical-marker-control.md`: hipótesis y alcance del segundo control.
- `exp-002-results.md`: resultados reproducibles del control de marca de ventana.
- `history-dependent-grouping-limit.md`: límite de canonicidad para vistas persistentes.
- `finite-radius-canonical-grouping-limit.md`: límite de reglas locales invariantes.
- `chonkers-source-audit.md`: auditoría de solo lectura de la implementación pública externa.
- `multilayer-history-independence-protocol.md`: protocolo de canonicidad por rutas de construcción.
- `exp-003-canonical-multilayer-control.md`: alcance del control multicapa por mitades.
- `exp-003-results.md`: resultados reproducibles de canonicidad multicapa.
- `phase-5-synthesis-and-review-request.md`: síntesis de controles y puerta de revisión humana.
- `exp-004-append-only-fixed-block-control.md`: control de localidad condicionado a extensiones append-only.
- `append-only-derived-view-contract.md`: contrato teórico de vista derivada para el dominio append-only.
- `exp-005-append-only-exhaustive-results.md`: control exhaustivo de prefijos completos preservados.
- `append-only-contract-traceability-matrix.md`: matriz de obligaciones, evidencia y alcance del contrato append-only.

## Status

Status: 🟡 Research
