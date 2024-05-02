<script setup>
import BaseInput from "../BaseInput.vue";
import BaseSelect from "../BaseSelect.vue";
import { ref, reactive } from 'vue';
import axios from 'axios';
import { useVuelidate } from '@vuelidate/core'
import { required, maxLength, minLength } from '@vuelidate/validators'

const path = "http://localhost:8000/api/v1.0/tasks/";
const optionsArray = [
  { value: 'Personal', text: 'Personal' },
  { value: 'Trabajo', text: 'Trabajo' },
  { value: 'Estudio', text: 'Estudio' },
  { value: 'Otros', text: 'Otros' }
];
let flag = true;

const formData = reactive({
  title: "",
  description: "",
  category: "",
  deadline: "",
  completed: "",
});
const rules = {
  title: {
    required,
    minLength: minLength(3),
    maxLength: maxLength(50)
  },
  description: {
    required,
    minLength: minLength(3),
    maxLength: maxLength(255)
  },
  category: { required },
  deadline: { required }
};
const v$ = useVuelidate(rules, formData);

const handleSubmit = async (event) => {
  event.preventDefault(); // Evitar el envío automático del formulario
  let validator = await v$.value.$validate();
  let errrr = await v$.errors;
  if (validator) {

    try {
      // Enviar los datos a través de Axios en una solicitud POST
      const response = await axios.post(path, {
        title: formData.title,
        description: formData.description,
        category: formData.category,
        deadline: formData.deadline,
        completed: formData.completed !== ""
      });

      // Manejar la respuesta exitosa si es necesario
      console.log('Solicitud POST exitosa:', response.data);
      alert("Solicitud enviada con éxito")
      formData.title = "",
        formData.description = "",
        formData.category = "",
        formData.deadline = "",
        formData.completed = ""
    } catch (error) {
      // Manejar el error si ocurre alguno
      console.error('Error al enviar la solicitud POST:', error);
    }
  } else {
    console.log(errrr)
    alert("Error al enviar el formulario:")
  }


}
</script>
<template>
  <div class="container">
    <h1>Create task form</h1>
    <form @submit.prevent="handleSubmit" enctype="multipart/form-data" class="form-horizontal">
      <fieldset>
        <BaseInput v-model="formData.title" type="text" label="Title" name="Title" :addClass="flag" />
        <BaseInput v-model="formData.description" type="text" label="Description" name="Description" :addClass="flag" />
        <BaseSelect v-model="formData.category" label="Options" name="Description" :addClass="flag"
          :options="optionsArray" />
        <BaseInput v-model="formData.deadline" type="datetime-local" label="Deadline" name="deadline"
          :addClass="flag" />


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
.row {
  margin-top: 10px;
  margin-bottom: 5px;
}

.btnSend {
  width: 100%;
}

h1 {
  text-align: center;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif;
}
</style>
