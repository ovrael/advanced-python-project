<template>
  <div>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PingMessage',
  data() {
    console.log("Data()")
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      axios.get('/')
        .then((res) => {
          console.log("Axios GET THEN")
          console.log(res)
          this.msg = res.data;
        })
        .catch((error) => {
          console.log("Axios GET CATCH")
          console.error(error);
        });
    },
  },
  created() {
    console.log("Hello world vue created()")
    this.getMessage();
  },
};
</script>