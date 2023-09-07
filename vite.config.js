import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

export default defineConfig({
  plugins: [vue()],

  // aggiunta della configurazione di risoluzione
  resolve: {
    alias: {
      'vue-cookies': 'vue-cookies/dist/vue-cookies.esm.js',
    }
  }
});
