<template>
    <div class="home">
        <HomePopUp v-show="show_modal" @close="show_modal = false" />

        <Hero/>

        <div class="container">
            <SearchSection/>
            <h1 class="text-2xl mt-3 mb-2">ตำแหน่งของสถานที่รับบริจาค</h1>
            <p class="mb-3">(กดที่ไอคอนหมุดเพื่อขยาย กดอีกครั้งเพื่อไปยังหน้ารับบริจาค)</p>

            <GoogleMap/>
            <HomeSectionPost/>
            <HomeSectionHospital/>
        </div>

    </div>

</template>

<script>
    // @ is an alias to /src
    import axios from 'axios'
    import Hero from '../components/Hero'
    import HomeSectionPost from "../components/HomeSectionPost";
    import HomeSectionHospital from "../components/HomeSectionHospital";
    import GoogleMap from "./GoogleMap";
    import SearchSection from "../components/SearchSection";
    import HomePopUp from "../components/HomePopUp";

    export default {
        name: 'Home',
        components: {
            GoogleMap,
            Hero,
            HomeSectionPost,
            HomeSectionHospital,
            SearchSection,
            HomePopUp
        },
        data() {
            return {
                mapLocation: [],
                show_modal: true
            }
        },
        created() {

        },
    }
</script>

<style scoped>
</style>
