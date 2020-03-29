<template>
    <div class="home">
        <Hero/>
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

    export default {
        name: 'Home',
        components: {
            Hero,
            HomeSectionPost,
            HomeSectionHospital
        }
    }
</script>
