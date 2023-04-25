<template>
    <div>
        <h1>
            {{ testingData }}
        </h1>
    </div>
</template>
  
<script>
import axios from 'axios';

export default {
    name: 'TestingDocker',
    data() {
        return {
            testingData: '',
        };
    },
    methods: {
        getMessage() {
            axios.get('/test')
                .then((res) => {
                    this.testingData = res.data;
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