<template>
    <div v-if="siteName.length > 0" class="row" style="margin-top: 10%;">
        <h1 style="color:white;">
            {{ siteName }}
        </h1>
        <h2 style="color:red;">
            We are currently developing this site 🛠️
        </h2>
    </div>
</template>
  
<script>
// import axios from 'axios'

// @ is an alias to /src  
export default {
    name: 'UnderDeveloping',
    props: {
        siteName: {
            type: String,
            default: '',
            required: true
        }
    }
}
</script>