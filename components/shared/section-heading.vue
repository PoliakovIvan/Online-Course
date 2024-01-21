<script setup>
defineProps({
  title: {
    type: String,
    required: true
  },
  subtitle: {
    type: String
  }
})
</script>

<template>
  <div class="heading">
    <p class="heading__subtitle"> {{ subtitle }}</p>
    <h2 class="heading__title">{{ title }}</h2>
  </div>
</template>