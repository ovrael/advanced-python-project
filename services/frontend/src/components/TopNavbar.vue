<template>
    <div class="topNav">
        <a class="logo" href="/"> <img alt="Vue logo" src="../assets/logo2.png">
        </a>
        <a class="navButton" href="/contact">Contact</a>
        <a class="navButton" href="/about">About</a>
    </div>
</template>

<style>
/* Add a black background color to the top navigation */
.topNav {
    background: rgb(0, 0, 0);
    background: linear-gradient(90deg, rgba(0, 0, 0, 1) 0%, rgba(0, 0, 0, 1) 10%, rgb(40, 120, 200) 90%, rgb(40, 120, 200) 100%);
    overflow: hidden;
    height: 40px;
    line-height: 40px;
}

.topNav .logo {
    float: left;
    color: rgb(40, 120, 200);
    background-color: black;
    width: 200px;

    padding: 0px 16px;
    text-decoration: none;
    font-size: 22px;
    line-height: 30px !important;
}

.topNav .logo:hover {
    /* background-color: rgb(40, 120, 200);
    color: black; */

}

/* Style the links inside the navigation bar */
.topNav .navButton {
    float: right;
    color: black;
    text-align: center;
    padding: 0px 16px;
    text-decoration: none;
    font-size: 18px;
    font-weight: 500;
}

.topNav .navButton:hover {
    color: rgb(40, 120, 200);
    background-color: black;
}
</style>