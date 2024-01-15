<script setup>
defineProps({
  itemData: {
    type: Object,
    required: true
  }
})

/* получение категорий с базы данных*/
const categoriesColors = {
  "marketing": '#03cea4',
  "management": '#5a87fc',
  "hr": '#f89828',
};

const getCategoryColor = (category) => {
  return categoriesColors[category.toLowerCase()] || '#ff69b4';
};
</script>

<template>
  <div class="course">
    <div class="course__image">
      <img :src="itemData.image" :alt="itemData.name">
    </div>
    <div class="course__body">
      <NuxtLink :style="{ backgroundColor: getCategoryColor(itemData.category) }" to="#" class="course__category">{{
        itemData.category }}</NuxtLink>
      <NuxtLink to="#" class="course__name">
        <h3>{{ itemData.name }}</h3>
      </NuxtLink>
      <div class="course__info">
        <span class="course__price">${{ itemData.price }}</span>
        <span class="course__mentor">by {{ itemData.mentor }}</span>
      </div>
    </div>
  </div>
</template>