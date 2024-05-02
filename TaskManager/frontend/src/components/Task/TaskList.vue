<script setup>
import { ref, computed, onMounted } from 'vue';
import axios from 'axios';
import { useStore } from 'vuex';

const store = useStore(); // Importa el store Vuex
const tasks = computed(() => store.state.data);
const title = computed(() => store.state.title);
const generalPath = 'http://localhost:8000/api/v1.0/tasks/';

onMounted(() => {
  console.log(title)
  store.dispatch('fetchData');
});
// Función para actualizar datos de tarea
function updateTaskData(id) {
  let object = tasks.value.find(task => task.id === id);
  if (object) {
    axios.patch(generalPath + id + "/", { completed: !object.completed })
      .then(response => {
        store.dispatch('fetchData');
      })
      .catch(error => {
        console.error('Error al actualizar datos de tarea:', error);
      });
  }
}

// Función para eliminar datos de tarea
function deleteTaskData(id) {
  let object = tasks.value.find(task => task.id === id);
  if (object) {
    axios.delete(generalPath + id + "/")
      .then(response => {
        store.dispatch('fetchData');
      })
      .catch(error => {
        console.error('Error al eliminar datos de tarea:', error);
      });
  }
}
</script>


<template>
  <div class="container">
    <h1>{{ title }}</h1>
    <table class="table">
      <thead>
        <tr>
          <th>ID</th>
          <th>Título</th>
          <th>Descripción</th>
          <th>Categoría</th>
          <th>Fecha límite</th>
          <th>Completada</th>
          <th>Cambiar estado</th>
          <th>Borrar</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="task in tasks" :key="task.id">
          <td>{{ task.id }}</td>
          <td>{{ task.title }}</td>
          <td>{{ task.description }}</td>
          <td>{{ task.category }}</td>
          <td>{{ task.deadline }}</td>
          <td>{{ task.completed ? 'Sí' : 'No' }}</td>
          <td><button class="btn btn-primary" @click="updateTaskData(task.id)">Actualizar estado</button></td>
          <td><button class="btn btn-primary" @click="deleteTaskData(task.id)">Borrar</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
