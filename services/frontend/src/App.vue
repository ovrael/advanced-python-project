<template>
    <TopNavbar />
    <LeftNavbar />

    <div class="container mainContainer">
        <div id="app">
            <router-view />
        </div>
    </div>
</template>

<script>

// @ is an alias to /src
import TopNavbar from '@/components/TopNavbar.vue';
import LeftNavbar from '@/components/LeftNavbar.vue';

export default {
    components: {
        TopNavbar,
        LeftNavbar
    }
}
</script>

<style>
.mainContainer {
    padding-left: 200px !important;
}
</style>