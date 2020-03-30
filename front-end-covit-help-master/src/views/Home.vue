<template>
    <div class="home">
        <Hero/>
        <GoogleMap/>
        <div class="container">
          <HomeSectionPost/>
          <HomeSectionHospital/>
        </div>
    </div>
</template>

<script>
    // @ is an alias to /src
    import Hero from '../components/Hero'
    import HomeSectionPost from "../components/HomeSectionPost";
    import HomeSectionHospital from "../components/HomeSectionHospital";
    import GoogleMap from "./GoogleMap";

    export default {
        name: 'Home',
        components: {
            GoogleMap,
            Hero,
            HomeSectionPost,
            HomeSectionHospital
        }
    }
</script>
