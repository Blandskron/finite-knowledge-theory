# Fase 4: auditoría de compatibilidad de Chonkers con FKT

## Objective

Evaluar si el preprint Chonkers de 2025 proporciona evidencia suficientemente verificable para adoptar o reutilizar una agrupación con garantías estrictas de tamaño y localidad dentro de FKT.

## Background

La agrupación clásica definida por contenido no ofrece una garantía universal al combinar una marca de ventana y un corte máximo forzado. El preprint *The Chonkers Algorithm* afirma resolver simultáneamente límites estrictos de tamaño y localidad mediante capas de fusiones deterministas [Berger, 2025](https://arxiv.org/abs/2509.11121). Si su modelo fuera compatible con FKT, sería una evidencia relevante para obtener \(G>1\) sin debilitar localidad; si no lo es, sigue siendo una referencia externa útil pero no una decisión fundacional.

## Hypothesis

El material público disponible permite tratar Chonkers como una candidata prometedora, pero no basta para adoptarla en FKT: se necesita una definición autosuficiente de entrada, salida, parámetros, desempates, reconstrucción y límites de localidad expresados con las métricas \(S\), \(D\), \(R\) y \(R^{\max}\) del laboratorio.

## Analysis

La afirmación central del preprint es pertinente: describe una arquitectura por capas con fusiones adyacentes, prioridades y una prueba inductiva de límites de peso y propagación de ediciones. El texto también presenta la fusión como determinista y distingue su enfoque de los métodos clásicos basados en huellas. Esto satisface una condición inicial de interés, pero una afirmación de un preprint no equivale a un contrato FKT verificable.

El determinismo debe poder evaluarse solo a partir de la entrada y parámetros públicos. La descripción disponible menciona prioridades de fusión, reglas de orden y fases de balanceo, *caterpillar* y *diffbit*. Sin una especificación completa de desempates, de la formación de proto-bloques y de los parámetros de cada capa, dos implementaciones independientes podrían tomar decisiones distintas. FKT no puede inferir esos detalles desde una implementación de referencia.

La reconstrucción parece inferible: si las fases únicamente fusionan fragmentos adyacentes sin descartarlos, expandir las fusiones en orden conserva la secuencia original. Sin embargo, esa propiedad debe formularse como un invariante explícito \(E(A(x))=x\), incluyendo entradas vacías, secuencias repetitivas, límites de capa y errores. El material revisado no ofrece una especificación de entrada/salida en el formato independiente de implementación que requiere FKT.

La ausencia de estado oculto tampoco queda demostrada. El preprint presenta un árbol de fusión y una estructura Yarn para deduplicación y actualizaciones; además, deriva detalles de reconstrucción de árbol hacia la implementación de referencia. Es posible que el algoritmo de agrupación sea funcional con parámetros fijos, pero esa es una inferencia no verificada. La identidad de objetos, cachés, hashes o el historial de actualizaciones no pueden afectar la salida canónica si FKT llega a adoptar una regla.

Por último, las garantías de Chonkers se expresan en su propia noción de peso y capas. Para ser comparables con FKT deben traducirse a un máximo de carga \(S\), una definición de edición compatible y una cota concreta de \(R^{\max}\). El preprint afirma pruebas inductivas y resultados estrictos; el laboratorio aún debe reconstruir o verificar esas pruebas para los parámetros que usaría, en vez de importar la conclusión por autoridad.

## Decision

Pending Investigation.

Chonkers se registra como candidata externa para estudio, no como componente adoptado. El preprint aporta una dirección plausible para superar el límite de la segmentación clásica, pero no satisface todavía los requisitos de especificación autosuficiente, trazabilidad de parámetros y verificación independiente exigidos por FKT. No se crea ADR, no se promociona conocimiento y no se autoriza implementación.

## Impact

La investigación pasa de comparar heurísticas a exigir un contrato formal de cualquier algoritmo con garantías estrictas. Una eventual adaptación deberá preservar \(\tau_1\) como representación canónica y demostrar que la vista derivada se calcula sin estado dependiente de historial.

## Next Investigation

¿Puede formularse un subconjunto autosuficiente de Chonkers, con parámetros finitos y reglas de desempate completas, cuya reconstrucción y cota de localidad se demuestren directamente en las métricas de FKT?

## Status

Status: 🟡 Research
