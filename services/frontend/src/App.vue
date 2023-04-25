<template>
  <TopNavbar />
  <LeftNavbar />
  <div id="app">
    <router-view />
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
#app {
  margin-left: 120px;
  margin-top: 80px;
}
</style>