# Fase 4: construcción admisible en un dominio delimitado

## Objective

Construir una agrupación no trivial que cumpla el contrato de admisibilidad, tenga \(G>1\) en un dominio declarado y haga explícitos tanto sus límites como las ediciones para las que ofrece localidad estricta.

## Background

El contrato exige una función total, aunque una garantía de reducción puede declararse para un subdominio. Esto permite distinguir una construcción matemáticamente válida de una solución universal. Los separadores explícitos ofrecen una frontera definida por el contenido cuya estabilidad puede probarse bajo ediciones que preserven esa estructura.

## Hypothesis

Una agrupación parametrizada por un separador \(s\in B\) y longitudes \(2\leq a\leq M\leq255\), con retroceso explícito a tokens unitarios fuera del dominio delimitado, satisface las seis cláusulas. En el subdominio válido alcanza \(G\geq a>1\) y, para ediciones que preservan cada separador y los límites de longitud, tiene \(R\leq M\).

## Analysis

Fíjense los parámetros públicos \(P=(s,a,M)\). Sea \(D_P\) el conjunto de secuencias unitarias que son concatenaciones de grupos no vacíos, cada uno terminado en \(s\), sin otro \(s\) interno y con longitud total entre \(a\) y \(M\), inclusive. Defínase \(A_P(u)\) así: si \(u\in D_P\), devuelve los grupos delimitados; si \(u\notin D_P\), devuelve un grupo unitario por cada token de \(u\). La secuencia vacía pertenece al caso de retroceso y produce la lista vacía.

La función es total, determinista y no usa estado externo. La expansión \(E\) concatena los grupos en orden, por lo que \(E(A_P(u))=u\) tanto en el dominio delimitado como en el retroceso. Cada vista es un intervalo contiguo, no vacío y sin solapamiento. El tamaño máximo es \(S(A_P)=M\) en \(D_P\) y uno fuera de él.

Si \(u\in D_P\) tiene \(n\) tokens y \(r\) grupos, cada grupo contiene al menos \(a\) tokens; por tanto \(r\leq n/a\) y \(G_P(u)=n/r\geq a>1\). La garantía es explícitamente condicional al dominio; fuera de él, \(G_P(u)=1\). Esta diferencia no es un defecto oculto: es parte del contrato de la construcción.

La clase de edición permitida \(\mathcal E_P\) modifica solo tokens internos de un único grupo, no inserta, elimina ni sustituye el separador \(s\), y deja la longitud final de ese grupo entre \(a\) y \(M\). Bajo una edición de \(\mathcal E_P\), todos los grupos posteriores permanecen idénticos bajo la alineación \(\phi_e\). La primera frontera común posterior es el separador del grupo editado, a una distancia de a lo sumo \(M\) desde el final de la edición. En consecuencia, \(R_{A_P}(u,e)\leq M\) y el daño de vista es a lo sumo un grupo.

La construcción demuestra que las seis cláusulas son consistentes y que \(G>1\) puede coexistir con una cota de localidad en un dominio y clase de edición declarados. No resuelve el objetivo universal de FKT: una edición que inserte o elimine un separador, o que haga un grupo demasiado largo o corto, activa el retroceso y puede cambiar muchas vistas. Tampoco añade semántica; el valor \(s\) es simplemente una condición sintáctica fija.

## Decision

Pending Investigation.

La construcción delimitada es una prueba de viabilidad del contrato, no una candidata universal para FKT. Se registra como control positivo: cualquier algoritmo más general debe superar sus restricciones de dominio y edición sin ocultarlas. No se crea ADR ni se autoriza implementación.

## Impact

La investigación dispone de una referencia exacta para distinguir garantías condicionadas de garantías universales. También establece que un factor \(G>1\) no prueba utilidad fundacional si depende de una estructura que la entrada arbitraria no garantiza.

## Next Investigation

¿Puede una agrupación total y no trivial mantener \(G>1\) y una cota de localidad para todas las secuencias de octetos y todas las ediciones locales, sin depender de separadores preservados?

## Status

Status: 🟡 Research
