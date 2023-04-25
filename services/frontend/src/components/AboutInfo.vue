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
                    this.aboutInfo = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
        },
    },
    created() {
        this.getMessage();
    },
};
</script>