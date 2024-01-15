<script setup>
defineProps({
  heading: {
    type: String,
    required: true,
  },
  subtitle: {
    type: String,
  }
})
</script>

<template>
  <section class="section">
    <div class="section__top">
      <div>
        <p class="section__subtitle"> {{ subtitle }}</p>
        <h2 class="section__heading">{{ heading }}</h2>
      </div>
      <outline-button url="#" />
    </div>
    <div class="section__bottom">
      <slot />
    </div>
  </section>
</template>