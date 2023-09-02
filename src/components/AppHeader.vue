<script>
// Importo lo STORE
import { store } from '../store.js';

// Inserisco l'EXPORT
export default {
  name: 'AppHeader',

  data() {
    return {
      store,
    }
  },

  methods: {

  }

}
</script>

<!-- TEMPLATE -->
<template>
  <nav>

  </nav>
</template>



<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;

nav {
  align-items: center;
  -webkit-animation: fadeInDown 1s ease forwards;
  animation: fadeInDown 1s ease forwards;
  background-color: #4B0082 !important;
  display: flex;
  height: 10vh;
  justify-content: space-between;
  max-width: 100%;
  padding: 0;
  position: -webkit-sticky;
  position: sticky;
  top: 0;
  z-index: 100;
}
</style>
