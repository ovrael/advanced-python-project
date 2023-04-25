<template>
    <div>
        <h1>
            {{ aboutInfo }}
        </h1>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'GetAboutUsInfo',
    data() {
        return {
            aboutInfo: '',
        };
    },
    methods: {
        getMessage() {
            axios.get('/about')
                .then((res) => {
                    console.log("About us Axios GET THEN")
                    console.log(res)
                    this.aboutInfo = res.data;
                })
                .catch((error) => {
                    console.log("About us Axios GET CATCH")
                    console.error(error);
                });
        },
    },
    created() {
        console.log("About info created()")
        this.getMessage();
    },
};
</script>