# Fase 3: finitud de una gramática de bloques acotados

## Objective

Probar que una gramática concreta de bloques de longitud explícita puede tener un alfabeto y un conjunto de tipos finitos, permitir reconstrucción determinista y representar cualquier secuencia finita de octetos.

## Background

Las investigaciones de Fase 1 y 2 proponen el alfabeto \(B = \{0, \ldots, 255\}\) y distinguen una gramática finita de la colección ilimitada de documentos. Para transformar esa distinción en evidencia, se requiere una gramática precisa cuya cardinalidad y decodificación puedan demostrarse, sin asumir vocabularios aprendidos ni significados lingüísticos.

## Hypothesis

Para cualquier límite fijo \(M\) con \(1 \leq M \leq 255\), una gramática cuyos bloques sean un octeto de longitud \(\ell\) seguido de \(\ell\) octetos de carga, con \(0 \leq \ell \leq M\), es finita, se segmenta de manera única y representa cada cadena de \(B^*\) como una secuencia de bloques.

## Analysis

Defínase el conjunto de bloques como \(G_M = \bigcup_{\ell=0}^{M} \{\ell\} \times B^\ell\). El primer componente se serializa en un octeto y especifica cuántos octetos de carga le siguen. El valor \(\ell = 0\) se excluye de documentos ordinarios para evitar bloques vacíos repetibles; se conserva aquí solo para describir el conjunto completo de tipos posibles. Para los bloques no vacíos, \(G_M^+ = \bigcup_{\ell=1}^{M} \{\ell\} \times B^\ell\).

La cardinalidad de los tipos no vacíos es

\[
|G_M^+| = \sum_{\ell=1}^{M} |B|^\ell = \sum_{\ell=1}^{M} 256^\ell.
\]

Como \(M\) y \(|B|\) son finitos, la suma es finita. La cabecera no agrega un alfabeto: pertenece a \(B\), por lo que la gramática usa exclusivamente la capa fundacional propuesta. El número de niveles de tipos es dos: octeto y bloque. La secuencia exterior de bloques no constituye un tipo fundacional adicional; es la colección de un documento.

La segmentación es única. Desde una posición válida \(p\), el primer octeto determina un único valor \(\ell\). El bloque ocupa exactamente las posiciones \(p\) a \(p+\ell\), incluida la cabecera. Por inducción sobre la cantidad de bloques, al retirar ese prefijo queda un único sufijo que se analiza con la misma regla. Si faltan \(\ell\) octetos de carga, la entrada codificada es inválida y debe rechazarse; no existe una segunda segmentación válida. La reconstrucción elimina cada cabecera y concatena las cargas en orden, obteniendo exactamente la secuencia original.

Toda cadena \(x \in B^*\) puede codificarse de forma constructiva: dividir \(x\) de izquierda a derecha en fragmentos de longitud \(M\), salvo posiblemente el último de longitud entre 1 y \(M\), y anteponer a cada fragmento su longitud. La cadena vacía se representa mediante una lista de cero bloques, no mediante un bloque vacío. Por tanto, la codificación existe para cualquier longitud finita, aunque \((G_M^+)^*\) sea infinito como conjunto de documentos.

Esta prueba establece finitud sintáctica, no finitud semántica ni compresión. El parámetro \(M\) sigue sin estar justificado; escogerlo altera la cantidad finita de tipos, la expansión de cabeceras y el comportamiento frente a ediciones. Además, una inserción que cruza el límite de un bloque puede requerir dividirlo; la estabilidad local debe definirse y evaluarse antes de afirmar ventaja frente a segmentación fija.

## Decision

Accepted.

El usuario aprobó explícitamente el 2026-07-09 la gramática parametrizada como evidencia de finitud sintáctica y reconstrucción determinista. La aceptación no selecciona un valor de \(M\), no atribuye significado a los bloques y no prueba la tesis global de conocimiento finito. La decisión queda trazada en [ADR-001](../../../adr/ADR-001-octet-foundation-and-bounded-block-grammar.md).

## Impact

FKT dispone de una candidata verificable para separar una base finita y una gramática finita de un flujo documental no acotado. La Fase 4 puede comparar esta gramática con otras reglas de segmentación según determinismo, reconstrucción, comportamiento ante errores y actualización local. No autoriza código de producción.

## Next Investigation

¿Qué regla de segmentación sobre la gramática de bloques acotados minimiza la resegmentación tras una inserción, eliminación o sustitución local?

## Status

Status: 🟢 Approved
