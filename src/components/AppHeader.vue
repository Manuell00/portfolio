<script>
// Importo lo STORE
import { store } from '../store.js';

// Inserisco l'EXPORT
export default {
  name: 'AppHeader',

  data() {
    return {
      store,
      offcanvasOpen: false,
    }
  },

  methods: {
    openOffcanvas() {
      this.offcanvasOpen = true;
    },
    closeOffcanvas() {
      this.offcanvasOpen = false;
    },
    scrollTo(sectionId) {
      const element = document.getElementById(sectionId);

      if (element) {
        let top = element.offsetTop;

        // Sottrai una quantità desiderata dalla posizione di top
        top = top - 200;  // ad esempio, per ridurre di 50px

        window.scrollTo({
          top: top,
          behavior: 'smooth'
        });
      }
    }


  }

}
</script>

<!-- TEMPLATE -->
<template>
  <!-- NAVBAR -->
  <nav>
    <button class="btn" @click="openOffcanvas">
      <i class="fa-solid fa-bars"></i>
    </button>
  </nav>

  <!-- OFFCANAS -->
  <div class="offcanvas" :class="{ 'active': offcanvasOpen }">

    <!-- Contenuto dell'offcanvas -->
    <div class="offcanvas-content">
      <!-- Contenuto del menu di navigazione -->
      <ul class="nav-links">
        <li><a href="#home" @click.prevent="scrollTo('home')">Home</a></li>
        <li><a href="#tech" @click.prevent="scrollTo('tech')">Tools</a></li>
        <li><a href="#portfolio" @click.prevent="scrollTo('portfolio')">Portfolio</a></li>
        <li> <a href="mailto:manuell.caselli@gmail.com"><button class="cta-button">CONTACT ME</button></a></li>
      </ul>
    </div>

    <!-- Pulsante per chiudere l'offcanvas -->
    <button class="close-button" @click="closeOffcanvas">Chiudi</button>
  </div>
</template>




<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/header.scss';
@use '../styles/partials/_variables.scss' as *;
</style>
