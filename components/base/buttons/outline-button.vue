<script setup>
defineProps({
  text: {
    type: String,
    default: "View All"
  },
  url: {
    type: String,
    required: true,
  },
})
</script>

<template>
  <NuxtLink class="button button--outline" :to="url">{{ text }}</NuxtLink>
</template>