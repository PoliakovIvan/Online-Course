<script setup>
</script>

<template>
  <section class="section">
    <div class="section__top">
      <slot name="heading" />
    </div>
    <div class="section__bottom">
      <slot name="content" />
    </div>
  </section>
</template>