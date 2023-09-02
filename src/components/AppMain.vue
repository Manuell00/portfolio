<script>
// Importo lo STORE
import { store } from '../store.js';

// Importo i COMPONENTi

// Inserisco l'EXPORT
export default {
    name: 'AppMain',
    components: {

    },

    // Inserisco i dati
    data() {
        return {
            store,
        }
    },

    // Dovrò inserire i metodi
}
</script>

<!-- TEMPLATE -->
<!-- In qusto caso essendo un componente molto grosso, lo renderò padre di altri piccoli sottocomponenti -->
<template>
    <div class="container-fluid">

        <!-- Home intro -->
        <div class="home-intro">

            <!-- Primo contenuto (scritto) -->
            <div class="content">

                <div class="content-movement">
                    <div>
                        <div id="sticker">🍝</div>
                        Hi Everyone! I'm Manuel
                    </div>
                </div>


                <div class="content-primary">
                    <h1>
                        A <span>Full-stack developer</span> and <span>management engineer</span>, blending tech expertise
                        with optimization skills.
                    </h1>
                </div>

                <div class="content-secondary">
                    <p>
                        Fresh out of Management Engineering, I took a 6-month deep dive into coding with Boolean. Data
                        analysis and web application development now capture my focus. Merging my newfound tech skills with
                        my engineering background, I'm eager to contribute and grow in the digital space.
                    </p>
                </div>
            </div>


            <!-- Secondo contenuto (Sticker) -->
            <div class="emoj">
                <div class="row flex-row">
                    <!-- First row of images (HTML, CSS, JavaScript) -->
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/html-5-svgrepo-com.svg" alt="HTML 5">
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/css-3-svgrepo-com.svg" alt="CSS 3">
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/javascript-svgrepo-com.svg" alt="JavaScript">
                    </div>

                    <!-- Second row of images (PHP, Sass, SQL) -->
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/php-svgrepo-com.svg" alt="PHP">
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/sass-svgrepo-com.svg" alt="Sass">
                    </div>
                    <div class="col-lg-4 col-md-4 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/sql-svgrepo-com.svg" alt="SQL">
                    </div>

                    <!-- Third row of images (Laravel, Vue, Vite, Python) -->
                    <div class="col-lg-3 col-md-3 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/laravel-svgrepo-com.svg" alt="Laravel">
                    </div>
                    <div class="col-lg-3 col-md-3 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/vue-svgrepo-com.svg" alt="Vue.js">
                    </div>
                    <div class="col-lg-3 col-md-3 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/vite-svgrepo-com.svg" alt="Vite">
                    </div>
                    <div class="col-lg-3 col-md-3 col-sm-6 col-12 text-center mb-4">
                        <img src="../../public/python-svgrepo-com.svg" alt="Python">
                    </div>
                </div>
            </div>

        </div>

    </div>
</template>

<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;


.container-fluid {
    margin: 0;
    max-width: 100%;
    overflow: hidden;
    width: 100%;
    height: 90vh;
    background-image: url(../../public/endless-constellation.svg);

    .home-intro {
        padding: 50px;
        height: auto;
        max-width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;


        // PRIMO CONTENUTO
        .content {
            animation: slideFromLeft 1s forwards;
            width: 50%;

            // First row of content
            .content-movement {
                margin-bottom: 1.5rem;
                width: max-content;
                padding-right: 5%;



                div {
                    padding: 0px 15px;
                    border-radius: 12px;
                    background-color: rgba(75, 0, 130, 0.6);
                    font-size: 2.0rem;
                    font-weight: 900;
                    letter-spacing: .05em;
                    margin: 0;
                    text-transform: capitalize;

                    #sticker {
                        animation: computerMovement 2s ease-in-out infinite;
                        font-size: 50px;
                        margin: 20px 0;
                        display: inline-block;
                        background-color: transparent;

                    }

                }

            }

            // Second row of content
            .content-primary {
                margin-bottom: 2rem;

                h1 {
                    text-transform: capitalize;
                    font-weight: 900;
                    letter-spacing: .02em;
                    margin: 0;

                    span {
                        color: #007BFF;
                        font-family: Cyborg;
                        font-size: 4.2rem;
                        text-shadow: 3px 3px 0 #1f2127, -1px -1px 0 #1f2127, 1px -1px 0 #1f2127, -1px 1px 0 #1f2127, 1px 1px 0 #1f2127;
                    }
                }
            }


            // Third row of content
            .content-secondary {
                margin-bottom: 2rem;

                p {
                    line-height: 1.5;
                    font-size: 1.5rem;
                    font-weight: 700;
                    letter-spacing: .04em;
                    margin: 0;
                    opacity: .8;
                    text-transform: lowercase;
                }
            }
        }

        // SECONDO CONTENUTO
        .emoj {
            animation: slideFromRight 1s forwards;
            width: 50%;
            padding: 0 10%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;

            .flex-row {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;

                img {
                    width: 100%;
                    height: 150px;
                    fill: #007BFF;
                }
            }
        }
    }
}

// Your existing styles...

// Media Queries for Responsiveness
@media (max-width: 1200px) {
    // For large devices like laptops

    .container-fluid .home-intro .content {
        width: 70%; // Increase width for more space
    }
}

@media (max-width: 1100px) {
    // For medium devices like tablets

    .container-fluid .home-intro {
        flex-direction: column; // Stack content and emoj sections on top of each other
    }

    .container-fluid .home-intro .content,
    .container-fluid .home-intro .emoj {
        width: 100%; // Utilize full width
        padding: 20px 0; // Add some vertical padding
    }
}

@media (max-width: 768px) {
    // For small devices like mobile phones

    .container-fluid .home-intro .content .content-movement div {
        font-size: 1.5rem; // Reduce font size
    }

    .container-fluid .home-intro .content .content-primary h1 {
        font-size: 1.8rem; // Reduce font size

        span {
            font-size: 2.5rem; // Reduce font size
        }
    }

    .container-fluid .home-intro .content .content-secondary p {
        font-size: 1.2rem; // Reduce font size
    }
}

@media (max-width: 576px) {
    // For very small devices like mobile phones

    .container-fluid .home-intro .content .content-movement div {
        font-size: 1.2rem; // Reduce font size more
    }

    .container-fluid .home-intro .content .content-primary h1 {
        font-size: 1.5rem; // Reduce font size more

        span {
            font-size: 2.2rem; // Reduce font size more
        }
    }

    .container-fluid .home-intro .content .content-secondary p {
        font-size: 1rem; // Reduce font size more
    }
}
</style>
