<template>
    <div id="app">
        <NavBar/>
        <router-view/>
        <Footer v-if="$route.name!='Login'" />
    </div>
</template>

<script>
    import NavBar from './components/NavBar'
    import Footer from './components/Footer'

    export default {
        components: {
            NavBar,
            Footer
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

    .center-y {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }

    .invalid-feedback {
        color: #f67575;
    }
    .border-image{
        border-radius: 5px 5px 5px 5px;
    }

    .el-dialog__body{
        break-word:break-word !important;
    }
</style>
