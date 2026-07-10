# Fase 5: auditoría de fuente de Chonkers

## Objective

Actualizar la evaluación de compatibilidad de Chonkers con FKT mediante inspección de solo lectura de su implementación pública de referencia.

## Background

La auditoría inicial se limitó al preprint y concluyó que faltaba una definición autosuficiente. La implementación pública Java de Chonkers está disponible en GitHub y organiza el algoritmo como árbol, configuración por capas, fusión y reagrupación. La inspección no ejecuta ni incorpora código externo.

## Hypothesis

La fuente pública hará visibles parámetros y mecanismos de capas suficientes para mejorar la trazabilidad, pero no demostrará por sí sola que la salida de agrupación sea una función pura de la entrada y parámetros de FKT.

## Analysis

El repositorio público identifica una implementación de referencia Java y expone módulos de árbol, configuración, *caterpillar*, *diffbits*, reagrupación y Yarn [repositorio de Chonkers](https://github.com/ichteltelch/chonkers). La configuración contiene una secuencia explícita de longitudes de *diffbits*, tamaños de unidad absoluta por capa y selección de configuración orientada a bytes [ChonkerConfig.java](https://github.com/ichteltelch/chonkers/blob/master/src/ds/chonker/tree/ChonkerConfig.java). Esto aporta evidencia de parámetros finitos y de un diseño multicapa, superando el nivel de detalle disponible en el resumen del preprint.

La misma fuente muestra que la concatenación delega en una fase `Rechonker` sobre extremos de árboles y que la configuración mantiene mapas concurrentes de canonicalización para nodos y datos monoidales. También utiliza una envoltura de identidad de referencia en esa canonicalización. Estos elementos pueden ser optimizaciones internas correctas, pero impiden inferir desde la lectura que dos historiales de construcción de la misma secuencia produzcan siempre la misma agrupación observable.

La existencia de parámetros por capa no basta para el contrato FKT. Todavía faltan: una definición independiente de entrada y salida; el conjunto completo de desempates; una prueba trazable de \(E(A_P(u))=u\); una traducción de los límites de peso a \(S\), \(D\), \(R\) y \(R^{\max}\); y una prueba o experimento que compare historiales de construcción. Ejecutar la fuente externa no está autorizado ni es necesario para esta conclusión.

La auditoría sí modifica una incertidumbre anterior: Chonkers no es solo una afirmación de preprint sin artefacto; existe una implementación pública concreta con configuración de capas y una arquitectura de reagrupación. Sin embargo, el artefacto Java sigue siendo una implementación de referencia externa, no una especificación independiente de lenguaje y no puede convertirse directamente en código o teoría FKT.

## Decision

Pending Investigation.

Chonkers permanece como candidata externa de alta prioridad para auditoría, con evidencia adicional de parámetros multicapa. No se adopta porque canonicidad, reconstrucción y límites FKT no han sido demostrados de forma independiente. No se crea ADR ni se incorpora código externo.

## Impact

Una futura investigación puede formular un experimento de caja negra que construya la misma secuencia por rutas distintas y compare su agrupación, siempre que se especifique la salida observable y se mantenga el aislamiento experimental. Hasta entonces, las conclusiones de FKT siguen basadas en sus propios controles reproducibles.

## Next Investigation

¿Qué salida observable y qué pares de historiales deben definirse para probar experimentalmente la independencia de historial de una agrupación multicapa?

## Status

Status: 🟡 Research
