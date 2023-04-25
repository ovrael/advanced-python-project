<template>
    <div class="about">
        <AboutInfo />
    </div>
</template>

<script>
// @ is an alias to /src
import AboutInfo from '@/components/AboutInfo.vue'

export default {
    name: 'AboutUsView',
    components: {
        AboutInfo
    }
}
</script>
