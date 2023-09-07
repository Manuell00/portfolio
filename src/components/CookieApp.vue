<script>
// Importo lo STORE
import { store } from '../store.js';
import CookieLaw from 'vue-cookie-law';

// Inserisco l'EXPORT
export default {
    name: 'CookieApp',

    data() {
        return {
            store,
        }
    },

    methods: {
        components: { CookieLaw }
    }

}
</script>

<!-- TEMPLATE -->
<template>
    <!-- <cookie-law theme="dark-lime"></cookie-law> -->
</template>




<!-- STYLE -->
<style scoped lang="scss">
@use '../styles/general.scss';
@use '../styles/partials/_variables.scss' as *;
</style>
