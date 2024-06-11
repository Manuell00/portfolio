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

        <div id="first">
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
                            Data Analyst & Management Engineer.
                        </h1>
                    </div>

                    <div class="content-secondary">
                        <p>
                            Fresh out of Bechelor Degree in Management Engineering, I took a 6-month deep dive into coding.
                        </p>

                        <p>
                            Now, <span>Data analysis</span> and <span>web application
                                development</span> capture my focus.
                        </p>
                    </div>
                </div>
            </div>


            <!-- TOOLING -->
            <div class="tooling" id="tech">

                <!-- Riga di titolo -->
                <div class="tooling-header">
                    <div class="tooling-title">
                        <h2>Technologies</h2>
                        <i class="fas fa-wrench animated-icon"></i>
                    </div>
                </div>

                <!-- Riga elementi -->
                <div class="tooling-element">
                    <div class="tooling-box">

                        <!-- Frontend Frameworks -->
                        <!-- Contenitore React -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-react"></i>
                            </div>
                            <div class="techname">
                                React
                            </div>
                        </div>
                        <!-- Contenitore Vue -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-vuejs"></i>
                            </div>
                            <div class="techname">
                                Vue.js
                            </div>
                        </div>

                        <!-- Backend Frameworks -->
                        <!-- Contenitore Laravel -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-laravel"></i>
                            </div>
                            <div class="techname">
                                Laravel
                            </div>
                        </div>

                        <!-- Languages -->
                        <!-- Contenitore Python -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-python"></i>
                            </div>
                            <div class="techname">
                                Python
                            </div>
                        </div>
                        <!-- Contenitore Javascript -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-js"></i>
                            </div>
                            <div class="techname">
                                JavaScript
                            </div>
                        </div>
                        <!-- Contenitore PHP -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-php"></i>
                            </div>
                            <div class="techname">
                                PHP
                            </div>
                        </div>

                        <!-- Styling -->
                        <!-- Contenitore SASS -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-sass"></i>
                            </div>
                            <div class="techname">
                                SASS
                            </div>
                        </div>
                        <!-- Contenitore Tailwind -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-tailwind-css"></i>
                            </div>
                            <div class="techname">
                                Tailwind CSS
                            </div>
                        </div>
                        <!-- Contenitore HTML -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-html5"></i>
                            </div>
                            <div class="techname">
                                HTML
                            </div>
                        </div>
                        <!-- Contenitore CSS -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-css3-alt"></i>
                            </div>
                            <div class="techname">
                                CSS
                            </div>
                        </div>

                        <!-- Database -->
                        <!-- Contenitore SQL -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-solid fa-database"></i>
                            </div>
                            <div class="techname">
                                SQL
                            </div>
                        </div>
                        <!-- Contenitore Office -->
                        <div class="box-content">
                            <div class="box-icon">
                                <i class="fa-brands fa-windows"></i>
                            </div>
                            <div class="techname">
                                Office
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        </div>


        <!-- MY WORKS -->
        <div class="work" id="portfolio">
            <div class="work-header">
                <div class="work-title">
                    <h2>My Projects</h2>
                    <i class="fa-solid fa-diagram-project"></i>
                </div>
            </div>



            <!-- PROJECTS -->
            <div class="projects">

                <!-- 1 Project -->
                <div class="single">
                    <div class="single-img">
                        <img src="../../public/spotify.png" alt="">
                    </div>

                    <div class="single-details">
                        <h4>Spotify Web</h4>

                        <div class="desc">
                            <p>This project is a <span class="highlight">meticulous recreation</span> of
                                Spotify's main web
                                application page. Crafted as one of my <span class="highlight">initial endeavors</span> into
                                web
                                design, it showcases my foundational skills in <span class="highlight">frontend
                                    development
                                </span>.
                            </p>
                            <div class="button-row">
                                <button>
                                    <a href="https://github.com/Manuell00/html-css-spotifyweb">
                                        <i class="fa-solid fa-arrow-right"></i>
                                        Code
                                    </a>
                                </button>
                            </div>
                        </div>




                        <ul class="tech-used">
                            <li>HTML5</li>
                            <li>CSS3</li>
                        </ul>

                    </div>
                </div>



                <!-- 2 Project -->
                <div class="single">

                    <div class="single-details">
                        <h4>Whatsapp</h4>

                        <p class="desc">
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
                            <p class="project-date"> <span>Completed :</span> <i class="fa-regular fa-calendar"></i> - May
                                2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/vue-boolzapp">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Code
                                </a>
                            </button>
                        </div>
                    </div>

                    <div class="single-img">
                        <img class="img-2" src="../../public/whatsapp.png" alt="">
                    </div>
                </div>

                <!-- 3 Project -->
                <div class="single">
                    <div class="single-img">
                        <img src="../../public/netflix.png" alt="">
                    </div>

                    <div class="single-details">
                        <h4>Netflix</h4>

                        <p class="desc">This project is a <span class="highlight">modern interpretation</span> of the film
                            and TV show
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
                            <p class="project-date"> <span>Completed :</span> <i class="fa-regular fa-calendar"></i> - June
                                2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/vite-boolflix">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Code
                                </a>
                            </button>
                        </div>
                    </div>
                </div>


                <!-- 4 Project -->
                <div class="single">

                    <div class="single-details">
                        <h4>Interactive Project Management Platform</h4>

                        <p class="desc">This application is a comprehensive <span class="highlight">project management
                                system</span>
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
                            <p class="project-date"> <span>Completed :</span> <i class="fa-regular fa-calendar"></i> -
                                August 2023</p>


                            <button>
                                <a href="https://github.com/Manuell00/laravel-many-to-many">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Code
                                </a>
                            </button>
                        </div>
                    </div>

                    <div class="single-img">
                        <img class="img-2" src="../../public/management.png" alt="">
                    </div>
                </div>

                <!-- 5 Project -->
                <div class="single">
                    <div class="single-img">
                        <img src="../../public/analysis.png" alt="">
                    </div>

                    <div class="single-details">
                        <h4>Data Analysis of European Football 2020</h4>

                        <p class="desc">This endeavor represents a detailed <span class="highlight">statistical
                                analysis</span> of
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
                            <p class="project-date"> <span>Completed :</span> <i class="fa-regular fa-calendar"></i> - May
                                2022</p>


                            <button>
                                <a href="https://github.com/Manuell00/analysis-of-European-football">
                                    <i class="fa-solid fa-arrow-right"></i>
                                    Code
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
@use '../styles/main.scss';
@use '../styles/partials/_variables.scss' as *;
</style>

