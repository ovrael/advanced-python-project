<template>
    <SideNavbar />

    <div id="app" class="container mainContainer">
        <router-view />
    </div>
</template>

<script>

// @ is an alias to /src
import SideNavbar from '@/components/SideNavbar.vue';

export default {
    components: {
        SideNavbar
    }
}
</script>

<style>
.mainContainer {
    padding-left: 200px !important;
}

body {
    background-color: transparent !important;
}

html {
    background-image: url('@/assets/img/background.svg') !important;
    background-size: contain;

    background-size: 100%;

    background-size: 100vw 100vh
}
</style>