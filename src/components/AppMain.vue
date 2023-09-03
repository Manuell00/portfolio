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
                <span>
                    <svg width="16" height="40" viewBox="0 0 8 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M6.99999 18C6.46955 18 5.96085 17.7893 5.58577 17.4142C5.2107 17.0391 4.99999 16.5304 4.99999 16V13.61C5.00042 12.9513 4.83816 12.3027 4.52764 11.7218C4.21712 11.1408 3.76793 10.6456 3.21999 10.28L2.79999 10L3.21999 9.72C3.76793 9.35442 4.21712 8.85917 4.52764 8.27825C4.83816 7.69733 5.00042 7.04871 4.99999 6.39V4C4.99999 3.46957 5.2107 2.96086 5.58577 2.58579C5.96085 2.21071 6.46955 2 6.99999 2C7.2652 2 7.51956 1.89464 7.70709 1.70711C7.89463 1.51957 7.99999 1.26522 7.99999 1C7.99999 0.734784 7.89463 0.48043 7.70709 0.292893C7.51956 0.105357 7.2652 0 6.99999 0C5.93912 0 4.92171 0.421427 4.17156 1.17157C3.42142 1.92172 2.99999 2.93913 2.99999 4V6.39C3.00103 6.7202 2.92029 7.04552 2.765 7.33692C2.6097 7.62832 2.38467 7.87674 2.10999 8.06L0.449988 9.17C0.313865 9.26148 0.202329 9.38503 0.125209 9.52977C0.0480885 9.67451 0.00775146 9.836 0.00775146 10C0.00775146 10.164 0.0480885 10.3255 0.125209 10.4702C0.202329 10.615 0.313865 10.7385 0.449988 10.83L2.10999 11.94C2.38467 12.1233 2.6097 12.3717 2.765 12.6631C2.92029 12.9545 3.00103 13.2798 2.99999 13.61V16C2.99999 17.0609 3.42142 18.0783 4.17156 18.8284C4.92171 19.5786 5.93912 20 6.99999 20C7.2652 20 7.51956 19.8946 7.70709 19.7071C7.89463 19.5196 7.99999 19.2652 7.99999 19C7.99999 18.7348 7.89463 18.4804 7.70709 18.2929C7.51956 18.1054 7.2652 18 6.99999 18Z"
                            fill="#14E956"></path>
                    </svg>
                    <h2>My Works</h2>

                    <svg width="16" height="40" viewBox="0 0 8 20" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path
                            d="M7.55 9.17L5.89 8.06C5.61532 7.87674 5.39029 7.62832 5.23499 7.33692C5.07969 7.04552 4.99896 6.7202 5 6.39V4C5 2.93913 4.57857 1.92172 3.82843 1.17157C3.07828 0.421427 2.06087 0 1 0C0.734784 0 0.480429 0.105357 0.292892 0.292893C0.105356 0.48043 0 0.734784 0 1C0 1.26522 0.105356 1.51957 0.292892 1.70711C0.480429 1.89464 0.734784 2 1 2C1.53043 2 2.03914 2.21071 2.41421 2.58579C2.78929 2.96086 3 3.46957 3 4V6.39C2.99957 7.04871 3.16183 7.69733 3.47235 8.27825C3.78287 8.85917 4.23205 9.35442 4.78 9.72L5.2 10L4.78 10.28C4.23205 10.6456 3.78287 11.1408 3.47235 11.7218C3.16183 12.3027 2.99957 12.9513 3 13.61V16C3 16.5304 2.78929 17.0391 2.41421 17.4142C2.03914 17.7893 1.53043 18 1 18C0.734784 18 0.480429 18.1054 0.292892 18.2929C0.105356 18.4804 0 18.7348 0 19C0 19.2652 0.105356 19.5196 0.292892 19.7071C0.480429 19.8946 0.734784 20 1 20C2.06087 20 3.07828 19.5786 3.82843 18.8284C4.57857 18.0783 5 17.0609 5 16V13.61C4.99896 13.2798 5.07969 12.9545 5.23499 12.6631C5.39029 12.3717 5.61532 12.1233 5.89 11.94L7.55 10.83C7.68612 10.7385 7.79766 10.615 7.87478 10.4702C7.9519 10.3255 7.99224 10.164 7.99224 10C7.99224 9.836 7.9519 9.67451 7.87478 9.52977C7.79766 9.38503 7.68612 9.26148 7.55 9.17Z"
                            fill="#14E956"></path>
                    </svg>

                </span>
            </div>

            <!-- PROJECTS -->
            <div class="projects">

                <!-- 1 Project -->
                <div class="single">
                    <div class="single-img">
                        <img src="../../public/Screenshot 2023-08-29 alle 14.45.19.png" alt="">
                    </div>

                    <div class="single-details">
                        <h4>Spotify Web</h4>

                        <p>This project is a <span class="highlight">meticulous recreation</span> of Spotify's main web
                            application page. Crafted as one of my <span class="highlight">initial endeavors</span> into web
                            design, it showcases my foundational skills in <span class="highlight">frontend
                                development</span>.</p>


                        <ul class="tech-used">
                            <li>HTML5</li>
                            <li>CSS3</li>
                        </ul>

                        <div class="last">
                            <p class="project-date"> <span>Completed :</span> April 2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/html-css-spotifyweb">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Github Repo
                                </a>
                            </button>
                        </div>
                    </div>
                </div>



                <!-- 2 Project -->
                <div class="single">

                    <div class="single-details">
                        <h4>Whatsapp</h4>

                        <p> Delving deeper into the realm of advanced web development, I undertook the challenge of
                            emulating one of the world's most used messaging platforms: <span
                                class="highlight">WhatsApp</span>. This project involved creating an intricate frontend that
                            captures the authentic feel of WhatsApp's user interface. Yet, its true complexity lies beneath
                            the surface. Harnessing the power of various <span class="highlight">APIs</span>, I successfully
                            built real-time chat functionalities, allowing for dynamic interactions reminiscent of the
                            actual app. This venture not only pushed my frontend skills but also gave me profound insights
                            into backend development and the seamless integration of third-party services.</p>


                        <ul class="tech-used">
                            <li>HTML5</li>
                            <li>CSS3</li>
                            <li>VUE</li>
                        </ul>

                        <div class="last">
                            <p class="project-date"> <span>Completed :</span> May 2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/vue-boolzapp">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Github Repo
                                </a>
                            </button>
                        </div>
                    </div>

                    <div class="single-img">
                        <img class="img-2" src="../../public/Screenshot 2023-08-29 alle 14.47.30.png" alt="">
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
    padding-top: 10vh;
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
    .work {
        width: 100%;
        height: auto;
        background-color: black;
        padding-top: 15rem;

        .work-header {
            align-items: flex-start;
            display: flex;
            justify-content: flex-start;
            padding-left: 5rem;
            font-size: 1.6rem;

            span {
                display: flex;

                h2 {
                    font-family: Cyborg;
                    font-weight: 900;
                    margin: 0 .5rem;
                    padding: 0;
                }
            }

        }

        .projects {
            align-items: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
            margin: 3rem 0 7rem;
            padding: 0 5rem;

            .single {
                align-items: center;
                display: flex;
                justify-content: space-between;
                margin: 6rem 0;
                width: 100%;

                .single-img {
                    align-items: center;
                    display: flex;
                    justify-content: center;
                    width: 60%;

                    img {
                        border-radius: 15px;
                        box-shadow: 0 60px 123px -25px hsla(225, 2%, 62%, .42), 0 35px 75px -35px hsla(225, 2%, 62%, .08);
                        -webkit-filter: blur(0);
                        filter: blur(0);
                        height: 398px;
                        opacity: 1;
                        -webkit-transform: perspective(800px) rotateY(25deg) scale(.8) rotateX(10deg);
                        transform: perspective(800px) rotateY(25deg) scale(.8) rotateX(10deg);
                        transition: all .6s ease;
                        width: 700px;


                        &:hover {
                            box-shadow: 0 19px 67px -38px hsla(225, 2%, 62%, .8);
                            -webkit-filter: blur(.2px);
                            filter: blur(.2px);
                            opacity: 1;
                            -webkit-transform: perspective(800px) rotateY(-15deg) translateY(-50px) rotateX(10deg) scale(1);
                            transform: perspective(800px) rotateY(-15deg) translateY(-50px) rotateX(10deg) scale(1);
                        }
                    }

                    .img-2 {
                        transform: perspective(800px) rotateY(-25deg) scale(.8) rotateX(10deg);

                        &:hover {
                            -webkit-transform: perspective(800px) rotateY(15deg) translateY(50px) rotateX(10deg) scale(1);
                            transform: perspective(800px) rotateY(15deg) translateY(50px) rotateX(10deg) scale(1);
                        }
                    }
                }
            }

            .single-details {
                align-items: center;
                color: #fff;
                display: flex;
                flex-direction: column;
                justify-content: center;
                padding: 1rem;
                width: 40%;

                h4 {
                    border: 3px solid $violet;
                    box-shadow: 6px 6px 0 0 $violet;
                    color: $violet;
                    font-family: Cyborg;
                    font-weight: 700;
                    font-weight: 900;
                    margin-bottom: 3rem;
                    padding: .7rem 1.1rem;
                    text-transform: uppercase;
                    transition: transform 0.7s ease-in-out;

                    &:hover {
                        transform: scale(1.2);
                    }
                }

                .highlight {
                    color: #2C3E50;
                    background-color: #EAECEE;
                    padding: 2px 5px;
                    border-radius: 5px;
                    font-weight: bold;
                }


                .tech-used {
                    margin-top: 1.5rem;
                    border: 2px solid $violet;
                    border-radius: 15px;
                    background-color: rgba($violet, 0.1);
                    text-align: center;
                    padding: 1rem;
                    display: flex;
                    flex-wrap: wrap;
                    align-items: center;
                    justify-content: center;
                    gap: 1rem;

                    li {
                        list-style-type: none;
                        background-color: #fff;
                        color: $violet;
                        padding: 0.5rem 1rem;
                        border-radius: 7px;
                        font-weight: 600;
                        transition: background-color 0.3s ease;

                        &:hover {
                            background-color: $violet;
                            color: #fff;
                        }
                    }
                }

                .last {
                    display: flex;
                    align-items: center;
                    justify-content: space-between;
                    gap: 3rem;
                    max-width: 100%;

                    .project-date {
                        margin: 1.5rem;
                        font-size: 1.7rem;
                        font-weight: 600;
                        transition: transform 0.5s ease;

                        &:hover {
                            transform: scale(1.2);
                        }

                        span {
                            display: inline-block;
                            padding: 0.2rem 0.5rem;
                            color: $violet;
                            text-transform: capitalize;
                            transition: color 0.3s ease;

                            &:hover {
                                color: lighten($violet, 15%);
                            }
                        }
                    }

                    button {
                        background-color: $violet; // supponendo che tu voglia mantenere il tema viola, ma puoi sostituirlo con qualsiasi colore
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        font-size: 16px;
                        cursor: pointer;
                        transition: background-color 0.3s ease, transform 0.3s ease;
                        display: inline-flex; // per allineare correttamente l'icona e il testo
                        align-items: center;

                        i {
                            margin-right: 8px; // spazio tra l'icona e il testo
                        }

                        &:hover {
                            background-color: darken($violet, 15%); // scurisce il colore del pulsante quando si passa sopra con il mouse
                            transform: translateY(-2px); // dà un effetto di "sollevamento" al pulsante
                        }

                        &:active {
                            transform: translateY(0); // re-imposta la posizione del pulsante quando viene cliccato
                        }

                        a {
                            text-decoration: none;
                            color: inherit; // prende il colore dal genitore, in questo caso `button`
                            display: flex; // per allineare correttamente l'icona e il testo
                            align-items: center;
                        }
                    }
                }

            }
        }
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
    .container-fluid {
        padding-top: 15vh;

        .home-intro {
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

