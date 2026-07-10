# Fase 5: límite de agrupación canónica de radio finito

## Objective

Caracterizar una limitación de reglas puras que deciden cada frontera mediante una ventana local de radio finito e invariancia por desplazamiento.

## Background

Las reglas clásicas de marca de ventana pertenecen a una familia más amplia: para decidir una frontera interior, inspeccionan una cantidad fija de octetos alrededor de esa posición y aplican la misma función en cada desplazamiento. Son canónicas porque dependen solo de la entrada, pero el requisito de tamaño máximo y agrupación no trivial debe analizarse también en entradas altamente simétricas.

## Hypothesis

Toda regla de frontera interior, pura, invariante por desplazamiento y de radio finito que garantice grupos de tamaño máximo finito debe producir fronteras en cada posición interior de una secuencia constante suficientemente larga. Por tanto, su factor de agrupación es uno en esa familia de entradas.

## Analysis

Sea \(F\) una función booleana que decide si existe una frontera tras una posición interior usando una ventana de radio \(r\): los \(2r+1\) octetos centrados en la posición. La invariancia por desplazamiento exige que dos posiciones con la misma ventana reciban la misma respuesta. Considérese una cadena constante \(c^n\), con \(n\) mucho mayor que \(2r\) y que el máximo \(M\) declarado.

En todas las posiciones interiores alejadas de los extremos, la ventana observada por \(F\) es idéntica: \(c^{2r+1}\). Por invariancia, la decisión también es idéntica en todas ellas. Hay solo dos casos. Si \(F\) devuelve falso, aparece un tramo interior sin fronteras de longitud arbitraria al aumentar \(n\); esto contradice un tamaño máximo \(M\) independiente de \(n\). Si \(F\) devuelve verdadero, hay una frontera tras cada octeto interior y todos los grupos interiores tienen longitud uno.

La conclusión se limita a reglas con radio fijo e invariancia por desplazamiento. No demuestra que toda regla canónica no trivial sea imposible. Una regla puede usar mecanismos no locales, múltiples capas, prioridades globales o una prueba distinta de límites; Chonkers se presenta como ejemplo externo de una dirección más compleja, aún no verificada para FKT. Tampoco impide agrupación no trivial en entradas no constantes.

Sin embargo, el resultado elimina una expectativa común: una condición local uniforme no puede ofrecer simultáneamente máxima longitud finita y una reducción mínima mayor que uno en toda entrada. En particular, usar una huella de ventana más sofisticada no resuelve por sí solo el caso de simetría; si no hay distinción local, la regla debe cortar siempre o aceptar tramos arbitrarios.

## Decision

Pending Investigation.

Se establece este límite para la clase de reglas de radio finito e invariancia por desplazamiento. FKT no adoptará una regla de esa clase como solución universal de agrupación no trivial sin declarar que las secuencias constantes caen al caso unitario. No se crea ADR ni se promueve conocimiento compartido.

## Impact

Los próximos candidatos deben identificar explícitamente qué mecanismo rompe o supera esta hipótesis: no localidad, capas, prioridades, una condición de dominio o una renuncia al factor de agrupación mínimo universal. Esto reduce el espacio de búsqueda sin confundir una restricción de clase con una imposibilidad general.

## Next Investigation

¿Puede una construcción canónica de múltiples capas superar el límite de radio finito y demostrar sus cotas sin introducir estado oculto?

## Status

Status: 🟡 Research
