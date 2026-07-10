# exp-003: resultados del control multicapa canónico

## Objective

Registrar la ejecución del protocolo de independencia de historial sobre la construcción multicapa por mitades.

## Background

La construcción recibe exclusivamente los bytes finales y construye intervalos por división recursiva. Es un control de canonicidad, no una propuesta de agrupación local.

## Hypothesis

Las rutas directa, de inserción, de concatenación y de edición producirán capas observables idénticas para la misma secuencia final.

## Analysis

Ejecutado el 2026-07-09 con el runtime Python empaquetado. Las 17 pruebas combinadas pasaron. Para la secuencia final `b"aXbcd"`, las cuatro rutas produjeron la misma jerarquía:

```text
layers=(((0, 5),), ((0, 2), (2, 5)), ((0, 1), (1, 2), (2, 3), (3, 5)), ((3, 4), (4, 5)))
leaves=((0, 1), (1, 2), (2, 3), (3, 4), (4, 5))
```

Las hojas reconstruyeron la secuencia final para longitudes de uno a dieciséis. Una inserción cambia la jerarquía cuando modifica la longitud total, por ejemplo la raíz cambia de \([0,8)\) a \([0,9)\). Por eso el control demuestra independencia de historial, pero no localidad de actualización.

## Decision

Pending Investigation.

El protocolo de historial queda validado por un caso positivo autocontenido. La construcción por mitades no se adopta como agrupación FKT porque su normalización global puede modificar capas internas tras una edición.

## Impact

Futuros candidatos multicapa podrán compararse contra este control: deben conservar la igualdad entre rutas y, además, demostrar una mejor cota de cambio tras ediciones.

## Next Investigation

¿Qué invariante multicapa puede limitar el cambio tras una edición sin perder la igualdad entre rutas de construcción?

## Status

Status: 🟡 Research
