<template>
 <div class="container">
  <div class="row">
    <div class="col text-left">
      <h1>Task List</h1>
    </div>
    <div class="col-md-12">
      <b-table striped hover :items="tasks" :fields="fields">
      </b-table>

    </div>
  </div>
 </div>



</template>

<script>
import axios from 'axios';

export default {
  data(){
    return{
      fields: [
        {key:"id",  label:"Id"},
        {key:"title",  label:"Title"},
        {key:"description",  label:"Description"},
        {key:"category",  label:"Category"},
        {key:"deadline",  label:"Deadline"},
        {key:"completed",  label:"Completed"}
      ],
      tasks: []
    }
  },
  methods: {
    getTasks () {
      const path = "localhost:8000/api/v1.0/tasks";
      axios.get(path).then((response)=>{
        this.tasks = response.data
      }).catch((error) =>{
        console.log(error)
      });
  }
  },
  created(){
    this.getBooks()
  }



}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
