# Fase 4: separación entre tokenización fundacional y agrupación derivada

## Objective

Determinar qué objetivo no semántico puede justificar grupos mayores que un octeto sin convertir la agrupación en una propiedad fundacional ni debilitar la localidad fuerte de la representación base.

## Background

La construcción \(\tau_1\) resuelve la representación y la localidad fuerte: cada octeto conserva un token independiente y \(R^{\max}=0\). Los bloques mayores pueden disminuir el número de elementos que una capa superior debe recorrer, pero también introducen límites que cambian tras ediciones. La pregunta no es si agrupar es posible, sino en qué capa pertenece y qué propiedad medible aporta.

## Hypothesis

La agrupación de más de un octeto solo se justifica como una vista derivada con un objetivo operacional explícito —reducir la cantidad de elementos inmediatos para navegación, indexación o procesamiento por lotes—. La tokenización fundacional debe permanecer como \(\tau_1\); una agrupación no debe reemplazarla ni definir unidades semánticas.

## Analysis

Sea \(u=\tau_1(x)\) la secuencia canónica de tokens unitarios de una entrada \(x\). Una agrupación derivada \(A_q\) con parámetro \(q>1\) particiona \(u\) en vistas ordenadas de entre uno y \(q\) tokens unitarios. Debe existir una operación de expansión \(E\) tal que \(E(A_q(u))=u\). Esta igualdad asegura que la agrupación no crea una nueva representación de la entrada: es una organización adicional de una secuencia ya definida.

El objetivo medible es el factor de reducción de elementos inmediatos \(G_q(x)=|u|/|A_q(u)|\). Para una agrupación completa de ancho \(q\), \(|A_q(u)|=\lceil |u|/q\rceil\), por lo que \(G_q(x)\) se aproxima a \(q\) en entradas largas. Esta propiedad puede reducir el número de referencias que una operación de nivel superior debe inspeccionar. No es compresión: si se serializan cabeceras, el tamaño en bytes puede aumentar. Tampoco es semántica: dos grupos no adquieren significado por contener varios octetos.

La localidad fuerte de \(\tau_1\) permanece intacta porque se mide en la secuencia canónica \(u\), no en la vista \(A_q(u)\). Una inserción puede cambiar muchas fronteras de una agrupación fija, pero no altera los tokens unitarios no editados. Por consiguiente, el daño de la vista debe reportarse por separado y nunca presentarse como daño de la capa fundacional.

Esta separación impone una disciplina útil. Si una propuesta necesita agrupar para rendimiento, debe declarar su parámetro, regla de construcción, coste de expansión, factor \(G_q\) y sensibilidad de sus fronteras. Si una propuesta pretende sustituir tokens unitarios por bloques mayores, debe demostrar una propiedad adicional que compense la pérdida de localidad; la mera reducción de cantidad de tokens no basta para modificar la fundación.

La agrupación puede representarse como listas de vistas o árboles de aridad finita. Esos objetos pueden tener profundidad dependiente de la longitud de un documento; por eso deben tratarse como estructuras derivadas, no como evidencia de un número finito de niveles fundacionales. El conjunto de tipos de agrupación puede seguir siendo finito aunque el número de instancias o la profundidad de una estructura no lo sea.

## Decision

Pending Investigation.

Se propone la separación \(\tau_1\) como capa canónica y \(A_q\) como vista derivada para evaluar cualquier beneficio de agrupación sin sacrificar la garantía ya demostrada. Falta demostrar que un esquema concreto de agrupación aporta valor suficiente y definir sus límites de actualización. No se adopta \(A_q\), no se crea ADR y no se autoriza implementación.

## Impact

Las futuras propuestas podrán comparar rendimiento estructural mediante \(G_q\) sin reabrir la definición de la primitiva. La especificación, si llega a existir, deberá distinguir representación canónica, vistas derivadas y significado semántico para no mezclar responsabilidades.

## Next Investigation

¿Puede una agrupación derivada determinista de ancho acotado ofrecer un factor \(G_q>1\) y una cota explícita de daño de vista tras una edición local?

## Status

Status: 🟡 Research
