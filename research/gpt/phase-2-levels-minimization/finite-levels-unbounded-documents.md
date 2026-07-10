# Fase 2: niveles finitos y documentos de longitud no acotada

## Objective

Establecer si una representación basada en el alfabeto de octetos \(B\) puede usar un número finito de niveles sin afirmar, erróneamente, que el conjunto de todos los documentos o composiciones es finito.

## Background

La investigación previa propone \(B = \{0, \ldots, 255\}\) como candidata a capa fundacional de representación y reconoce que \(B^*\) es infinito. El roadmap exige determinar el número mínimo de niveles fundacionales, mientras que la arquitectura exige preservar entradas arbitrariamente largas. Por tanto, “niveles finitos” debe significar un número finito de tipos o reglas de composición, no un límite oculto sobre la longitud admisible del documento.

## Hypothesis

Una jerarquía puede tener profundidad y conjunto de tipos finitos, y a la vez representar cada elemento de \(B^*\), si el documento se modela como una secuencia exterior no acotada de unidades de nivel superior. Ninguna jerarquía de profundidad finita y aridad máxima finita puede, en cambio, representar como un único árbol todo \(B^*\) si solo permite hojas de \(B\).

## Analysis

Sea \(T_0 = B\). Para una aridad máxima \(m \geq 2\), un tipo de bloque de nivel 1 puede definirse como \(T_1 = \bigcup_{i=1}^{m} T_0^i\). Su cardinalidad es \(|T_1| = \sum_{i=1}^{m} 256^i\), que es finita. Repitiendo la construcción durante \(d\) niveles con aridades finitas, cada \(T_k\) es finito por inducción: una unión finita de productos cartesianos finitos es finita.

Pero un árbol de profundidad \(d\) y aridad máxima \(m\) contiene, como máximo, \(m^d\) hojas. Puesto que existen cadenas de \(B^*\) de longitud mayor que \(m^d\), tal árbol no puede codificar todas las cadenas como una sola composición. Esta es una limitación estructural, no una deficiencia de un algoritmo particular.

La forma coherente de evitarla es distinguir tres dominios. Primero, el alfabeto fundacional \(B\) es finito. Segundo, los tipos de bloque y sus reglas de reconstrucción pueden ser finitos y versionados. Tercero, un documento es una lista ordenada de cero o más bloques; la lista pertenece a \(T_k^*\), que es infinita si \(T_k\) no es vacío. La reconstrucción es determinista si cada bloque preserva su longitud o si la gramática de bloques es prefijo-libre, y si la concatenación mantiene el orden.

Esta distinción ofrece una prueba de posibilidad para profundidad finita de la gramática, pero no una prueba de “conocimiento finito”. También deja abierta la elección del número mínimo de niveles. Con una sola capa de octetos y una secuencia exterior ya existe representación sin pérdida; añadir bloques solo se justifica si aporta límites, estabilidad de actualización, análisis estructural o eficiencia demostrable. En consecuencia, no debe fijarse aún un número de niveles ni interpretar los bloques como unidades semánticas.

## Decision

Accepted.

El usuario aprobó explícitamente el 2026-07-09 la distinción entre la finitud de primitivas, tipos y niveles, y la cardinalidad no acotada de los documentos. Esta aceptación no fija todavía el número mínimo de niveles ni atribuye significado a los bloques. La decisión queda trazada en [ADR-001](../../../adr/ADR-001-octet-foundation-and-bounded-block-grammar.md).

## Impact

Las fases posteriores deben expresar por separado: conjunto de primitivas, tipos de composición, límite de profundidad y colección de documentos. Cualquier especificación futura que afirme que “todo es finito” deberá indicar el objeto matemático exacto al que se refiere. El diseño de tokenización no puede usar la longitud ilimitada de un corpus como evidencia de que las primitivas o los niveles sean ilimitados.

## Next Investigation

¿Qué gramática determinista de bloques sobre octetos permite segmentación y reconstrucción únicas, con actualización local y sin introducir un vocabulario aprendido?

## Status

Status: 🟢 Approved
