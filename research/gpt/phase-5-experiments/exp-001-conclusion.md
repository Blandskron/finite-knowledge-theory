# exp-001: conclusión de controles de localidad

## Objective

Cerrar el alcance aprobado de `exp-001-tokenization-locality` y separar los resultados observados de cualquier conclusión teórica aún no aprobada.

## Background

ADR-002 autorizó comparar \(\tau_1\), bloques fijos \(\tau_M\) y agrupación delimitada \(A_P\) con reconstrucción, determinismo y métricas de cambio. Las Fases 1 a 4 ya habían formulado las predicciones que este experimento debía contrastar.

## Hypothesis

Los controles experimentales reproducirán las predicciones teóricas: \(\tau_1\) conservará el sufijo no modificado bajo ediciones locales, los bloques fijos sufrirán desalineación por inserción o eliminación, y \(A_P\) conservará localidad solo dentro de su dominio declarado.

## Analysis

La suite final ejecutó nueve pruebas con solo la biblioteca estándar. Incluyó reconstrucción y determinismo de los tres controles, sustitución, inserción, eliminación, parámetros inválidos, un caso delimitado válido y una enumeración exhaustiva de 769 inserciones de un octeto en cadenas binarias de longitud hasta seis.

Todos los casos pasaron. Para la inserción de control, \(\tau_1\) conservó siete grupos de sufijo y registró un grupo nuevo; \(\tau_4\) conservó cero grupos de sufijo y registró cinco grupos afectados entre las dos salidas. En el caso delimitado válido, la edición modificó el primer grupo y preservó el segundo. Estos resultados coinciden con las propiedades esperadas de cada construcción.

La enumeración exhaustiva aporta evidencia de implementación para la identidad concreta de \(\tau_1\): al insertar un octeto en la posición \(p\) de una cadena de longitud \(n\), el experimento observó prefijo común \(p\), sufijo común \(n-p\) y exactamente un grupo agregado en los 769 casos del dominio finito probado. No extiende esa verificación a entradas arbitrarias ni prueba por sí sola la teoría matemática general.

## Decision

Pending Investigation.

`exp-001` se considera ejecutado y reproducible dentro de su alcance. Sus observaciones respaldan los controles teóricos, pero no aprueban \(\tau_1\) como especificación oficial ni seleccionan una agrupación universal. Se requiere revisión humana antes de promover el resultado o abrir un experimento de alcance mayor.

## Impact

El laboratorio dispone de un harness Python probado para futuros experimentos de localidad. Cualquier siguiente experimento deberá declarar una hipótesis distinta y mantener los controles \(\tau_1\), \(\tau_M\) y \(A_P\) cuando sean pertinentes.

## Next Investigation

¿Aprueba el usuario usar `exp-001` como evidencia de control para diseñar el siguiente experimento de agrupación universal?

## Status

Status: 🟡 Research
