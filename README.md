# practica2PRGWebII respuestas:

## ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

GraphQL permite consultar exactamente los campos necesarios, evitando el exceso de datos. Además, con una única solicitud se pueden realizar múltiples operaciones (consulta y mutación), ideal para interfaces reactivas como Vue, donde los datos pueden cambiar dinámicamente.

## ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

Los tipos se definen como clases que heredan de `graphene.ObjectType`, y sus campos son atributos de clase. Los resolvers son métodos asociados a las consultas o mutaciones, normalmente prefijados con `resolve_`.

## ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

Porque el backend debe ser la fuente de verdad. Si la lógica de disponibilidad está solo en el frontend, otros clientes o integraciones podrían corromper los datos al omitir esa lógica. Centralizar la lógica garantiza integridad y consistencia.

## ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

Incorporando esa lógica directamente en el método de mutación del backend (`modificar_stock`), donde se controla que:
- El stock no sea negativo.
- La disponibilidad (`disponible`) cambie en función del stock.
Así, cualquier modificación al inventario pasa por esta validación.
