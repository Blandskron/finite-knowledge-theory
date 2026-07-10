# Fase 1: hipótesis de los octetos como primitivas fundacionales

## Objective

Determinar si un alfabeto fijo de octetos puede servir como candidata a primitiva fundacional para representar, sin pérdida, entradas textuales, código y documentos estructurados dentro del alcance de FKT.

## Background

La arquitectura del laboratorio exige que toda primitiva fundacional sea finita, enumerable, estable, determinista y composable. Los vocabularios aprendidos no satisfacen estabilidad porque cambian con los datos y el entrenamiento. Los grafemas y las palabras tampoco son candidatos atómicos fiables: su segmentación depende de reglas, idioma, normalización o composición.

Un octeto es un valor de ocho bits. El conjunto \(B = \{0, 1, \ldots, 255\}\) tiene cardinalidad \(|B| = 256\). Los estándares de codificación también tratan una cadena UTF-8 como una secuencia de octetos, aunque la validez semántica de esa secuencia requiere reglas adicionales [RFC 3629](https://www.rfc-editor.org/rfc/rfc3629.html). Unicode advierte que los puntos de código y sus propiedades evolucionan entre versiones, por lo que no deben confundirse con una fundación inmutable [Unicode Standard, Chapter 3](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/).

## Hypothesis

La candidata mínima para una primitiva fundacional de representación es el octeto sin interpretación semántica, definido como un elemento de \(B\). Una entrada FKT inicial sería una secuencia finita \(x \in B^*\), acompañada fuera de la capa fundacional por un contrato de formato que determine cómo interpretar la secuencia cuando corresponda.

## Analysis

El conjunto \(B\) es finito y enumerable por construcción. Si su identidad se fija como un entero sin signo de ocho bits, no depende de versiones de Unicode, de corpus ni de un diccionario aprendido; por tanto, satisface estabilidad. La correspondencia entre cada valor y su patrón binario es única, así que satisface determinismo.

La composición elemental se define por concatenación de secuencias. Para cualesquiera \(u, v \in B^*\), \(u \mathbin{\Vert} v \in B^*\); además, la concatenación es asociativa y conserva la reconstrucción exacta de la secuencia original. Esto demuestra composabilidad de la representación, no de la semántica. Para un documento binario, \(B^*\) permite preservar cada byte. Para texto UTF-8 válido, la capa de formato puede recuperar una secuencia de caracteres usando una gramática definida por el estándar; las secuencias inválidas deben mantenerse como bytes o producir un error explícito, nunca reinterpretarse silenciosamente.

Se consideraron tres alternativas. Los puntos de código Unicode tienen un rango acotado en una versión concreta, pero su repertorio y propiedades se revisan; fijarlos exigiría congelar una versión y aun así no resolvería normalización ni formato. Los grafemas son combinaciones de puntos de código y no forman una unidad atómica estable universal. Las palabras o tokens aprendidos son finitos solo para un vocabulario congelado y dejan de ser estables si el vocabulario se adapta.

La principal limitación es decisiva: \(B^*\) es infinito, porque admite secuencias de longitud arbitraria. Por ello, esta hipótesis no prueba que el conocimiento ni sus niveles superiores sean finitos; únicamente establece una base finita para entradas arbitrarias. La Fase 2 deberá distinguir con precisión entre un alfabeto fundacional finito, composiciones potencialmente no acotadas y una jerarquía de niveles finita. Tampoco se afirma que el octeto sea una unidad de significado.

## Decision

Accepted.

El usuario aprobó explícitamente el 2026-07-09 que el octeto sea la candidata a primitiva fundacional de representación. La aceptación se limita a la capa de representación: no convierte al octeto en unidad semántica ni autoriza código de producción. La decisión queda trazada en [ADR-001](../../../adr/ADR-001-octet-foundation-and-bounded-block-grammar.md).

## Impact

Si la hipótesis se sostiene, las futuras especificaciones podrán separar una capa de transporte inmutable de 256 símbolos de las reglas de decodificación, estructura y significado. Esto evita que un vocabulario, una versión de Unicode o un corpus se conviertan prematuramente en parte de la fundación. No autoriza implementación de tokenizador ni código de producción.

## Next Investigation

¿Puede definirse una jerarquía con un número finito de niveles sobre \(B^*\) que mantenga reconstrucción determinista sin confundir composiciones no acotadas con primitivas fundacionales?

## Status

Status: 🟢 Approved
