<template>
    <div class="sideNav">
        <a class="sideNavOption text-center" href="/option1">Option 1</a>
        <a class="sideNavOption text-center" href="/option2">Option 2</a>
        <a class="sideNavOption text-center" href="/option3">Option 3</a>
        <a class="sideNavOption text-center" href="/option4">Option 4</a>
    </div>
</template>

<style>
.sideNav {
    height: calc(100% - 40px);
    width: 200px;

    position: absolute;
    left: 0;
    top: 40px;

    background-color: rgb(15, 15, 15);
    color: rgb(40, 120, 200);
}

.sideNavOption {
    height: 50px;
    line-height: 50px;
    width: 100%;
    text-decoration: none;
    display: block;
}

.sideNavOption:hover {
    color: black;
    background-color: rgb(40, 120, 200);
    cursor: pointer;
}
</style>