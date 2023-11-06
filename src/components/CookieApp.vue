<script>
export default {
    name: 'Cookie',
    data() {
        return {
            hasResponded: false
        };
    },
    mounted() {
        this.hasResponded = this.$cookies.isKey('cookieResponse');
        document.body.style.overflow = this.hasResponded ? '' : 'hidden';
    },
    methods: {
        giveConsent() {
            this.$cookies.set('cookieResponse', 'accepted', '24h');
            this.hasResponded = true;
        },
        refuseConsent() {
            this.$cookies.set('cookieResponse', 'refused', '24h');
            this.hasResponded = true;
        }
    },
    watch: {
        hasResponded(newVal) {
            if (!newVal) {
                document.body.style.overflow = 'hidden';
            } else {
                document.body.style.overflow = '';
            }
        }
    },
};
</script>

<template>
    <section id="cookie-section" v-if="!hasResponded">
        <div class="overlay"></div>
        <div class="cookie-card">
            <span class="title">🍪 Informativa sui Cookie</span>
            <p class="description">Il mio sito portfolio utilizza i cookie per migliorare la tua navigazione garantendo
                un'esperienza sicura e personalizzata.
            </p>
            <p class="minimal">Per maggiori informazioni leggi :
                <a
                    href="https://www.cookielawinfo.com/cookie-law/#:~:text=The%20cookie%20law%20requires%20websites,block%20the%20cookies%20from%20loading.">Politiche
                    sui cookies
                </a>.
            </p>

            <div class="actions">
                <!-- Bottone accettazione -->
                <button @click="giveConsent" class="accept">
                    Accetto
                </button>
                <!-- Bottone rifiuto -->
                <button @click="refuseConsent" class="accept">
                    Rifiuto
                </button>
            </div>
        </div>
    </section>
</template>

  <!-- STYLE  -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/cookie.scss';
@use '../styles/partials/_variables.scss' as *;
</style>
