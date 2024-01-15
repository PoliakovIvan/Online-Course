<script setup>

const isOpen = ref(false);

const data = {
  "logoDark": "/images/svg/createX-logo-b.svg",
  "logoLight": "/images/svg/createX-logo-w.svg",
  "name": "CreateX",
  "navbar": [
    { "name": "About us", "slug": "about-us" },
    { "name": "Courses", "slug": "courses" },
    { "name": "Events", "slug": "events" },
    { "name": "Blog", "slug": "blog" },
    { "name": "Contacts", "slug": "contactss" }
  ]
}
</script>

<template>
  <header>
    <div class="header__desktop">
      <nav class="container">
        <NuxtLink to="/" class="header__logo">
          <!-- temp data -->
          <img class="header__logo--dark" :src="data.logoDark" :alt="data.name">
          <img class="header__logo--light" :src="data.logoLight" :alt="data.name">
        </NuxtLink>
        <ul class="header__menu">
          <li v-for="item in data.navbar" :key="JSON.stringify(item)">
            <NuxtLink :to="`/${item.slug}`"> {{ item.name }}</NuxtLink>
          </li>
        </ul>
        <div class="header__buttons">
          <primary-button url="#" text="Get consultation" />
          <outline-button url="#" text="Log in" />
        </div>
        <button class="header__burger" @click="isOpen = !isOpen" :aria-label="isOpen ? 'Close menu' : 'Open menu'">
          <svg v-if="!isOpen">
            <use xlink:href="/images/svg/sprites.svg#burger">
            </use>
          </svg>
          <svg v-else>
            <use xlink:href="/images/svg/sprites.svg#xmark"></use>
          </svg>
        </button>
      </nav>
    </div>
    <div :class="isOpen ? 'left-0' : 'left-full'" class="header__mobile mobile-header container">
      <nav>
        <ul class="mobile-header__menu">
          <li v-for="item in data.navbar" :key="JSON.stringify(item)">
            <NuxtLink :to="`/${item.slug}`"> {{ item.name }}</NuxtLink>
          </li>
        </ul>
        <div class="mobile-header__buttons">
          <primary-button url="#" text="Get consultation" />
          <outline-button url="#" text="Log in" />
        </div>
      </nav>
    </div>
  </header>
</template>