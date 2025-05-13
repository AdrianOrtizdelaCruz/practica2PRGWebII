# Instrucciones de Uso:

# 🛍️ Backend Flask + GraphQL + Vue Frontend - Inventario de Productos

Este proyecto implementa el backend de una tienda online con **Flask** y **GraphQL**, conectado a un frontend en **Vue** que muestra productos de manera reactiva según su disponibilidad.

---

## 📦 Requisitos

### 🔧 Backend (Flask + GraphQL)

- Python 3.8 o superior
- pip
- (opcional) Entorno virtual `venv`

### 🌐 Frontend (Vue)

- Node.js y npm
- Vue 3 + Vite

---

## 🚀 Instalación y Ejecución del Backend

1. Clona el proyecto y accede al directorio `backend`:
cd backend/

2.Crea un entorno virtual (opcional):

python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

3.Instala las dependencias:

pip install -r requirements.txt

4.Ejecuta el servidor:

python app.py

El backend está disponible en:
http://localhost:5000/graphql

🎯 Funcionalidad del Backend
📌 Datos en memoria
Los productos se almacenan en una lista de Python al iniciar el servidor, con campos:

id (int)

nombre (str)

precio (float)

stock (int)

disponible (bool) → se actualiza automáticamente según el stock.

🔍 Query GraphQL
query {
  productos {
    id
    nombre
    precio
    stock
    disponible
  }
}

✏️ Mutación GraphQL
mutation {
  modificarStock(id: 1, cantidad: -3) {
    id
    stock
    disponible
  }
}

🔗 Conexión con el Frontend Vue
En el frontend (frontend/src/apollo.js), uri apuntando al backend:

import { ApolloClient, InMemoryCache } from '@apollo/client/core'

export const apolloClient = new ApolloClient({
  uri: 'http://localhost:5000/graphql',
  cache: new InMemoryCache(),
})
En main.ts:
import { createApp, h, provide } from 'vue'
import App from './App.vue'
import { DefaultApolloClient } from '@vue/apollo-composable'
import { apolloClient } from './apollo'

createApp({
  setup() {
    provide(DefaultApolloClient, apolloClient)
  },
  render: () => h(App),
}).mount('#app')

En App.vue, usa las queries y mutaciones:
import { useQuery, useMutation } from '@vue/apollo-composable'
import gql from 'graphql-tag'

⚠️ Instala estas dependencias si no las tienes:
npm install @apollo/client graphql graphql-tag @vue/apollo-composable

🧪 Test opcional del backend
Puedes ejecutar el archivo test.py (si existe) para comprobar funcionalidad:
python test.py

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
