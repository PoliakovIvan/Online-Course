<script setup>
defineProps({
  itemData: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <div class="course">
    <div class="course__image">
      <img :src="itemData.image" :alt="itemData.name">
    </div>
    <div class="course__body">
      <card-category :categoryName="itemData.category" />
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