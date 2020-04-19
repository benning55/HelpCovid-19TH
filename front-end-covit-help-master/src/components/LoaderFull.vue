<template>
    <transition>
        <div class="fixed opacity-80 h-full w-full z-10">
            <img width="100px" class="center-y" src="../assets/Rolling-1s-200px.svg" alt="Loading...">
        </div>
    </transition>

</template>

<script>
    export default {
        data() {
            return {}
        }
    }
</script>

<style scoped>
    .center {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

    .opacity-80 {
        background-color: rgba(255, 255, 255, 1);
        top: 0;
        left: 0;
    }
</style>