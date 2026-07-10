# exp-003: control multicapa canónico por mitades

## Objective

Implementar el protocolo de independencia de historial sobre una construcción multicapa propia, pura y reproducible.

## Background

El protocolo de Fase 5 requiere comparar salidas por capa entre rutas de construcción. Para validar el protocolo sin usar código externo, se necesita una construcción cuyo resultado dependa únicamente de la secuencia final. La partición recursiva por mitades es un control matemático simple: no pretende representar una segmentación eficiente ni local.

## Hypothesis

Una vista de intervalos obtenida al dividir recursivamente cada intervalo no unitario por su punto medio producirá exactamente las mismas capas para una secuencia final dada, sin importar si se alcanzó por construcción directa, inserción, concatenación o edición.

## Analysis

La construcción recibe solo los bytes finales. El intervalo raíz es \([0,n)\); cada intervalo de longitud mayor que uno se divide en \([inicio,\lfloor(inicio+fin)/2\rfloor)\) y \([\lfloor(inicio+fin)/2\rfloor,fin)\). Las capas observables son listas ordenadas de intervalos por profundidad. Las hojas cubren la entrada sin solapamiento y reconstruyen exactamente la secuencia.

Como la función no recibe historia, caché ni estado de actualización, las rutas del protocolo deben converger. Esta propiedad valida el mecanismo de comparación, no la hipótesis de localidad: una inserción puede modificar puntos medios y múltiples intervalos internos, por lo que el control ilustra el coste de normalización canónica global.

## Decision

Pending Investigation.

Se crea `exp-003` únicamente como control de canonicidad multicapa. No se propone la partición por mitades como agrupación FKT, no se crea ADR y no se autoriza una implementación de referencia.

## Impact

El laboratorio obtiene un caso positivo para el protocolo de historial y una base para comparar futuras construcciones multicapa que pretendan mejorar localidad sin perder canonicidad.

## Next Investigation

¿El control por mitades conserva igualdad de capas para las cuatro rutas y qué capas cambian tras una inserción local?

## Status

Status: 🟡 Research
