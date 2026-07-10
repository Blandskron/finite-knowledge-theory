# Fase 4: baseline de tokenizador por bloques fijos

## Objective

Definir un tokenizador teórico mínimo, determinista y reversible sobre la gramática aprobada de bloques acotados, y establecer con precisión sus límites frente a ediciones locales.

## Background

[ADR-001](../../../adr/ADR-001-octet-foundation-and-bounded-block-grammar.md) acepta los octetos como capa de representación y una gramática de bloques de longitud explícita, pero no fija la regla que elige los límites de bloque. Una regla de segmentación debe ser independiente de corpus, vocabulario aprendido y heurísticas implícitas. La literatura sobre *content-defined chunking* usa marcas derivadas del contenido para preservar límites tras modificaciones en muchos casos, pero vincula el resultado a parámetros como ventana, marca y tamaño máximo [USENIX FAST '05](https://www.usenix.org/legacy/event/fast05/tech/full_papers/jain/jain_html/).

## Hypothesis

Para un parámetro fijo \(M\), la partición de izquierda a derecha en cargas de longitud \(M\), salvo la última, es un baseline suficiente para definir una tokenización totalmente determinista y reversible de \(B^*\). Su coste de estabilidad está acotado con exactitud: una sustitución sin cambio de longitud afecta a lo sumo un bloque, mientras que una inserción o eliminación puede resegmentar todo el sufijo.

## Analysis

Sea \(M\) un entero fijado por la futura especificación, con \(1 \leq M \leq 255\). Para una entrada \(x \in B^*\) de longitud \(n\), el tokenizador \(\tau_M\) procede conceptualmente así: si \(n=0\), produce la lista vacía. En caso contrario, divide \(x\) en la secuencia ordenada de subcadenas \((c_1, \ldots, c_r)\), donde \(|c_i|=M\) para \(i<r\) y \(1 \leq |c_r| \leq M\). Cada token es el par \((|c_i|, c_i)\), serializable mediante la cabecera de longitud de la gramática aprobada.

El inverso \(\rho_M\) elimina las cabeceras y concatena las cargas. Por construcción, \(\rho_M(\tau_M(x))=x\) para todo \(x \in B^*\). La regla no consulta datos externos; por tanto, misma entrada y mismo \(M\) producen siempre la misma salida. También es inequívoca: los límites son múltiplos de \(M\) desde el inicio y la última carga se identifica por su longitud explícita.

La estabilidad depende del tipo de edición. Una sustitución en una posición altera únicamente la carga que contiene esa posición y conserva todos los límites, por lo que preserva los demás tokens. Una inserción o eliminación desplaza la congruencia de las posiciones siguientes módulo \(M\); por ello puede modificar cada bloque posterior y tiene peor caso lineal en la longitud del sufijo. Esta limitación no invalida la reversibilidad, pero demuestra que bloques fijos no satisfacen una garantía fuerte de actualización local.

Una alternativa posterior es introducir límites definidos por contenido con una función de ventana y parámetros públicos fijados. Esa familia puede volver a sincronizar límites después de una edición en entradas favorables, pero no debe aceptarse por una expectativa estadística sin declarar métrica, parámetros, tratamiento de secuencias adversariales y garantía de peor caso. Tampoco se ha demostrado que mejore el objetivo de FKT, que aún se refiere a representación y no a compresión o deduplicación.

Por tanto, \(\tau_M\) es un baseline teórico, no un tokenizer semántico: sus tokens no representan palabras, grafemas ni conceptos. El valor de \(M\) sigue abierto; elegirlo ahora sería una decisión de diseño sin la evidencia comparativa requerida.

## Decision

Pending Investigation.

Se propone \(\tau_M\) como baseline formal para evaluar determinismo, reconstrucción y sensibilidad a ediciones. Aún no se adopta como especificación porque falta definir una métrica de localidad, criterios para seleccionar \(M\) y la necesidad misma de segmentación definida por contenido. No se crea ADR ni se autoriza implementación.

## Impact

La Fase 5 podrá comparar reglas solo contra propiedades explícitas: reconstrucción exacta, tamaño máximo, cantidad de tokens alterados y distancia hasta resincronización. Esto impide presentar una mejora probabilística de *chunking* como una propiedad fundacional sin evidencia reproducible.

## Next Investigation

¿Qué métrica formal de localidad de edición debe satisfacer FKT antes de comparar bloques fijos con segmentación definida por contenido?

## Status

Status: 🟡 Research
