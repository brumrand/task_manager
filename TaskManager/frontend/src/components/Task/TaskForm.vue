<script setup>
import BaseInput from "../BaseInput.vue";
import BaseSelect from "../BaseSelect.vue";
import { ref } from 'vue';
import axios from 'axios';
const path = "http://localhost:8000/api/v1.0/tasks/";
const optionsArray = [
  { value: 'Personal', text: 'Personal' },
  { value: 'Trabajo', text: 'Trabajo' },
  { value: 'Estudio', text: 'Estudio' },
  { value: 'Otros', text: 'Otros' }
];

const title = ref("");
const description = ref("");
const category = ref("");
const deadline = ref("");
const completed = ref("");

const handleSubmit = async (event) => {
  event.preventDefault(); // Evitar el envío automático del formulario

  
  try {
    // Enviar los datos a través de Axios en una solicitud POST
    const response = await axios.post(path, {
      title,
      description,
      category,
      deadline,
      completed
    });
 
    // Manejar la respuesta exitosa si es necesario
    console.log('Solicitud POST exitosa:', response.data);
  } catch (error) {
    // Manejar el error si ocurre alguno
    console.error('Error al enviar la solicitud POST:', error);
  }
}
</script>
<template >
  <div class="container">
    <h1>Create task form</h1>
    <form  @submit.prevent="handleSubmit" enctype="multipart/form-data" class="form-horizontal">
  <fieldset>
    <BaseInput v-model="title"  type="text" label="Title" name="Title" addClass="form-control"/>
    <BaseInput v-model="description"  type="text" label="Description" name="Description" addClass="form-control"/>
    <BaseSelect v-model="category"  label="Options" name="Description" addClass="form-control" :options="optionsArray"/>
    <BaseInput v-model="deadline"  type="datetime-local" label="Deadline" name="deadline"         addClass="form-control"/>
    <BaseInput v-model="completed"  type="checkbox" label="Completed" name="completed"         />

    <div class="form-group row">
      <div class="col-sm-10 offset-sm-2">
        <button class="btn btn-primary btnSend" title="Make a POST request on the Task List resource">POST</button>
      </div>
    </div>
  </fieldset>
</form>


  </div>

</template>



<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.row{
  margin-top: 10px;
  margin-bottom: 5px;
}
.btnSend{
  width: 100%;
}
h1{
  text-align: center;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}

</style>
