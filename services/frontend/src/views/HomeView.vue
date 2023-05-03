<template>
    <div class="text-center welcome">
        <h1>
            Welcome
        </h1>
        <hr id="welcomeDividor" class="dividor">
        <br>
        <h5>
            Multiple <aiTools>AI tools</aiTools> to easy your life.
        </h5>
    </div>
</template>

<script>
export default {
    name: 'HomeView',
    mounted() {
        console.log('Loaded home view.')
    }
}
</script>

<style>
aiTools {
    color: rgb(40, 120, 200);
}

.welcome {
    color: rgba(200, 200, 200, 0.9);
    padding-top: 25%;
}

.dividor {
    position: relative;
    width: 0px;
    height: 2px;
    margin: 0 auto;
    animation-name: expand;
    animation-duration: 1.5s;
    animation-fill-mode: forwards;
}

.dividor::before,
.dividor::after {
    content: '';
    position: absolute;
    top: 0;
    width: 0px;
    height: 2px;
    animation-duration: 1.5s;
    animation-fill-mode: forwards;
}

.dividor::before {
    left: -300px;
    animation-name: expand-left;
}

.dividor::after {
    right: -300px;
    animation-name: expand-right;
}

@keyframes expand {
    0% {
        width: 0px;
    }

    100% {
        width: 600px;
    }
}

@keyframes expand-left {
    0% {
        width: 0px;
        left: -300px;
    }

    100% {
        width: 300px;
        left: 0;
    }
}

@keyframes expand-right {
    0% {
        width: 0px;
        right: -200px;
    }

    100% {
        width: 200px;
        right: 0;
    }
}
</style>