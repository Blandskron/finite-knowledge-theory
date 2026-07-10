# Fase 4: métricas formales de localidad de edición

## Objective

Definir criterios matemáticos para medir cuánto cambia una tokenización tras una edición local, de modo que la comparación entre bloques fijos y reglas definidas por contenido sea verificable y no dependa de ejemplos aislados.

## Background

El baseline \(\tau_M\) aprobado para investigación es reversible y determinista, pero una inserción o eliminación puede alterar todo el sufijo. Decir que otro método “es más local” es ambiguo: puede referirse a límites, tokens, bytes serializados, tiempo de actualización o probabilidad de resincronización. FKT necesita separar esas propiedades antes de elegir una regla.

## Hypothesis

Una métrica suficiente para esta etapa combina cuatro cantidades: tamaño máximo de bloque, número de tokens afectados, distancia de resincronización y comportamiento de peor caso. El requisito mínimo de localidad debe expresarse como una cota independiente de la longitud total del documento; una mejora solo esperada o promedio debe declararse explícitamente como tal.

## Analysis

Sea \(\tau\) un tokenizador reversible sobre secuencias de octetos y sea \(e\) una edición que transforma \(x\) en \(y=e(x)\). La edición identifica un intervalo modificado y una biyección de coordenadas \(\phi_e\) entre el prefijo y sufijo no modificados de \(x\) e \(y\). Esta alineación evita confundir el desplazamiento físico producido por una inserción con un cambio de contenido.

Se definen cuatro medidas. El tamaño máximo \(S(\tau)\) es la mayor longitud de carga que \(\tau\) permite en cualquier token. El daño de tokens \(D_\tau(x,e)\) es el número de tokens que no pueden conservarse idénticos al comparar \(\tau(x)\) y \(\tau(y)\) fuera del intervalo editado, usando \(\phi_e\) para alinear el sufijo. La distancia de resincronización \(R_\tau(x,e)\) es la menor cantidad de bytes no modificados desde el final de la edición hasta una frontera común alineada, a partir de la cual ambas tokenizaciones son idénticas; toma el valor \(\infty\) si no existe tal frontera antes del final del documento. Finalmente, el peor caso de resincronización es \(R^{\max}_\tau = \sup_{x,e} R_\tau(x,e)\), sobre las entradas y ediciones admitidas.

Estas definiciones permiten clasificar resultados sin mezclar garantías. Para bloques fijos, \(S(\tau_M)=M\). Una sustitución de igual longitud tiene \(D_{\tau_M}\leq 1\) y \(R_{\tau_M}=0\) fuera del bloque afectado. Para una inserción de longitud no múltiplo de \(M\), existen entradas donde no reaparece una frontera alineada antes del final, de modo que \(R_{\tau_M}\) puede crecer con el sufijo y \(R^{\max}_{\tau_M}=\infty\) si la longitud del documento no está acotada.

La propuesta de requisito mínimo para evaluar una alternativa es: (1) \(S(\tau)\leq M\) para un parámetro público fijado; (2) reconstrucción exacta y determinismo; y (3) una de dos declaraciones excluyentes. Una garantía fuerte exhibe una constante \(C\), independiente de \(|x|\), tal que \(R_\tau(x,e)\leq C\) para toda edición permitida. Una garantía empírica o probabilística debe declarar distribución de entradas, parámetros y percentiles; no puede presentarse como garantía fundacional.

La métrica no impone todavía que FKT alcance una garantía fuerte. Su valor inmediato es revelar que el baseline fijo cumple las propiedades de representación y tamaño, pero no la propiedad de localidad fuerte. La comparación futura deberá considerar además si la complejidad y las nuevas reglas introducidas justifican el beneficio.

## Decision

Pending Investigation.

Se propone usar \(S\), \(D\), \(R\) y \(R^{\max}\) como vocabulario y criterio de evaluación para la Fase 4. Falta analizar si existe una regla de segmentación determinista sobre la gramática aprobada que satisfaga una cota fuerte útil, o si FKT debe aceptar una garantía probabilística declarada. No se adopta una regla ni se crea ADR.

## Impact

Los futuros experimentos podrán reportar resultados comparables: tamaño de bloque, tokens afectados, distancia hasta resincronización y caso peor. Esto hace auditable cualquier reclamación de estabilidad local y evita confundir una mejora de rendimiento o deduplicación con una propiedad de la representación.

## Next Investigation

¿Existe una regla determinista de segmentación sobre octetos con tamaño máximo fijo y una cota de resincronización independiente de la longitud del documento para toda edición local?

## Status

Status: 🟡 Research
