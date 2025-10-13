import tailwindcss from '@tailwindcss/vite';

export default defineNuxtConfig({
  compatibilityDate: '2025-07-15',
  devtools: { enabled: true },

  ssr: true,

  vite: {
    plugins: [tailwindcss()]
  },

  modules: ['@nuxt/ui', '@nuxt/image']
});