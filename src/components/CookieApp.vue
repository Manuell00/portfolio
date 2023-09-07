<script>
// Importo lo STORE
import { store } from '../store.js';

// EXPORT
export default {
    name: 'CookieApp',

    data() {
        return {
            store,
            showBanner: true,
            hasUserAcceptedCookies: false,
        }
    },
    created() {
        const cookiePreference = this.$cookies.get("cookiePreference");

        if (cookiePreference) {
            if (cookiePreference === 'accepted') {
                console.log('Il cookie "cookiePreference" è registrato con il valore "accepted".');
                this.hasUserAcceptedCookies = true;
                this.showBanner = false;

                console.log('Il cookie scadrà in meno di 24 ore.');
            }
        } else {
            this.showBanner = true;
        }
    },




    methods: {
        acceptCookies() {
            // Qui puoi iniziare ad impostare i cookie non essenziali
            this.$cookies.set("cookiePreference", "accepted", "1d");
            console.log("L'utente ha accettato i cookie.");
            this.showBanner = false;

        },

        declineCookies() {
            // Non impostare i cookie non essenziali
            this.$cookies.set("cookiePreference", "declined", "1d");
            console.log("L'utente NON ha accettato i cookie.");
            this.showBanner = false;

        }
    }
}
</script>

<template>
    <div class="cookie" v-if="showBanner && !hasUserAcceptedCookies">
        <p>This website uses cookies solely to store your preferences. <a
                href="https://termly.io/resources/templates/cookie-policy-template/">Learn more.</a>
        </p>
        <button class="accept" @click="acceptCookies">Accept</button>
        <button class="decline" @click="declineCookies">Decline</button>

    </div>
</template>


<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;

.cookie {
    font-family: Arial, Helvetica, sans-serif;
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background-color: $green-rgba;
    border-top-left-radius: 5px;
    border-top-right-radius: 5px;
    padding: 15px 10px; // Padding ridotto per dispositivi mobile
    width: 100%;
    text-align: center;
    box-shadow: 0 -4px 8px rgba(0, 0, 0, 0.1);

    p {
        font-size: 1.6rem; // Dimensione del font ridotta per mobile

        a {
            color: #333;
            text-decoration: none;

            &:hover {
                text-decoration: underline;
            }
        }
    }

    button {
        background-color: $green;
        font-size: 1.6rem;
        border: none;
        border-radius: 5px;
        color: white;
        cursor: pointer;
        display: inline-block;
        padding: 8px 15px;
        margin: 0 10px;

        &.accept {
            background-color: darken($green, 15%); // Verde più scuro per il bottone "Accept"

            &:hover {
                background-color: darken($green, 25%);
            }
        }

        &.decline {
            background-color: #333; // Grigio scuro per il bottone "Decline"

            &:hover {
                background-color: #555;
            }
        }
    }
}

// MEDIA QUERY

@media (max-width: 768px) {
    .cookie {
        padding: 20px;

        p {
            font-size: 1.5rem;

            a {
                font-size: 1.5rem;

            }
        }

        button {
            font-size: 1.0rem;
            margin: 0 10px;
            padding: 10px 20px;
        }
    }
}

@media (max-width: 500px) {
    .cookie {
        p {
            font-size: 1rem;

            a {
                font-size: 1.0rem;

            }
        }

        button {
            font-size: 1.0rem;
            margin: 0 10px;
            padding: 10px 20px;
        }
    }
}
</style>
