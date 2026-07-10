# Fase 4: síntesis del tokenizador teórico y propuesta experimental

## Objective

Consolidar las conclusiones de diseño teórico de Fase 4 y definir el alcance mínimo, reproducible y no productivo de los primeros experimentos en Python de Fase 5.

## Background

Las Fases 1 a 3 aprobadas establecen una representación basada en octetos y una gramática de bloques acotados. La Fase 4 investigó tokenización reversible, localidad de edición y agrupación derivada. Se evaluaron bloques fijos, tokens unitarios, vistas de ancho fijo, reglas clásicas definidas por contenido, una construcción delimitada y una candidata externa con garantías declaradas.

## Hypothesis

El resultado suficiente para abrir experimentos es mantener \(\tau_1\) como baseline canónico y probar empíricamente, sin atribuirles estatus fundacional, las agrupaciones derivadas contra métricas explícitas de reconstrucción, tamaño, reducción y localidad.

## Analysis

La tokenización unitaria \(\tau_1\) es total sobre \(B^*\), determinista y reversible; para toda edición local conserva los tokens no modificados bajo alineación y cumple \(R^{\max}=0\). Por tanto, constituye el control universal de representación y localidad. No debe confundirse con semántica ni con una propuesta de compresión.

Los bloques y agrupaciones de ancho fijo pueden reducir la cantidad de elementos inmediatos, pero una inserción o eliminación general desplaza sus fronteras y deja un peor caso no acotado. Las reglas clásicas definidas por contenido pueden mejorar el comportamiento en entradas favorables, pero una marca de ventana combinada con un máximo forzado conserva tramos adversariales que se comportan como cortes fijos. Ninguno de esos mecanismos queda adoptado como garantía universal.

La construcción delimitada demuestra que el contrato de admisibilidad es consistente: una agrupación puede lograr \(G>1\) y una cota de localidad cuando declara un dominio y una clase de edición que preserva sus delimitadores. Sin embargo, FKT no puede convertir esa garantía condicionada en una propiedad de entradas arbitrarias. Chonkers permanece como candidata externa: su preprint es relevante, pero no se ha transformado en una especificación autosuficiente conforme a las métricas de FKT.

La separación de responsabilidades es esencial. La capa canónica será \(\tau_1\). Las agrupaciones \(A\) se tratarán como vistas derivadas que deben expandirse exactamente a \(\tau_1\); sus métricas de daño no alteran la garantía de la capa canónica. Esta separación permite experimentar sin fijar una teoría semántica ni una implementación de producción.

El primer experimento propuesto, `exp-001-tokenization-locality`, tendrá tres familias: \(\tau_1\); bloques fijos \(\tau_M\) para varios \(M\); y la agrupación delimitada \(A_P\) con retroceso unitario. Sus entradas incluirán cadena vacía, secuencias repetitivas, secuencias con y sin delimitadores y ediciones de sustitución, inserción y eliminación. Las invariantes obligatorias serán reconstrucción exacta, determinismo, límite de tamaño declarado y medición de daño/resincronización. El experimento no implementará Chonkers, no entrenará modelos y no definirá APIs públicas.

## Decision

Accepted.

El usuario aprobó explícitamente el 2026-07-09 abrir la Fase 5 para `exp-001-tokenization-locality`. \(\tau_1\) pasa a ser baseline experimental canónico; toda agrupación superior se tratará como vista derivada y se evaluará mediante \(S\), \(D\), \(R\), \(R^{\max}\) y \(G\). Ninguna agrupación no trivial queda aceptada como universal. La decisión queda trazada en [ADR-002](../../../adr/ADR-002-phase-5-tokenization-locality-experiment.md).

## Impact

La aprobación no crea una especificación oficial ni una implementación de referencia. Autoriza únicamente las primeras líneas de código experimental aislado, cuya función es intentar refutar o cuantificar las propiedades ya documentadas. Cualquier resultado experimental se registrará en markdown y requerirá revisión antes de modificar conocimiento compartido o ADRs.

## Next Investigation

¿Aprueba el usuario abrir la Fase 5 para el experimento aislado `exp-001-tokenization-locality` con \(\tau_1\), \(\tau_M\) y \(A_P\) como controles?

## Status

Status: 🟢 Approved
