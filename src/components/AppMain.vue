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
        <div class="home-intro" id="home">

            <!-- Primo contenuto (scritto) -->
            <div class="content">

                <div class="content-movement">
                    <div>
                        <div id="sticker">🍝</div>
                        <span>Hi Everyone! I'm Manuel</span>
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
                        Fresh out of Management Engineering, I took a 6-month deep dive into coding with Boolean. <span>Data
                            analysis</span> and <span>web application development</span> now capture my focus.</p>
                    <p>
                        Merging my
                        newfound tech skills with
                        my <span>engineering background</span> , I'm eager to contribute and grow in the digital space.
                    </p>
                </div>

                <!-- Inserisco button per download  -->
                <div id="cv" class="cv-download">
                    <a href="../../public/manuel-cv.pdf" download="Manuel-CV.pdf" class="cv-button">Download
                        CV</a>
                </div>
            </div>


            <!-- Secondo contenuto (Sticker) -->
            <div class="emoj">
                <img src="../../public/hand-computer.jpeg" alt="">
            </div>



        </div>


        <!-- TOOLING -->
        <div class="tooling" id="tech">
            <div class="tooling-title">
                <h2>Technologies</h2>
                <i class="fas fa-wrench animated-icon"></i>
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
        <div class="work" id="portfolio">
            <div class="work-header">
                <div class="work-title">
                    <h2>Portfolio</h2>
                    <i class="fas fa-folder"></i> <!-- Questa è l'icona di FontAwesome -->
                </div>
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

                        <p>
                            I embarked on an advanced web development journey by recreating the look and feel of the
                            globally recognized platform: <span class="highlight">WhatsApp</span>. While the frontend
                            mirrors WhatsApp's UI, the real challenge was integrating real-time chat functionalities through
                            various <span class="highlight">APIs</span>. This project honed both my frontend and backend
                            skills, emphasizing the integration of third-party services.
                        </p>



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

                <!-- 3 Project -->
                <div class="single">
                    <div class="single-img">
                        <img src="../../public/Screenshot 2023-08-30 alle 13.00.08.png" alt="">
                    </div>

                    <div class="single-details">
                        <h4>Netflix</h4>

                        <p>This project is a <span class="highlight">modern interpretation</span> of the film and TV show
                            search concept, inspired by Netflix's aesthetic. Leveraging an API and axios calls, it allows
                            users to <span class="highlight">delve into detailed characteristics</span> of any film or TV
                            series. It stands as a testament to my advanced skills in <span class="highlight">API
                                integration</span> and interface design.</p>



                        <ul class="tech-used">
                            <li>HTML5</li>
                            <li>CSS3</li>
                            <li>Vue</li>
                            <li>Vite</li>
                        </ul>

                        <div class="last">
                            <p class="project-date"> <span>Completed :</span> June 2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/vite-boolflix">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Github Repo
                                </a>
                            </button>
                        </div>
                    </div>
                </div>


                <!-- 4 Project -->
                <div class="single">

                    <div class="single-details">
                        <h4>Interactive Project Management Platform</h4>

                        <p>This application is a comprehensive <span class="highlight">project management system</span>
                            tailored for professionals seeking robustness and clarity. With full <span
                                class="highlight">CRUD
                                functionalities</span>, users can effortlessly manage, visualize, and
                            collaborate on their projects as well as explore those created by other community members. The
                            underlying database architecture boasts intricate <span class="highlight">relational
                                tables</span>, ensuring data integrity and streamlined workflows.</p>



                        <ul class="tech-used">
                            <li>HTML5</li>
                            <li>CSS3</li>
                            <li>Laravel</li>
                            <li>php</li>
                            <li>Sass</li>
                        </ul>

                        <div class="last">
                            <p class="project-date"> <span>Completed :</span> August 2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/laravel-many-to-many">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Github Repo
                                </a>
                            </button>
                        </div>
                    </div>

                    <div class="single-img">
                        <img class="img-2" src="../../public/Screenshot 2023-08-29 alle 14.46.28.png" alt="">
                    </div>
                </div>

                <!-- 5 Project -->
                <div class="single">
                    <div class="single-img">
                        <video width="320" height="240" controls>
                            <source src="../../public/registrazione1.mov" type="video/mp4">
                            Your browser does not support the video tag.
                        </video>
                    </div>

                    <div class="single-details">
                        <h4>Data Analysis of European Football 2020</h4>

                        <p>This endeavor represents a detailed <span class="highlight">statistical analysis</span> of
                            footballers' performances in the UEFA Euro 2020 Championship. By meticulously dissecting
                            multiple datasets, the project illuminates patterns and insights across five distinct <span
                                class="highlight">visual representations</span>. Each graph is a culmination of dissected
                            columns from various datasets, seamlessly merged to provide a comprehensive view of players'
                            prowess and contributions during the tournament.</p>




                        <ul class="tech-used">
                            <li>Python</li>
                            <li>SQL</li>
                        </ul>

                        <div class="last">
                            <p class="project-date"> <span>Completed :</span> May 2022</p>


                            <button>
                                <a href="https://github.com/Manuell00/analysis-of-European-football">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Github Repo
                                </a>
                            </button>
                        </div>
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
            color: black;

            // First row of content
            .content-movement {
                margin-bottom: 1.5rem;
                width: max-content;
                padding-right: 5%;



                div {
                    padding: 0px 15px;
                    border-radius: 12px;
                    background-color: rgba(16, 233, 86, 1);
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
                        color: $green;
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
                    color: grey;

                    span {
                        color: $green;
                        text-transform: uppercase;
                    }
                }
            }

            .cv-button {
                display: inline-block;
                padding: 10px 20px;
                margin-top: 20px;
                background-color: #333;
                color: #fff;
                text-transform: uppercase;
                text-decoration: none;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;

                &:hover {
                    background-color: #555;
                }
            }

        }

        // SECONDO CONTENUTO
        .emoj {
            animation: slideFromRight 1s forwards;
            width: 50%;
            height: 100%;
            padding: 0 10%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: row;

            img {
                max-width: 800px;
                max-height: 800px;
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
        background-color: black;
        padding-bottom: 10rem;


        .tooling-title {
            align-items: center;
            background: linear-gradient(135deg, rgba(18, 20, 29, 0.8), rgba(28, 30, 39, 0.8));
            border-radius: 12px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: center;
            margin-bottom: 5rem;
            padding: 0 3rem;
            transition: 0.7s ease-in;

            &:hover {
                transform: scale(1.1);
                box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
            }

            .animated-icon {
                padding-left: 50px;
                padding-bottom: 30px;
                display: block;
                font-size: 2rem;
                animation: rotateIcon 8s infinite linear;
            }


            h2 {
                font-family: 'Arial', sans-serif;
                font-weight: 900;
                font-size: 2rem;
                text-transform: uppercase;
                color: white;
                letter-spacing: 1.5px;
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
            background: #12141d;


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

        .work-header {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 3rem 0;
            background: #f7f7f7;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);

            .work-title {
                align-items: center;
                border-radius: 12px;
                box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
                display: flex;
                justify-content: center;
                padding: 0 3rem;
                transition: 0.7s ease-in;

                i {
                    color: #333;
                    padding-left: 20px;
                    display: block;
                    font-size: 2rem;
                    animation: pulse 2s infinite;
                }

                h2 {
                    font-family: 'Arial', sans-serif;
                    font-weight: 900;
                    font-size: 2rem;
                    text-transform: uppercase;
                    color: #333;
                    letter-spacing: 1.5px;
                }

                &:hover {
                    transform: scale(1.1);
                    box-shadow: 0 7px 20px rgba(0, 0, 0, 0.3);
                }

            }



        }




        .projects {
            align-items: center;
            display: flex;
            flex-direction: column;
            justify-content: center;
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

                    img,
                    video {
                        border-radius: 15px;
                        box-shadow: 0 60px 123px -25px hsla(225, 2%, 62%, .42), 0 35px 75px -35px hsla(225, 2%, 62%, .08);
                        -webkit-filter: blur(0);
                        filter: blur(0);
                        height: 398px;
                        opacity: 1;
                        -webkit-transform: perspective(800px) rotateY(25deg) scale(.8) rotateX(10deg);
                        transition: all .6s ease;
                        width: 700px;
                        transform: perspective(800px) rotateY(25deg) scale(.8) rotateX(-5deg);


                        &:hover {
                            box-shadow: 0 19px 67px -38px hsla(225, 2%, 62%, .8);
                            -webkit-filter: blur(.2px);
                            filter: blur(.2px);
                            opacity: 1;
                            -webkit-transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(1.0);
                            transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(1.0);
                        }
                    }

                    .img-2 {
                        transform: perspective(800px) rotateY(-25deg) scale(.8) rotateX(5deg);

                        &:hover {
                            -webkit-transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(1.0);
                            transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(1.0);
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

                p {
                    font-family: 'Open Sans', sans-serif;
                    line-height: 1.6;
                    letter-spacing: 0.5px;
                    font-weight: 400;
                }


                h4 {
                    border: 2px solid $green;
                    /* Cambiato da dashed a solid */
                    box-shadow: 8px 8px 0 0 $green;
                    color: $green;
                    font-family: 'Futura';
                    font-weight: 600;
                    margin-bottom: 2rem;
                    padding: 1rem 1.5rem;
                    text-transform: capitalize;
                    transition: transform 0.5s ease-in-out, box-shadow 0.5s ease-in-out;

                    &:hover {
                        transform: rotate(5deg);
                        box-shadow: 12px 12px 0 0 $green;
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
                    border: 2px solid $green;
                    border-radius: 15px;
                    background-color: rgba($green, 0.1);
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
                        color: black;
                        padding: 0.5rem 1rem;
                        border-radius: 7px;
                        font-weight: 600;
                        transition: background-color 0.3s ease;

                        &:hover {
                            background-color: $green;
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
                            color: $green;
                            text-transform: capitalize;
                            transition: color 0.3s ease;

                            &:hover {
                                color: lighten($green, 15%);
                            }
                        }
                    }

                    button {
                        background-color: $green; // supponendo che tu voglia mantenere il tema viola, ma puoi sostituirlo con qualsiasi colore
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
                            background-color: darken($green, 15%); // scurisce il colore del pulsante quando si passa sopra con il mouse
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

@media (max-width: 2500px) {
    .container-fluid {

        .emoj {
            img {
                width: 700px;
                height: 700px;
            }
        }

        .work {
            .projects {
                .single {
                    .single-img {

                        img,
                        video {
                            width: 750px;
                            height: auto;
                        }
                    }

                }
            }

        }

    }
}

@media (max-width: 1700px) {
    .container-fluid .emoj {

        img {
            width: 500px;
            height: 500px;
        }
    }

    .container-fluid {
        .work {
            .projects {
                .single {
                    .single-details {
                        p {
                            font-size: 1.4rem;
                        }
                    }

                    .last {
                        .project-date {
                            font-size: 1.5rem;
                            text-align: center;

                        }
                    }

                }
            }

        }

    }
}

@media (max-width: 1500px) {

    .container-fluid {
        .work {
            .projects {
                .single {
                    .single-img {

                        img,
                        video {
                            width: 600px;
                            height: auto;
                        }
                    }

                    .single-details {
                        p {
                            font-size: 1.2rem;
                        }
                    }

                    .last {
                        .project-date {
                            font-size: 1.2rem;

                        }
                    }

                }
            }

        }


    }
}

@media (max-width: 1200px) {
    .container-fluid {

        .home-intro {
            flex-direction: column;

            .content {
                width: 70%;
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
                    width: 100%;
                    padding: 20px 0;

                    img {
                        width: 300px;
                        height: auto;
                    }
                }
            }
        }

        .work {
            .projects {
                .single {
                    flex-direction: column;
                    margin: 5rem 0;

                    .single-img {
                        order: 1;
                        margin-bottom: 3rem;

                        img,
                        .img-2,
                        video {
                            width: 700px;
                            transform: perspective(800px) rotateY(-25deg) scale(.8) rotateX(5deg);

                            &:hover {
                                -webkit-transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(0.9);
                                transform: perspective(800px) rotateY(0deg) translateY(0px) rotateX(0deg) scale(0.9);
                            }
                        }
                    }

                    .single-details {
                        order: 2;

                        p {
                            display: none;
                        }
                    }

                }
            }
        }
    }
}

@media (max-width: 768px) and (min-width: 577px) {
    .container-fluid {
        .home-intro {
            .content {
                .content-movement {
                    .sticker {
                        display: block;
                    }

                    div {
                        font-size: 1.5rem;
                    }
                }

                .content-primary h1 {
                    font-size: 1.8rem;

                    span {
                        font-size: 2.5rem;
                    }
                }

                .content-secondary p {
                    font-size: 1.2rem;
                }
            }

            .emoj img {
                width: 300px;
            }
        }

        .work {
            .projects {
                .single {
                    .single-img {

                        img,
                        video,
                        .img-2 {
                            width: 500px;
                            height: auto;
                        }
                    }

                }
            }

        }
    }
}

@media (max-width: 576px) {
    .container-fluid {
        .home-intro {
            .content {
                .content-movement {

                    div {
                        font-size: 1.8rem;

                        span {
                            display: block;
                            font-size: 1.8rem;
                            line-height: 3.0rem;

                        }
                    }
                }

                .content-primary h1 {
                    font-size: 2.3rem;

                    span {
                        font-size: 2.5rem;
                    }
                }

                .content-secondary p {
                    font-size: 1.5rem;
                }
            }

            .emoj img {
                width: 230px;
            }

        }

        #tech {
            .tooling-title {
                text-align: center;

                h2 {
                    font-size: 1.3rem;
                }

                a {
                    font-size: 1.3rem;
                }
            }

        }


        .work {
            .work-header {
                .work-title {
                    text-align: center;

                    h2 {
                        font-size: 1.5rem;
                    }

                    a {
                        font-size: 1.5rem;
                    }
                }
            }

            .projects {
                .single {
                    text-align: center;

                    .single-img {

                        img,
                        video,
                        .img-2 {
                            width: 400px;
                        }
                    }

                    .last {
                        display: flex;
                        align-items: center;
                        justify-content: center;
                        flex-direction: column;
                    }

                }
            }

        }
    }

}

@media (max-width: 450px) {
    .container-fluid {
        .home-intro {
            .content {
                line-height: 50px;

                .cv-button {
                    font-size: 1.3rem;
                }

                .content-movement {

                    div {
                        font-size: 1.3rem;


                        span {
                            display: block;
                            font-size: 1.3rem;

                        }
                    }
                }

                .content-primary h1 {
                    font-size: 1.5rem;

                    span {
                        font-size: 1.7rem;
                    }
                }

                .content-secondary p {
                    font-size: 1.5rem;
                }
            }

            .emoj img {
                width: 230px;
            }

        }


        #tech {
            .tooling-title {
                padding: 0;

                h2 {
                    font-size: 1.1rem;
                }

                i {
                    font-size: 1.1rem;
                }
            }

        }

        .work {

            .work-header {
                .work-title {
                    text-align: center;

                    h2 {
                        font-size: 1.1rem;
                    }

                    i {
                        font-size: 1.1rem;
                    }
                }
            }

            .projects {
                .single {

                    .single-img {

                        img,
                        video,
                        .img-2 {
                            width: 400px;
                        }
                    }

                }
            }

        }
    }

}


@media (max-width: 380px) {
    .container-fluid {
        .home-intro {
            .content {
                line-height: 50px;

                .cv-button {
                    font-size: 1.0rem;
                }

                .content-movement {

                    div {
                        font-size: 1.1rem;

                        span {
                            font-size: 1.1em;

                        }

                    }
                }

                .content-primary h1 {
                    font-size: 1.3rem;

                    span {
                        font-size: 1.5rem;
                    }
                }

                .content-secondary p {
                    font-size: 1.3rem;
                }
            }

            .emoj img {
                width: 200px;
            }

        }

        #tech {
            .tooling-title {

                h2 {
                    font-size: 0.9rem;
                }

                a {
                    font-size: 0.9rem;
                }
            }

        }

        .work {
            .work-header {
                .work-title {
                    text-align: center;

                    h2 {
                        font-size: 0.9rem;
                    }

                    i {
                        font-size: 0.9rem;
                    }
                }
            }

            .projects {
                .single {

                    .single-img {

                        img,
                        video,
                        .img-2 {
                            width: 300px;
                        }
                    }

                }
            }

        }
    }

}
</style>

