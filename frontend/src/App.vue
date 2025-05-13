<template>
  <div v-if="loading">Cargando productos...</div>
  <div v-else>
    <h1>Inventario de Productos</h1>
    <div v-for="p in productos" :key="p.id" style="margin-bottom: 1rem;">
      <strong>{{ p.nombre }}</strong> - Stock: {{ p.stock }} - 
      <span :style="{ color: p.disponible ? 'green' : 'red' }">
        {{ p.disponible ? 'Disponible' : 'Agotado' }}
      </span>
      <div>
        <button @click="modificar(p.id, -1)">Vender</button>
        <button @click="modificar(p.id, 1)">Reponer</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue'
import { useQuery , useMutation} from '@vue/apollo-composable'
import gql from 'graphql-tag'


// GraphQL: Query y Mutación
const QUERY = gql`
  query {
    productos {
      id
      nombre
      stock
      disponible
    }
  }
`

const MUTACION = gql`
  mutation ($id: Int!, $cantidad: Int!) {
    modificarStock(id: $id, cantidad: $cantidad) {
      producto {
        id
        stock
        disponible
      }
    }
  }
`

// Carga de productos
const productos = ref([])
const { result, loading, refetch } = useQuery(QUERY)

watch(result, () => {
  productos.value = result.value?.productos || []
})

// Mutación para cambiar el stock
const { mutate } = useMutation(MUTACION)

function modificar(id, cantidad) {
  mutate({ id, cantidad }).then(() => {
    refetch()
  })
}
</script>
