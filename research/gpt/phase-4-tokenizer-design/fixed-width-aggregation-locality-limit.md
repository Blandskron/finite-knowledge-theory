# Fase 4: límite de localidad de la agrupación de ancho fijo

## Objective

Evaluar si una agrupación derivada determinista de ancho fijo puede lograr una reducción de elementos inmediatos mayor que uno y, simultáneamente, una cota de daño de vista independiente de la longitud del documento.

## Background

La capa canónica \(\tau_1\) preserva cada octeto y tiene localidad fuerte. Una vista \(A_q\) puede agrupar hasta \(q\) tokens unitarios para reducir la cantidad de elementos inmediatos. La variante más simple corta la secuencia en grupos consecutivos de longitud \(q\) desde el inicio. Esta regla es determinista y ofrece \(G_q>1\), pero debe analizarse con las métricas de daño y resincronización antes de considerarla útil.

## Hypothesis

Para todo \(q>1\), la agrupación de ancho fijo desde el inicio ofrece un factor \(G_q\) cercano a \(q\) en secuencias largas, pero no tiene una cota de daño de vista ni de resincronización independiente de la longitud tras una inserción o eliminación cuya longitud no sea múltiplo de \(q\).

## Analysis

Defínase \(A_q^{\mathrm{fix}}\) como la partición de la secuencia unitaria \(u\) en grupos consecutivos de \(q\) elementos, salvo el último. Para \(|u|=n\), el número de vistas es \(\lceil n/q\rceil\), de modo que \(G_q(u)=n/\lceil n/q\rceil\). Para \(n\geq q\), este factor es mayor que uno y converge a \(q\) cuando \(n\) crece.

Considérese una inserción de \(s\) tokens unitarios con \(s\not\equiv0\pmod q\). Después de la inserción, toda frontera fija del sufijo se desplaza \(s\) posiciones respecto de la alineación de contenido \(\phi_e\). Una frontera situada a una posición múltiplo de \(q\) antes de la edición se alinea con una frontera posterior solo si el desplazamiento es múltiplo de \(q\); por hipótesis no lo es. Por tanto, pueden no existir fronteras comunes alineadas hasta el final del documento.

Para una secuencia con un sufijo de longitud arbitraria, el número de vistas del sufijo que cambian es \(\Theta(n/q)\). En las métricas definidas, \(R_{A_q^{\mathrm{fix}}}(u,e)\) puede crecer con el tamaño del sufijo y \(R^{\max}_{A_q^{\mathrm{fix}}}=\infty\) cuando la longitud del documento no está acotada. La eliminación produce el mismo resultado por simetría. Una sustitución de igual longitud conserva las fronteras y afecta a lo sumo una vista.

El resultado es análogo al límite de los bloques fijos, pero ahora se aplica solo a la vista derivada; \(\tau_1\) no se ve afectado. Esto confirma que \(G_q>1\) no basta para justificar una vista de ancho fijo si se requiere estabilidad fuerte de la vista. Mantener esta variante puede ser razonable cuando el coste de reconstrucción global es aceptable, pero no satisface el objetivo de actualización local declarado por FKT.

La única excepción estructural ocurre cuando la longitud de cada inserción y eliminación es múltiplo de \(q\). Esa restricción no cubre ediciones locales generales y no puede servir como garantía del sistema.

## Decision

Pending Investigation.

Se demuestra que \(A_q^{\mathrm{fix}}\) ofrece reducción inmediata de elementos, pero falla la cota fuerte de daño de vista para ediciones generales. No se adopta como agrupación local de FKT. La investigación debe evaluar reglas con límites derivados del contenido o con otra estructura de actualización, siempre preservando \(\tau_1\) como representación canónica.

## Impact

Las propuestas futuras deben reportar tanto \(G_q\) como su daño de vista en peor caso. Una mejora de factor de agrupación no podrá presentarse como mejora de localidad si resegmenta un sufijo arbitrario.

## Next Investigation

¿Puede una regla de agrupación definida por contenido con ancho máximo fijo evitar el daño no acotado de \(A_q^{\mathrm{fix}}\) para todas las ediciones locales?

## Status

Status: 🟡 Research
