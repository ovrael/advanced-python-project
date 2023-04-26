<template>
	<div>
		<p>{{ msg }}</p>
	</div>
	<div class="row">

	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'PingMessage',
	data() {
		return {
			msg: '',
		};
	},
	methods: {
		getMessage() {
			axios.get('/')
				.then((res) => {
					this.msg = res.data;
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

<style>
.blackBg {
	background-color: black;
}

.blueBg {
	background-color: blue;
}

.redBg {
	background-color: red;
}
</style>