# Fase 4: contrato de admisibilidad para agrupación con localidad estricta

## Objective

Formular un contrato autosuficiente con el que FKT pueda evaluar cualquier agrupación candidata de localidad estricta, incluida una posible adaptación de Chonkers, sin depender de código, estado de ejecución ni convenciones implícitas.

## Background

El análisis previo identifica cuatro obligaciones: determinismo, reconstrucción exacta, parámetros trazables y cotas de localidad comparables. Chonkers ofrece una dirección externa, pero su descripción disponible no puede importarse como especificación. FKT necesita primero un criterio propio de admisibilidad que sea independiente de un algoritmo concreto.

## Hypothesis

Un contrato de seis cláusulas —dominio, parámetros, canonicidad, reconstrucción, límites y localidad— es suficiente para decidir si una agrupación puede pasar de hipótesis de investigación a candidata para una especificación futura.

## Analysis

Sea \(u=\tau_1(x)\) la secuencia canónica de tokens unitarios de una entrada \(x\). Una candidata \(A_P\) recibe \(u\) y una tupla finita y pública de parámetros \(P\). El contrato exige lo siguiente.

Primero, el **dominio** debe incluir toda secuencia finita de tokens unitarios, incluida la vacía, y declarar de forma total qué sucede ante parámetros inválidos. Segundo, los **parámetros** deben ser valores finitos serializables: por ejemplo, un máximo de carga \(M\), una cantidad de capas \(L\), prioridades y reglas de comparación. Ningún valor puede provenir de corpus, reloj, memoria, aleatoriedad, caché o historial de ediciones.

Tercero, la **canonicidad** exige que \(A_P(u)\) sea una función pura: para los mismos \(u\) y \(P\), toda implementación conforme produce la misma secuencia ordenada de vistas y los mismos límites. Cada empate debe tener una regla explícita dependiente solo de contenido, posición canónica o parámetros públicos. Cuarto, la **reconstrucción** exige una expansión \(E\) con \(E(A_P(u))=u\), y cada vista debe cubrir un intervalo contiguo, no vacío y sin solapamiento de \(u\).

Quinto, los **límites** deben proporcionar constantes explícitas \(M(P)\) y \(G(P)\): toda vista tiene carga entre uno y \(M(P)\), y el factor de reducción observado debe definirse como \(|u|/|A_P(u)|\). Un algoritmo puede permitir \(G=1\) en casos adversariales, pero no puede afirmar una reducción mínima mayor que uno sin prueba para el dominio declarado.

Sexto, la **localidad** debe declarar una constante \(C(P)\) y una clase exacta de ediciones. Para toda edición permitida \(e\), debe demostrarse \(R_{A_P}(u,e)\leq C(P)\), con la alineación \(\phi_e\) ya definida por FKT. Si la garantía es solo promedio, el contrato la clasifica como empírica y prohíbe describirla como estricta. La prueba debe ser independiente de la longitud de \(u\).

Este contrato sí permite expresar un subconjunto verificable de Chonkers en el futuro, pero no pretende que el subconjunto exista ya. La elección de unidades, capas o prioridades de un algoritmo concreto solo es admisible cuando todas las cláusulas se completan y se prueban. \(\tau_1\) satisface el contrato con \(M=1\), \(G=1\) y \(C=0\), lo que confirma que el contrato no presupone agrupación no trivial.

## Decision

Pending Investigation.

Se propone el contrato de seis cláusulas como marco de evaluación de candidatos con localidad estricta. No se adopta un algoritmo concreto, no se afirma que Chonkers lo satisfaga y no se crea ADR. El contrato debe recibir revisión matemática y humana antes de formalizarse en especificación.

## Impact

FKT puede ahora rechazar de manera verificable propuestas que dependan de estado oculto o que confundan resultados promedio con garantías. Una futura adaptación deberá documentar sus parámetros y prueba contra cada cláusula, preservando siempre \(\tau_1\) como representación canónica.

## Next Investigation

¿Puede construirse una agrupación no trivial \(A_P\) que cumpla las seis cláusulas con \(G(P)>1\) en un dominio explícitamente declarado?

## Status

Status: 🟡 Research
