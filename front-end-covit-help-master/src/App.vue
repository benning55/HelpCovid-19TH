<template>
    <div id="app">
        <NavBar/>
        <transition name="fade" mode="out-in" @after-enter="beforeEnter">
<!--        <vue-page-transition name="fade">-->
            <router-view/>
<!--        </vue-page-transition>-->
        </transition>

    </div>
</template>

<script>
    import NavBar from './components/NavBar'

    export default {
        components: {
            NavBar,
        },
        methods: {
            beforeEnter() {
                this.$root.$emit('scrollBeforeEnter');
            }
        }
    }
</script>

<style>
    #app {
        font-family: 'Sarabun', sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;
    }

    #nav a {
        font-weight: bold;
        color: #2c3e50;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }

    .invalid-feedback {
        color: #f67575;
    }

    .border-image {
        border-radius: 5px 5px 5px 5px;
    }

    .el-dialog__body {
        break-word: break-word !important;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .2s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0;
    }


</style>
