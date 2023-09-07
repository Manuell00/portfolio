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

  .social-links {
    margin: 0 1rem;
    position: relative;

    .dropdown-toggle {
      text-decoration: none;
      color: white;
      font-weight: 500;
      font-size: 2.0rem;
      cursor: pointer;
      transition: background-color 0.3s ease, transform 0.5s ease;

      &:hover {
        transform: translateY(-10px);
        padding: 10px 0;
        color: $green;
      }

    }

    .dropdown-menu {
      display: none;
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translate(-50%, 0%);
      background-color: black;
      border-radius: 5px;
      overflow: hidden;
      z-index: 1;

      a {
        display: block;
        padding: 10px 20px;
        color: white;
        transition: background-color 0.3s;

        &:hover {
          background-color: lighten($footer-background-color, 10%);
          color: $green;
        }
      }
    }

    &:hover {
      .dropdown-menu {
        display: block;
      }
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


// MEDIA QUERY

@media (max-width: 1500px) {
  nav {
    padding: 0 1rem;

    .nav-links {
      width: 40%;

      li {
        margin: 0 0.5rem;

        a {
          font-size: 1.8rem;
        }
      }
    }

    .social-links {
      gap: 20px;

      a {
        font-size: 4rem;
      }
    }

    .cta-button {
      font-size: 1.4rem;
      padding: 0.8rem 2.5rem;
    }
  }
}

@media (max-width: 992px) {
  nav {
    flex-direction: column;
    height: auto;
    padding: 0.8rem;

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
        padding: 0.8rem 0;

        li {
          margin: 0;

          a {
            font-size: 1.4rem;
          }
        }
      }
    }

    .social-links {
      display: none;
    }

    .cta-button {
      margin-top: 0.8rem;
      width: 100%;
      font-size: 1.2rem;
      padding: 0.7rem 2.2rem;
    }
  }
}

@media (max-width: 768px) {
  nav {

    .cta-button {
      font-size: 1.1rem;
      padding: 0.6rem 2rem;
    }

    .nav-links.active {
      a {
        font-size: 1.2rem;
      }
    }
  }
}


@media (max-width: 400px) {
  nav {
    padding: 1rem 0;

    .cta-button {
      font-size: 0.8rem;
      padding: 0.6rem 2rem;
    }

    .nav-links.active {
      a {
        font-size: 0.9rem;
      }
    }
  }
}
</style>
