<template>
    <div class="sideNav">
        <div class="topOptions">

            <router-link to="/" class="logo text-center" @click="changePage('')">
                <img alt="Logo" class="logoImage" src="@/assets/img/aiToolsLogo.png">
            </router-link>

            <router-link to="/imageToText" active-class="active" class="sideNavOption text-center">
                Image to text
            </router-link>

            <router-link to="/spamDetection" active-class="active" class="sideNavOption text-center">
                Spam detection
            </router-link>

            <router-link to="/textAnalysis" active-class="active" class="sideNavOption text-center">
                Text analysis
            </router-link>

            <router-link to="/imageAnalysis" active-class="active" class="sideNavOption text-center">
                Image analysis
            </router-link>

            <router-link to="/speechToText" active-class="active" class="sideNavOption text-center">
                Speech to text
            </router-link>

        </div>

        <div class="bottomOptions">
            <router-link to="/about" active-class="active" class="sideNavOption text-center">
                About
            </router-link>
        </div>
    </div>
</template>

<script>
export default {
    name: 'SideNavbar',
    data() {
        return {
            currentPage: '',
        };
    },
    methods: {
        changePage(pageName) {
            this.currentPage = pageName;
        },
    },
};
</script>

<style>
.logo {
    height: 60px;
    line-height: 50px;
    width: 100%;
    display: block;
}

.logoImage {
    margin: 0 auto;
}

.sideNav {
    height: 100%;
    width: 200px;

    position: absolute;
    left: 0;
    top: 0;

    background-color: rgb(15, 15, 15);
    color: #2878c8;
}

.sideNavOption {
    height: 50px;
    line-height: 50px;
    width: 100%;
    text-decoration: none;
    display: block;
}

.bottomOptions {
    position: absolute;
    bottom: 0;
    left: 0;

    width: 200px;
    height: 50px;
}

.active {
    color: black;
    background-color: rgb(17, 95, 173);
}

.sideNavOption:hover {
    color: black;
    background-color: rgb(40, 120, 200);
    cursor: pointer;
}
</style>