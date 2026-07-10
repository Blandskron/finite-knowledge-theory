# exp-002: control de marca de ventana con corte forzado

## Objective

Implementar un control experimental mínimo para contrastar el comportamiento de una marca de contenido con un tamaño máximo forzado.

## Background

La Fase 4 demostró que la familia clásica de marcas de ventana puede resincronizar en casos favorables, pero que los cortes forzados conservan un peor caso semejante a bloques fijos. `exp-001` validó los controles unitario, fijo y delimitado; este experimento aísla la regla de marca sin afirmar que sea Rabin, Gear o Chonkers.

## Hypothesis

Un control con una marca derivada de la suma modular de una ventana conservará un grupo posterior cuando una marca natural reaparece, pero se comportará como bloques fijos en un tramo donde ninguna ventana alcance la marca y los cortes sean todos forzados.

## Analysis

Los parámetros serán una ventana \(w\), una longitud mínima \(m\), una longitud máxima \(M\) y una marca \(a\). Tras acumular al menos \(m\) octetos desde el último corte, se creará un límite natural si la suma modular de los últimos \(w\) octetos es \(a\); se creará un límite forzado al alcanzar \(M\). La suma modular se elige por transparencia y determinismo, no por resistencia a colisiones ni rendimiento.

El experimento verificará reconstrucción, determinismo y el máximo \(M\). Usará un caso con marcadores naturales y un caso sin marcadores, ambos con una inserción local. El resultado se medirá con el mismo conteo de prefijo, sufijo y grupos afectados de `exp-001`.

## Decision

Pending Investigation.

El control se crea exclusivamente para contrastar la hipótesis de Fase 4. No es una implementación de segmentación por contenido aprobada, no representa un algoritmo publicado y no altera \(\tau_1\) como baseline canónico.

## Impact

El resultado permitirá decidir si la evidencia experimental reproduce el límite teórico bajo parámetros visibles. No podrá demostrar una propiedad universal de toda posible regla de contenido.

## Next Investigation

¿Los casos naturales y forzados del control reproducen respectivamente preservación local y pérdida de sufijo?

## Status

Status: 🟡 Research
