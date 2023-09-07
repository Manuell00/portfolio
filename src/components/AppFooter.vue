<script>
// Importo lo STORE
import { store } from '../store.js';

export default {
    name: 'AppFooter',

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
    <footer class="app-footer">
        <div class="content">

            <!-- Inserisco la navbar -->
            <nav>
                <!-- Indirizzi -->
                <ul class="direct">
                    <li><a href="#home" @click.prevent="scrollTo('home')">Home</a></li>
                    <li><a href="#portfolio" @click.prevent="scrollTo('portfolio')">Portfolio</a></li>
                    <li><a href="../../public/manuel-cv.pdf" download="Manuel-CV.pdf" class="cv-button">Curriculum</a></li>
                    <li><a href="mailto:manuell.caselli@gmail.com">Contact me</a></li>
                </ul>

                <!-- Social -->
                <ul class="social-links">
                    <a href="https://www.linkedin.com/in/manuel-caselli-78a0a7244/"><i class="fab fa-linkedin"></i></a>
                    <a href="https://github.com/Manuell00"><i class="fa-brands fa-github"></i></a>
                    <a href="https://www.instagram.com/manuel_caselli/"><i class="fa-brands fa-instagram"></i></a>
                </ul>

                <!-- Mappa -->
                <div class="map">
                    <iframe
                        src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d141915.11095709525!2d8.751099207959587!3d44.43390326053964!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x12d34152dcd49aad%3A0x236a84f11881620a!2sGenova%20GE!5e0!3m2!1sit!2sit!4v1693921341880!5m2!1sit!2sit"
                        width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy"
                        referrerpolicy="no-referrer-when-downgrade"></iframe>
                </div>
            </nav>

            <p>&copy; 2023 Manuel Caselli | All Rights Reserved</p>
        </div>
    </footer>
</template>

<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;

.app-footer {
    border-right: 1px solid rgba(0, 0, 0, 0.1);
    background-color: $footer-background-color;
    font-family: 'Roboto', sans-serif;
    color: black;
    padding: 20px;
    box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1); // aggiunge ombra in alto
    transition: all 0.3s; // transizione fluida


    .content {
        display: flex;
        justify-content: center;
        flex-direction: column;
        align-items: center;
        width: 100%;

        nav {
            display: flex;
            justify-content: space-between;
            flex-direction: row;
            align-items: center;
            width: 100%;
            padding: 0 100px;

            .direct {
                display: flex;
                flex-direction: column;
                gap: 1rem;
                list-style-type: none;
                font-size: 60px;
                text-transform: uppercase;

                li {
                    cursor: pointer;
                    text-decoration: none;
                    padding: 10px 15px; // Aumenta un po' il padding
                    background-color: rgba($green, 0.1); // Usa il verde come sfondo con un'opacità ridotta
                    border-radius: 10px; // Angoli più arrotondati
                    transition: background-color 0.3s, transform 0.3s;

                    &:hover {
                        background-color: rgba($green, 0.3); // Cambia l'opacità al passaggio del mouse
                        transform: scale(1.03); // Effetto di ingrandimento leggero all'hover
                    }

                    a {
                        text-decoration: none;
                        color: black;
                        transition: color 0.3s;

                        &:hover {
                            color: $green; // Cambia colore al passaggio del mouse
                        }
                    }
                }
            }

            .social-links {
                display: flex;
                flex-direction: column;
                gap: 2rem;
                list-style-type: none;
                font-size: 100px;

                a {
                    transition: all 0.3s; // transizione fluida
                    color: black;

                    &:hover {
                        transform: scale(1.2); // effetto di zoom al passaggio del mouse
                        color: $green; // cambio colore all'hover
                    }
                }
            }

            .map {
                position: relative;
                padding: 20px;
                border-radius: 15px;
                background-color: rgba(255, 255, 255, 0.1); // Sfondo leggermente trasparente per un aspetto di "glass"
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.3);
                transition: transform 0.3s;

                // Queste pseudo-classi creano gli "schiacciamenti" che danno l'effetto 3D.
                &:before,
                &:after,
                &:nth-child(1),
                &:nth-child(2) {
                    content: '';
                    position: absolute;
                    background: rgba(0, 0, 0, 0.3); // Strato grigio scuro per dare l'effetto 3D
                    transition: all 0.3s;
                }

                // Top and Bottom
                &:before,
                &:after {
                    width: 100%;
                    height: 5px;
                    left: 0;
                }

                &:before {
                    top: -5px;
                    transform: skewX(-45deg);
                }

                &:after {
                    bottom: -5px;
                    transform: skewX(45deg);
                }

                // Left and Right
                &:nth-child(1),
                &:nth-child(2) {
                    height: 100%;
                    width: 5px;
                    top: 0;
                }

                &:nth-child(1) {
                    left: -5px;
                    transform: skewY(-45deg);
                }

                &:nth-child(2) {
                    right: -5px;
                    transform: skewY(45deg);
                }

                &:hover {
                    transform: translateY(-10px); // Effetto di "sollevamento" al passaggio del mouse
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);

                    &:before {
                        top: -10px;
                    }

                    &:after {
                        bottom: -10px;
                    }

                    &:nth-child(1) {
                        left: -10px;
                    }

                    &:nth-child(2) {
                        right: -10px;
                    }
                }

                iframe {
                    max-width: 400px;
                    height: 400px;
                    border: none;
                    border-radius: 5px;
                    filter: grayscale(50%);

                    &:hover {
                        filter: grayscale(0%);
                    }
                }
            }



        }
    }


    @media (max-width: 2500px) {

        // Adattamenti per schermi fino a 2500px
        .content {
            nav {
                padding: 0 50px; // Riduci lo spazio attorno alla nav
            }
        }
    }

    @media (max-width: 1700px) {

        // Adattamenti per schermi fino a 1700px
        .content {
            nav {
                .direct {
                    font-size: 50px; // Riduci la dimensione del font
                }
            }
        }
    }

    @media (max-width: 1500px) {

        // Adattamenti per schermi fino a 1500px
        .content {
            nav {
                .direct {
                    font-size: 45px; // Ulteriore riduzione del font
                }

                .social-links {
                    font-size: 80px; // Riduci la dimensione delle icone social
                }

                .map {
                    iframe {
                        width: 300px;
                        height: 300px;
                    }
                }
            }
        }
    }

    @media (max-width: 1200px) {

        // Adattamenti per schermi fino a 1200px
        .content {
            nav {
                flex-direction: row;

                .direct {
                    font-size: 40px; // Ancora più piccolo
                }

                .social-links {
                    flex-direction: row;
                    font-size: 70px; // Riduci ulteriormente le icone social
                    margin: 1rem;

                }

                .map {
                    display: none; // Nascondi la mappa
                }
            }
        }
    }

    @media (max-width: 768px) and (min-width: 577px) {

        // Adattamenti specifici per schermi tra 577px e 768px
        .content {
            nav {
                flex-direction: row; // Imposta il layout in colonna

                .direct,
                .social-links {
                    flex-direction: column; // Orizzontale
                    justify-content: center; // Centrato
                }

                .direct {
                    font-size: 35px; // Riduci il font
                    gap: 15px;

                    li {
                        padding: 5px 15px;
                    }
                }

                .social-links {
                    font-size: 60px; // Riduci le icone social
                    gap: 15px;
                    margin: 0;
                }

            }
        }
    }

    @media (max-width: 576px) {

        // Adattamenti per schermi fino a 576px
        .content {
            nav {
                flex-direction: column; // Mantieni la colonna

                .direct {
                    font-size: 15px; // Font ancora più piccolo
                    gap: 10px;
                    flex: column;

                    li {
                        padding: 5px 10px;
                    }
                }

                .social-links {
                    font-size: 50px; // Isole social più piccole
                    gap: 10px;
                }
            }

            p {
                text-align: center;
            }
        }
    }
}
</style>
