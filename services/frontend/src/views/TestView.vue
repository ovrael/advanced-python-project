<template>
    <div>
        <img alt="Vue logo" src="../assets/logo.png">
        <Test />
        <Test />
        <img alt="Vue logo" src="../assets/logo.png" width="60">
        <Test />
        <Test />
        <img alt="Vue logo" src="../assets/logo.png" width="20">
        <img alt="Vue logo" src="../assets/logo.png" width="20">
        <img alt="Vue logo" src="../assets/logo.png" width="20">
        <img alt="Vue logo" src="../assets/logo.png" width="20">
        <img alt="Vue logo" src="../assets/logo.png" width="20">
        <img alt="Vue logo" src="../assets/logo.png" width="20">
    </div>
</template>
  
<script>
// @ is an alias to /src
import Test from '@/components/Test.vue'

export default {
    name: 'TestView',
    components: {
        Test
    }
}
</script>
  