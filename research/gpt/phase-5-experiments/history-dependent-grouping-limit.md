# Fase 5: límite de agrupación dependiente de historial

## Objective

Determinar si una estructura que conserva grupos mediante actualizaciones locales puede servir como vista canónica de FKT o debe quedar restringida a una optimización dependiente de historial.

## Background

Los controles de Fase 5 muestran que las reglas canónicas de bloques fijos o marca forzada pueden resegmentar sufijos. Una estructura persistente puede evitar ese coste conservando grupos existentes y modificando solo un vecindario local. Esa ventaja parece resolver localidad, pero debe contrastarse con la cláusula de canonicidad: misma entrada y mismos parámetros deben producir la misma vista, sin importar el historial.

## Hypothesis

Una agrupación que privilegia conservar grupos previos puede lograr actualizaciones locales, pero no puede ser canónica si dos historiales que producen la misma secuencia final conservan particiones diferentes.

## Analysis

Considérese una capacidad máxima de cuatro octetos. La construcción directa canónica de \(y=\texttt{aXbcd}\) por corte fijo desde la izquierda produce \((\texttt{aXbc},\texttt{d})\). Ahora considérese otro historial: primero se construye \(x=\texttt{abcd}\) como \((\texttt{abcd})\); después se inserta \(\texttt{X}\) tras \(\texttt{a}\). Una política de actualización local que conserve el grupo existente puede dividir el grupo desbordado de cinco octetos de forma balanceada y producir \((\texttt{aX},\texttt{bcd})\).

Ambas vistas expanden a la misma secuencia \(y\), tienen cargas dentro del máximo y difieren solo localmente entre versiones. Sin embargo, no son iguales entre sí. Si la salida depende de si \(y\) se construyó directamente o mediante una inserción, no existe una función pura \(A_P(y)\): existe una función de \((y,\text{historial})\). Eso viola la tercera cláusula del contrato de admisibilidad.

La observación no invalida árboles balanceados, *ropes*, cachés ni estructuras persistentes. Esas estructuras pueden ser excelentes mecanismos de almacenamiento o actualización sobre la secuencia canónica \(\tau_1\). Su agrupación debe tratarse como estado derivado, identificable por versión o historial, y nunca como la serialización canónica de conocimiento. Para FKT, su costo y localidad pueden medirse como propiedades de una implementación experimental, no como propiedades de la representación fundacional.

El ejemplo también aclara una alternativa legítima: exigir una normalización global después de cada edición restauraría canonicidad, pero puede destruir la ventaja de actualización local. El conflicto no se resuelve ocultando el historial; debe elegirse explícitamente qué capa posee cada propiedad.

## Decision

Pending Investigation.

Las agrupaciones dependientes de historial quedan excluidas como candidatas a vista canónica de FKT mientras no demuestren independencia total del historial. Pueden investigarse como cachés o índices derivados, siempre que su salida no se confunda con \(A_P(u)\) ni con la representación compartida.

## Impact

La búsqueda de una agrupación universal debe permanecer en reglas puras de entrada y parámetros públicos. Los futuros experimentos de estructuras persistentes deberán incluir una prueba de convergencia canónica o declarar explícitamente que solo evalúan una optimización de implementación.

## Next Investigation

¿Puede una regla pura y canónica con grupos no unitarios demostrar localidad estricta universal sin recurrir a historial ni a cortes forzados?

## Status

Status: 🟡 Research
