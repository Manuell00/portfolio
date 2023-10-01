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
  <nav>
    <div class="social-links">
      <span class="dropdown-toggle"><i class="fa-solid fa-share-from-square"></i></span>
      <div class="dropdown-menu">
        <a href="https://www.linkedin.com/in/manuel-caselli-78a0a7244/"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/Manuell00"><i class="fa-brands fa-github"></i></a>
        <a href="https://www.instagram.com/manuel_caselli/"><i class="fa-brands fa-instagram"></i></a>
      </div>
    </div>

    <div class="main-nav">
      <ul class="nav-links">
        <!-- Inserisco gli eventi al click -->
        <li><a href="#home" @click.prevent="scrollTo('home')">Home</a></li>
        <li><a href="#tech" @click.prevent="scrollTo('tech')">Tools</a></li>
        <li><a href="#portfolio" @click.prevent="scrollTo('portfolio')">Portfolio</a></li>
      </ul>

    </div>

    <a href="mailto:manuell.caselli@gmail.com"> <button class="cta-button">CONTACT ME</button></a>
  </nav>
</template>




<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/header.scss';
@use '../styles/partials/_variables.scss' as *;
</style>
