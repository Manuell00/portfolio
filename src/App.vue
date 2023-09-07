<script>

// Importo lo STORE
import { store } from './store.js';
// Importo AXIOS 
import axios from 'axios';

// Importo i COMPONENTI
import AppHeader from './components/AppHeader.vue'
import AppMain from './components/AppMain.vue'
import AppFooter from './components/AppFooter.vue'
import CookieApp from './components/CookieApp.vue'


// Inserisco l'EXPORT
export default {
  components: {
    AppHeader,
    AppMain,
    AppFooter,
    CookieApp,
  },

  // Inserisco i dati
  data() {
    return {
      store,
    }
  },

  // Dovrò inserire i metodi
  methods: {

  },

  // CREATED viene utilizzato al posto di mounted perchè svolge l'attività quando viene creata l'app
  created() {
  }

}


</script>



<!-- TEMPLATE -->
<template>
  <!-- Inserisco l'header e il suo componente -->
  <header>
    <AppHeader />
  </header>

  <!-- Inserisco il main e il suo componente -->
  <main>
    <AppMain />
  </main>

  <!-- Inserisco il footer e il suo componente -->
  <footer>
    <AppFooter />
    <!-- <CookieApp /> -->
  </footer>
</template>



<!-- Inserisco lo style -->
<style lang="scss">
@use './styles/general.scss' as *;
@use './styles/partials/variables.scss' as *;
</style>
