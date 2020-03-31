<template>
    <div class="home">
        <Hero/>

        <div class="container">
            <h1 class="text-2xl mt-3 mb-2">ตำแหน่งของสถานที่รับบริจาค</h1>
            <p class="mb-3">(กดที่ไอคอนหมุดเพื่อขยาย กดอีกครั้งเพื่อไปยังหน้ารับบริจาค)</p>
            <GoogleMap :position="mapLocation"/>
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

    export default {
        name: 'Home',
        components: {
            GoogleMap,
            Hero,
            HomeSectionPost,
            HomeSectionHospital
        },
        data() {
            return {
                mapLocation: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/posts/donate/1/`)
                .then(res => {
                    this.mapLocation = res.data
                })
                .catch(e => {
                    console.log(e)
                })
        }
    }
</script>
