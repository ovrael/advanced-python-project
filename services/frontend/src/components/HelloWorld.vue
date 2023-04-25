<template>
	<div>
		<p>{{ msg }}</p>
	</div>
	<div class="row">
		<div class="col-2 blackBg">
			COL-2 COL-2
		</div>
		<div class="col-3 redBg">
			COL-3 COL-3 COL-3
		</div>
		<div class="col-7 blueBg">
			COL-7 COL-7 COL-7 COL-7 COL-7 COL-7 COL-7
		</div>
	</div>
	<div class="row">
		<div class="col-2">
			<button type="button" class="btn btn-outline-success">Success</button>
		</div>
		<div class="col-3">
			<button type="button" class="btn btn-danger">Danger</button>
		</div>
		<div class="col-7">
			<button type="button" class="btn btn-primary">Primary</button>
		</div>
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