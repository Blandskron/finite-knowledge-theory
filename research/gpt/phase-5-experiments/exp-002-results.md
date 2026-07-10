# exp-002: resultados del control de marca de ventana

## Objective

Registrar la ejecución reproducible del control de marca de ventana con corte máximo forzado.

## Background

El experimento implementa la hipótesis de Fase 4 con una suma modular transparente; no es una implementación de Rabin, Gear, FastCDC o Chonkers.

## Hypothesis

La presencia de una marca natural preservará el grupo posterior a una inserción local, mientras que un tramo sin marcas se segmentará por el máximo forzado y perderá el sufijo exacto.

## Analysis

Ejecutado el 2026-07-09 con el runtime Python empaquetado. Las 13 pruebas combinadas de `exp-001` y `exp-002` pasaron.

Con `window=1`, `minimum=2`, `maximum=4` y `marker=ord("Z")`, la salida fue:

```text
natural-marker: before=(b'abZ', b'cdZ') after=(b'abXZ', b'cdZ') prefix=0 suffix=1 changed=2
forced-only: before=(b'abcd', b'efgh', b'ijkl') after=(b'aXbc', b'defg', b'hijk', b'l') prefix=0 suffix=0 changed=7
```

El primer caso confirma que una marca de contenido puede resincronizar después de una edición cuando una frontera natural subsiguiente permanece. El segundo demuestra el límite anunciado: al no aparecer `Z`, cada frontera surge del máximo cuatro y una inserción desplaza todos los grupos posteriores. La suma modular es deliberadamente simple; los resultados prueban el comportamiento de este control, no una generalización estadística para funciones de huella criptográfica o rodante.

## Decision

Pending Investigation.

El resultado respalda el análisis de Fase 4 para la familia de marca de ventana con corte forzado. No adopta la regla como agrupación universal ni refuta algoritmos con garantías estrictas de otra construcción.

## Impact

El harness ya contiene controles reproducibles para los casos favorable y adversarial de una regla clásica definida por contenido. Un siguiente experimento solo estará justificado si formula una construcción con garantías distintas, no si repite parámetros de este control.

## Next Investigation

¿Qué construcción autosuficiente, distinta de marcas con corte forzado, puede someterse al contrato de localidad estricta de FKT?

## Status

Status: 🟡 Research
