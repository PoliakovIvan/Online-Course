<script setup>
defineProps({
  categoryName: {
    type: String,
    required: true
  }
})

/* получение категорий с базы данных*/
const categories = {
  "marketing": {
    color: '#03cea4',
    url: '/marketing'
  },
  "management": {
    color: '#5a87fc',
    url: '/management'
  },
  "hr": {
    color: '#f89828',
    url: '/hr'
  },
  "design": {
    color: '#f52f6e',
    url: '/design'
  },
  "development": {
    color: '#7772f1',
    url: '/development'
  }
};
</script>

<template>
  <NuxtLink :style="{ backgroundColor: categories[categoryName.toLowerCase()].color || '#ff69b4' }"
    :to="categories[categoryName.toLowerCase()].url" class="category">
    {{
      categoryName }}</NuxtLink>
</template>