# Fase 4: límite de la agrupación clásica definida por contenido

## Objective

Determinar si una regla clásica de agrupación definida por contenido, con ancho máximo fijo, puede evitar para toda edición local el daño no acotado de la agrupación de ancho fijo.

## Background

La agrupación fija ofrece \(G_q>1\) pero pierde toda resincronización en un sufijo tras ciertos desplazamientos. La agrupación definida por contenido elige límites mediante una función de una ventana de datos, por ejemplo una huella rodante que coincide con una marca. Este enfoque puede conservar límites próximos a una edición en muchos casos, pero necesita un tamaño máximo para impedir bloques arbitrariamente grandes. La literatura de sistemas observa que ese máximo fuerza cortes y puede degradar la resiliencia a actualizaciones [USENIX FAST '05](https://www.usenix.org/legacy/event/fast05/tech/full_papers/jain/jain_html/).

## Hypothesis

Una regla clásica de marca de contenido con máximo forzado \(M\) no puede garantizar simultáneamente \(G>1\), ancho máximo \(M\) y daño de vista acotado para toda entrada y toda edición local. Puede mejorar la localidad en casos favorables, pero conserva un peor caso no acotado.

## Analysis

Considérese una regla que examina cada ventana de \(w\) tokens unitarios y crea una frontera natural cuando una función determinista \(h\) devuelve una marca \(a\). Para asegurar que cada grupo mida como máximo \(M\), la regla introduce una frontera forzada cuando han transcurrido \(M\) tokens desde la última frontera sin encontrar una marca natural. Si se elimina ese mecanismo forzado, una entrada sin marcas naturales puede producir grupos de longitud arbitraria y viola el requisito de ancho máximo.

Para que \(G>1\) sea posible, la regla no puede marcar cada posición de cada entrada; existe al menos una ventana cuyo valor no coincide con \(a\). En las reglas clásicas basadas en una marca de huella, puede elegirse una repetición de esa ventana no marcada para formar un tramo sin fronteras naturales. En dicho tramo, todos los límites son forzados y quedan a distancias múltiplos de \(M\) desde la frontera precedente.

Una inserción de longitud no múltiplo de \(M\) dentro de ese tramo desplaza las fronteras forzadas del sufijo respecto de la alineación de contenido. Igual que en \(A_q^{\mathrm{fix}}\), no tiene por qué reaparecer una frontera común antes del final del tramo. Al elegir un tramo sin marcas tan largo como se quiera, el daño de vista y la distancia de resincronización crecen sin cota. Por tanto, el peor caso de la regla clásica con máximo forzado sigue siendo \(R^{\max}=\infty\).

Este resultado no niega el valor práctico de la segmentación definida por contenido. Las fronteras derivadas del contenido pueden resincronizar después de ediciones en datos que contengan marcas adecuadas; la fuente consultada describe justamente ese compromiso y también señala que el tamaño máximo produce cortes con comportamiento similar a bloques fijos. La propiedad es entonces condicional o estadística, no una garantía fundacional universal.

Tampoco se concluye que toda posible agrupación definida por contenido sea imposible. Construcciones recientes afirman garantías estrictas de tamaño y localidad, pero su modelo, prueba y compatibilidad con los requisitos de FKT deben auditarse antes de usarlas. El presente resultado se limita a la familia clásica de marcas de ventana con máximo forzado.

## Decision

Pending Investigation.

Se concluye que la agrupación clásica definida por contenido no satisface por sí sola la garantía fuerte requerida por FKT en el peor caso. Puede quedar como candidato empírico si declara sus parámetros y distribución de evaluación, pero no se adopta como propiedad fundacional ni como solución universal. No se crea ADR ni se autoriza implementación.

## Impact

Las comparaciones futuras deben separar resultados promedio de teoremas de peor caso. Para lograr \(G>1\) con localidad fuerte, FKT necesitaría una construcción con prueba explícita distinta de la marca clásica con corte forzado, o aceptar conscientemente una garantía no universal.

## Next Investigation

¿La construcción Chonkers publicada en 2025 satisface, bajo una lectura verificable, los requisitos de determinismo, reconstrucción y ausencia de estado oculto que FKT exige?

## Status

Status: 🟡 Research
