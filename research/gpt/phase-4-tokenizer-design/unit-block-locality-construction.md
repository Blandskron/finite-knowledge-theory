# Fase 4: construcción de localidad fuerte con bloques unitarios

## Objective

Determinar si existe una regla determinista de segmentación sobre octetos que mantenga un tamaño máximo fijo y una distancia de resincronización independiente de la longitud del documento para toda edición local.

## Background

La métrica aprobada para investigación exige distinguir una garantía fuerte \(R_\tau(x,e)\leq C\) de una propiedad promedio. El baseline de bloques fijos \(\tau_M\) falla esa condición ante inserciones y eliminaciones cuando \(M>1\). La segmentación definida por contenido puede preservar límites en muchos casos, pero los métodos habituales dependen de parámetros y compromisos de tamaño; incluso las propuestas recientes que reclaman garantías estrictas añaden una construcción más compleja [Chonkers](https://arxiv.org/abs/2509.11121). Antes de estudiar esas alternativas, debe resolverse la cuestión de existencia mínima.

## Hypothesis

El tokenizador unitario \(\tau_1\), que representa cada octeto como un bloque con carga de longitud uno, satisface reconstrucción exacta, determinismo, \(S(\tau_1)=1\) y \(R^{\max}_{\tau_1}=0\) para inserciones, eliminaciones y sustituciones locales.

## Analysis

Para \(x=(x_1,\ldots,x_n)\in B^*\), defínase \(\tau_1(x)=((1,x_1),\ldots,(1,x_n))\). Cada par es un bloque válido de la gramática aprobada con \(M=1\). La decodificación elimina las cabeceras y concatena las cargas, por lo que recupera exactamente \(x\). La regla es determinista y no depende de posición, corpus, vocabulario, hash ni estado externo.

Todo límite entre dos octetos es una frontera de token. Para una sustitución, las fronteras permanecen y solo cambia el token cuyo único octeto fue sustituido. Para una inserción, el token nuevo ocupa exactamente el intervalo insertado; bajo la alineación \(\phi_e\), cada octeto no modificado del sufijo conserva su token unitario y la frontera al final de la edición ya es común. Para una eliminación sucede simétricamente. Según la definición de distancia de resincronización, \(R_{\tau_1}(x,e)=0\) para toda edición local y, por tanto, \(R^{\max}_{\tau_1}=0\).

La construcción responde afirmativamente a la pregunta de existencia con una cota independiente de \(|x|\). También revela una limitación de la pregunta: si solo se exige tamaño máximo y localidad, la solución trivial de un octeto por token siempre satisface el requisito. Por eso, esa exigencia no justifica por sí misma un algoritmo de segmentación más elaborado.

El coste es una granularidad máxima: hay \(|x|\) tokens para una entrada de \(|x|\) octetos y cada bloque serializado añade una cabecera. No se afirma que esta representación sea eficiente, comprimida o semánticamente informativa. La evidencia de métodos definidos por contenido es útil para estudiar agrupación, pero no reemplaza esta prueba elemental ni convierte sus beneficios prácticos en garantías fundacionales.

## Decision

Pending Investigation.

Queda demostrada la existencia de una regla con localidad fuerte: \(\tau_1\). No se propone adoptarla como tokenizador de FKT porque el proyecto aún no ha definido qué ganancia de agrupación, eficiencia o estructura debe compensar su mayor cantidad de tokens. No se crea ADR ni se autoriza implementación.

## Impact

La Fase 4 ya no debe preguntar si la localidad fuerte es posible, sino qué requisito adicional no trivial debe satisfacer un tokenizador FKT y cómo se medirá sin abandonar determinismo y reconstrucción. Cualquier propuesta que use bloques mayores que uno debe compararse contra \(\tau_1\) como límite de localidad.

## Next Investigation

¿Qué objetivo no semántico y medible debe justificar el uso de bloques mayores que un octeto en FKT sin debilitar la garantía de localidad fuerte?

## Status

Status: 🟡 Research
