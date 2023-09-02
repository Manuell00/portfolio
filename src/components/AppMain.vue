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

                <!-- Prima svg -->
                <svg class="mini-img" width="800px" height="800px" viewBox="0 0 24 24" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path d="M9 6L3.40208 11.1314C3.1859 11.3296 3.1859 11.6704 3.40208 11.8686L9 17" stroke="#000000"
                        stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
                    <path d="M14 17L19.5979 11.8686C19.8141 11.6704 19.8141 11.3296 19.5979 11.1314L14 6" stroke="#000000"
                        stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" />
                </svg>

                <!-- Immagine -->
                <img src="../../computers.svg" alt="">

                <!-- Seconda svg -->
                <svg class="mini-img" width="800px" height="800px" viewBox="0 0 24 24" fill="none"
                    xmlns="http://www.w3.org/2000/svg">
                    <path
                        d="M7.90451 6.92144C8.41341 6.45495 8.44779 5.66424 7.9813 5.15534C7.51481 4.64645 6.7241 4.61207 6.2152 5.07856L7.90451 6.92144ZM1.46194 11.1314L2.3066 12.0529L2.3066 12.0529L1.46194 11.1314ZM1.46194 11.8686L2.3066 10.9471L2.3066 10.9471L1.46194 11.8686ZM6.2152 17.9214C6.7241 18.3879 7.51481 18.3536 7.9813 17.8447C8.44779 17.3358 8.41341 16.545 7.90451 16.0786L6.2152 17.9214ZM6.2152 5.07856L0.617287 10.21L2.3066 12.0529L7.90451 6.92144L6.2152 5.07856ZM0.617287 12.79L6.2152 17.9214L7.90451 16.0786L2.3066 10.9471L0.617287 12.79ZM0.617287 10.21C-0.139356 10.9036 -0.139356 12.0964 0.617287 12.79L2.3066 10.9471C2.63087 11.2444 2.63087 11.7556 2.3066 12.0529L0.617287 10.21Z"
                        fill="#000000" />
                    <path
                        d="M16.0557 16.0786C15.5468 16.545 15.5125 17.3358 15.9789 17.8447C16.4454 18.3536 17.2361 18.3879 17.745 17.9214L16.0557 16.0786ZM22.4983 11.8686L21.6537 10.9471L21.6537 10.9471L22.4983 11.8686ZM22.4983 11.1314L21.6537 12.0529L21.6537 12.0529L22.4983 11.1314ZM17.745 5.07856C17.2361 4.61207 16.4454 4.64645 15.979 5.15534C15.5125 5.66424 15.5468 6.45495 16.0557 6.92144L17.745 5.07856ZM17.745 17.9214L23.343 12.79L21.6537 10.9471L16.0557 16.0786L17.745 17.9214ZM23.343 10.21L17.745 5.07856L16.0557 6.92144L21.6537 12.0529L23.343 10.21ZM23.343 12.79C24.0996 12.0964 24.0996 10.9036 23.343 10.21L21.6537 12.0529C21.3294 11.7556 21.3294 11.2444 21.6537 10.9471L23.343 12.79Z"
                        fill="#000000" />
                    <path
                        d="M15.2127 3.80317C15.3801 3.13343 14.9729 2.45476 14.3032 2.28732C13.6334 2.11989 12.9548 2.52709 12.7873 3.19683L15.2127 3.80317ZM8.78732 19.1968C8.61989 19.8666 9.02709 20.5452 9.69683 20.7127C10.3666 20.8801 11.0452 20.4729 11.2127 19.8032L8.78732 19.1968ZM12.7873 3.19683L8.78732 19.1968L11.2127 19.8032L15.2127 3.80317L12.7873 3.19683Z"
                        fill="#000000" />
                </svg>
            </div>

        </div>


        <!-- TOOLING -->
        <div class="tooling">
            <div class="tooling-title">
                <h2>Tooling</h2>
            </div>

            <div class="tooling-box">
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

        <!-- MY WORKS -->
        <div class="work">
            <div class="work-header">


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
    width: 100%;
    min-height: 90vh;
    max-height: 100%;
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
            flex-direction: row;

            .mini-img {
                max-width: 200px; // Questo garantisce che le immagini non siano più grandi del loro contenitore
                height: auto;
            }

            img {
                max-width: 500px; // Questo garantisce che le immagini non siano più grandi del loro contenitore
                height: auto;
            }
        }
    }

    // Tooling
    .tooling {
        align-items: center;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 5rem 0;
        background: linear-gradient(to bottom, black, $violet );
        background-size: 200% 200%;

        .tooling-title {
            align-items: center;
            background: #12141d;
            border-radius: 12px;
            box-shadow: inset 0 0 4px 1px $violet;
            -webkit-box-shadow: inset 0 0 4px 1px $violet;
            -moz-box-shadow: inset 0 0 4px 1px $violet;
            display: flex;
            justify-content: center;
            margin-bottom: 5rem;
            padding: 0 3rem;
            transition: 0.7s ease-in;

            &:hover {
                transform: scale(1.2);
            }

            h2 {
                font-size: 3.5rem;
                color: $violet;
                font-family: 'CYBORG', sans-serif;
                font-weight: 900;
                text-shadow: 3px 3px 0 #000, -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
                text-transform: uppercase;
            }
        }

        .tooling-box {
            align-items: center;
            background-image: url(../../public/endless-constellation.svg);
            border-radius: 15px;
            border: 5px solid black;
            display: flex;
            flex-wrap: wrap;
            justify-content: center;
            padding: 1.5rem;
            width: 50%;

            .flex-row {
                display: flex;
                flex-wrap: wrap;
                justify-content: center;
                row-gap: 20px;

                img {
                    width: 100%;
                    height: 150px;
                    transition: all 0.4s ease-in;

                    &:hover {
                        transform: scale(1.1);
                    }
                }
            }
        }
    }

    // WORKS
    .work .work-header {
        align-items: flex-start;
        display: flex;
        justify-content: flex-start;
        padding-left: 5rem;
    }
}


// MEDIA QUERY

@media (max-width: 1700px) {
    .container-fluid .emoj {
        .mini-img {
            width: 120px;
        }

        img {
            width: 350px; // Slightly reduce the image width for large devices
        }
    }
}

@media (max-width: 1200px) {
    .container-fluid .home-intro {
        .content {
            width: 70%; // Increase width for more space
        }

        .emoj {
            .mini-img {
                width: 100px;
            }

            img {
                width: 300px; // Slightly reduce the image width for large devices
            }

            svg.mini-img {
                // Nascondi SVG con classe .mini-img a partire da 1300px
                display: none;
            }
        }
    }
}

@media (max-width: 1200px) {
    .container-fluid .home-intro {
        flex-direction: column; // Stack content and emoj sections on top of each other

        .content {
            display: flex;
            justify-content: center;
            text-align: center;
            flex-direction: column;

            .content-movement {
                text-align: center;
                padding: 0;
                width: 100%;
            }

            .emoj {
                width: 100%; // Utilize full width
                padding: 20px 0; // Add some vertical padding

                svg.mini-img {
                    display: none;
                }

                img {
                    width: 250px; // Reduce the image width for tablets
                }
            }
        }
    }
}

@media (max-width: 768px) {
    .container-fluid .home-intro {
        .content {
            .content-movement {
                .sticker {
                    display: block;
                }

                div {
                    font-size: 1.5rem; // Reduce font size
                }
            }

            .content-primary h1 {
                font-size: 1.8rem; // Reduce font size

                span {
                    font-size: 2.5rem; // Reduce font size
                }
            }

            .content-secondary p {
                font-size: 1.2rem; // Reduce font size
            }
        }

        .emoj {


            img {
                width: 200px; // Further reduce the image width for mobile phones
            }
        }
    }
}

@media (max-width: 576px) {
    .container-fluid .home-intro {
        .content {
            .content-movement div {
                font-size: 1.2rem; // Reduce font size more
            }

            .content-primary h1 {
                font-size: 1.5rem; // Reduce font size more

                span {
                    font-size: 2.2rem; // Reduce font size more
                }
            }

            .content-secondary p {
                font-size: 1rem; // Reduce font size more
            }
        }

        .emoj img {
            width: 250px; // Reduce the image width even more for very small devices
        }
    }
}
</style>

