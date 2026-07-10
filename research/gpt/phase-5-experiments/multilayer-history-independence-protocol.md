# Fase 5: protocolo de independencia de historial multicapa

## Objective

Definir una prueba de caja negra para decidir si una agrupación multicapa observable es canónica, es decir, independiente de la ruta por la que se construye una misma secuencia final.

## Background

La fuente de Chonkers muestra capas, árboles y una fase de reagrupación, pero no permite concluir desde inspección estática que la vista final sea una función pura. Las estructuras dependientes de historial pueden mantener localidad de actualización y aun así producir agrupaciones distintas para el mismo contenido. Se requiere un protocolo que distinga esas posibilidades sin depender de identidades internas ni cachés.

## Hypothesis

Si una agrupación multicapa es canónica, entonces para una misma entrada final \(y\), configuración pública \(P\) y capa observable \(\ell\), toda ruta de construcción producirá la misma secuencia ordenada de intervalos de octetos en esa capa.

## Analysis

La salida observable mínima por capa será una lista \(B_\ell(y)\) de intervalos \([inicio,fin)\), expresados en coordenadas de la secuencia final. Cada intervalo debe incluir su longitud, orden y opcionalmente una etiqueta de capa; no debe incluir direcciones de memoria, hashes de identidad, cachés ni IDs de nodo. La expansión de todos los intervalos de la capa base debe reconstruir \(y\). Si una implementación no puede exponer esta salida, no puede demostrar conformidad con el contrato FKT.

El protocolo compara cuatro rutas con la misma configuración \(P\). La ruta directa construye \(y\) en una sola operación. La ruta de inserción construye un prefijo y sufijo, los concatena y luego inserta un fragmento intermedio. La ruta de concatenación construye los fragmentos de \(y\) por separado y los concatena. La ruta de edición construye una secuencia cercana \(x\), aplica sustituciones, inserciones o eliminaciones y alcanza \(y\). Tras normalizar las coordenadas a \(y\), el protocolo exige \(B_\ell^{directa}(y)=B_\ell^{inserción}(y)=B_\ell^{concatenación}(y)=B_\ell^{edición}(y)\) para cada capa \(\ell\) declarada.

Los datos de prueba deben incluir cadenas vacías, constantes, alternantes, periódicas, no repetitivas y límites de tamaño alrededor de cada unidad absoluta configurada. Las rutas deben insertar en inicio, centro y final; las cadenas periódicas son especialmente importantes porque activan mecanismos de repetición y desempates. Cada caso registra además reconstrucción exacta, tamaño máximo por capa y la primera frontera común tras la edición.

Un desacuerdo entre rutas refuta canonicidad de la vista observable, aunque todas reconstruyan correctamente el contenido. Una coincidencia en un conjunto finito de casos no demuestra universalidad, pero aporta evidencia reproducible y puede revelar parámetros o desempates no declarados. El protocolo no exige ejecutar Chonkers ni adoptar su código; es un contrato de ensayo para cualquier algoritmo multicapa candidato.

## Decision

Pending Investigation.

Se propone este protocolo como requisito previo para afirmar independencia de historial de una agrupación multicapa. No se ejecuta aún contra código externo, no se adopta Chonkers y no se crea ADR.

## Impact

FKT puede evaluar una construcción compleja por su salida canónica, sin depender de la representación interna elegida por un lenguaje. Un experimento futuro deberá implementar o adaptar el protocolo solo con autoridad explícita para analizar un candidato concreto.

## Next Investigation

¿Autoriza el usuario un experimento aislado que implemente este protocolo sobre una construcción multicapa propia, sin ejecutar ni copiar la implementación externa de Chonkers?

## Status

Status: 🟡 Research
