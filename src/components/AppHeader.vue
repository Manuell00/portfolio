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
    <div class="logo-section">
      <img src="../../public/Logo.png" alt="Manuel Caselli Logo" />
    </div>

    <div class="main-nav">
      <ul class="nav-links">
        <li><a href="#home">Home</a></li>
        <li><a href="#portfolio">Portfolio</a></li>
      </ul>

      <div class="social-links">
        <a href="https://www.linkedin.com/in/manuel-caselli-78a0a7244/"><i class="fab fa-linkedin"></i></a>
        <a href="https://github.com/Manuell00"><i class="fa-brands fa-github"></i></a>
      </div>
    </div>

    <button class="cta-button">CONTACT ME</button>
  </nav>
</template>




<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;

nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-direction: row;
  background-color: black !important;
  height: 10vh;
  width: 100%;
  box-sizing: border-box;
  padding: 0 2rem;
  z-index: 1000;
  text-transform: uppercase;
  position: fixed;
  font-family: sans-serif;
  top: 0;

  .logo-section {
    height: 100px;
    width: 100px;

    img {
      border-radius: 50%;
      height: 100%;
      width: 100%;
    }
  }

  .main-nav {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 100px;
  }

  .nav-links {
    display: flex;
    justify-content: space-around;
    align-items: center;
    list-style: none;
    padding: 0;
    width: 30%;


    li {
      margin: 0 1rem;

      a {
        text-decoration: none;
        color: white;
        font-weight: 500;
        transition: color 0.3s ease;
        font-size: 2.0rem;

        &:hover {
          color: $green;
        }
      }
    }
  }

  .social-links {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 30px;

    a {
      margin-left: 1rem;
      color: white;
      font-size: 4.5rem;
      transition: 0.7s all ease;

      &:hover {
        color: $green;
      }
    }
  }

  .cta-button {
    background-color: white;
    color: black;
    font-weight: 600;
    padding: 1rem 3rem;
    border: none;
    border-radius: 15px;
    transition: background-color 0.3s ease;
    font-size: 1.5rem;
    transition: 0.7s all ease;

    &:hover {
      background-color: darken(white, 20%);
      color: $green;
    }
  }
}


// ... il resto del tuo stile ...

@media (max-width: 992px) {
  nav {
    flex-direction: column;
    height: auto;
    padding: 1rem;

    .main-nav {
      width: 100%;
      gap: 0;
      justify-content: center;
    }

    .nav-links {
      display: none; // Nasconde i link di default su schermi più piccoli

      &.active {
        // Mostra i link quando il menu hamburger è attivo
        display: flex;
        flex-direction: column;
        position: absolute;
        top: 100%;
        left: 0;
        background-color: $green;
        width: 100%;
        gap: 0.5rem;
        padding: 1rem 0;

        li {
          margin: 0;

          a {
            font-size: 1.5rem;
          }
        }
      }
    }

    .social-links {
      display: none;
    }

    .cta-button {
      margin-top: 1rem;
      width: 100%;
    }
  }
}
</style>
