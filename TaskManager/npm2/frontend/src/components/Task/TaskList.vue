
<script setup>
import { ref } from 'vue'
import axios from 'axios';

const tasks = ref([]);
const title = ref('');
const path = ref('');

// Obtener la URI actual
const currentUri = window.location.pathname;

// Establecer el título y la ruta dependiendo de la URI actual
if (currentUri === "/listLastSevenDays") {
  title.value = "Tabla de Tareas últimos siete días";
  path.value = "http://localhost:8000/api/v1.0/tasksLastSevenDays/";
} else {
  title.value = "Tabla de Tareas";
  path.value = "http://localhost:8000/api/v1.0/tasks/";
}


// Define las funciones
function getTaskData() {
  axios.get(path.value)
    .then((response) => {
      console.log(response.data);
      tasks.value = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
}

function updateTaskData(id) {
  let object  = tasks.value.find(task => task.id === id);
  if(object){
    axios.patch(path.value+id+"/", { completed: !object.completed })
    .then(response => {
      getTaskData();
    })
    .catch(error => {
      
    });
  }
}

function deleteTaskData(id) {
  let object  = tasks.value.find(task => task.id === id);
  if(object){
    axios.delete(path.value+id+"/")
    .then(response => {
      getTaskData();
    })
    .catch(error => {
      
    });
  }
}


// Llama a la función después de definirla
getTaskData();
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
<style scoped>

</style>