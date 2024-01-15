export default defineNuxtConfig({
  devtools: { enabled: true },
  ssr: true,
  css: [
    '~/assets/scss/main.scss'
  ],
  components: [
    {
      path: '~/components',
      pathPrefix: false
    }
  ]
})
