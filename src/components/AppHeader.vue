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
      dropDisplay: false,
    }
  },

  methods: {
    openOffcanvas() {
      this.offcanvasOpen = true;
    },
    closeOffcanvas() {
      this.offcanvasOpen = false;
    },
    toggleDrop() {
      if (this.dropDisplay) {
        this.dropDisplay = false
      }
      else {
        this.dropDisplay = true
      }

    },

    scrollTo(sectionId) {
      const element = document.getElementById(sectionId);

      if (element) {
        let top = element.offsetTop;

        // Sottrai una quantità desiderata dalla posizione di top
        top = top - 100;  // ad esempio, per ridurre di 50px

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
        <li> <a href="mailto:manuell.caselli@gmail.com">CONTACT ME</a></li>
        <li>
          <!-- Inserisco button per download  -->
          <a href="../../public/MANUEL_CASELLI-cv.pdf" download="Manuel-CV.pdf" class="cv-button"> Curriculum</a>
        </li>

        <!-- Dropdown social -->
        <li class="dropdown" @click="toggleDrop">
          Social
          <div :style="dropDisplay ? { display: 'block' } : {}" class="dropdown-content">
            <!-- Inserisci qui gli elementi del dropdown -->
            <a href="https://www.linkedin.com/in/manuel-caselli-78a0a7244/"><i class="fab fa-linkedin"></i></a>
            <a href="https://github.com/Manuell00"><i class="fa-brands fa-github"></i></a>
            <a href="https://www.instagram.com/manuel_caselli/"><i class="fa-brands fa-instagram"></i></a>
          </div>
        </li>
      </ul>

      <!-- Pulsante per chiudere l'offcanvas -->
      <div class="close-button" :style="{ 'padding-top': dropDisplay ? '180px' : '0' }">
        <button @click="closeOffcanvas">
          <i class="fa-solid fa-xmark"></i>
        </button>
      </div>
    </div>
  </div>
</template>




<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/header.scss';
@use '../styles/partials/_variables.scss' as *;
</style>
