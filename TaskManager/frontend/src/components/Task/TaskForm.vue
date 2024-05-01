<template >
  <div class="container">
    <h1>Create task form</h1>
    <form action="/api/v1.0/tasks/" method="POST" enctype="multipart/form-data" class="form-horizontal" novalidate="">
  <fieldset>
    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Title</label>
      <div class="col-sm-10">
        <input name="title" class="form-control" type="text" value="">
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Description</label>
      <div class="col-sm-10">
        <textarea name="description" class="form-control"></textarea>
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Category</label>
      <div class="col-sm-10">
        <select class="form-control" name="category">
          <option value="Personal">Personal</option>
          <option value="Trabajo">Trabajo</option>
          <option value="Estudio">Estudio</option>
          <option value="Otros">Otros</option>
        </select>
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Deadline</label>
      <div class="col-sm-10">
        <input name="deadline" class="form-control" type="datetime-local" value="">
      </div>
    </div>

    <div class="form-group row">
      <label class="col-sm-2 col-form-label">Completed</label>
      <div class="col-sm-10">
        <input type="checkbox" name="completed" value="true">
      </div>
    </div>

    <div class="form-group row">
      <div class="col-sm-10 offset-sm-2">
        <button class="btn btn-primary btnSend" title="Make a POST request on the Task List resource">POST</button>
      </div>
    </div>
  </fieldset>
</form>


  </div>

</template>

<script>
export default {

}
</script>

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
