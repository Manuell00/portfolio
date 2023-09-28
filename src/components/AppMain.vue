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
                        <img src="../../public/spotify.png" alt="">
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
                                    Code
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

