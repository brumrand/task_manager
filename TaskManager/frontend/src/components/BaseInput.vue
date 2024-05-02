<template>
  <div class="form-group row">
    <label class="col-sm-2 col-form-label">{{ label }}</label>
    <div class="col-sm-10">
      <input addClass="form-control" :class="{ 'form-control ': addClass }" :value="modelValue"
        @input="$emit('update:modelValue', $event.target.value)" v-bind="$attrs">
    </div>
  </div>

</template>

<script setup>
defineProps({
  label: {
    type: String,
    default: ""
  },
  addClass: {
    type: [Boolean]
  },
  modelValue: {
    type: String,
    default: ""
  },
})

</script>

<style scoped></style>
