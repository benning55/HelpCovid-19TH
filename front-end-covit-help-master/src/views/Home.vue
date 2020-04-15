<template>
    <div class="home">
        <HomePopUp v-show="show_modal" @close='close()'/>

        <Hero/>

        <div class="container">

            <SearchSection/>


            <h1 class="text-2xl mt-3 mb-2">ตำแหน่งของสถานที่รับบริจาค</h1>
            <p class="mb-3">(กดที่ไอคอนหมุดเพื่อขยาย กดอีกครั้งเพื่อไปยังหน้ารับบริจาค)</p>

            <GoogleMap/>

            <HomeSectionPost/>
        </div>

        <HomeSectionSupplier/>

        <div class="container">
            <HomeSectionHospital/>
        </div>

    </div>

</template>

<script>
    import Hero from '../components/Hero'
    import HomeSectionPost from "../components/HomeSectionPost";
    import HomeSectionHospital from "../components/HomeSectionHospital";
    import GoogleMap from "./GoogleMap";
    import SearchSection from "../components/SearchSection";
    import HomePopUp from "../components/HomePopUp";
    import HomeSectionSupplier from "../components/HomeSectionSupplier";


    export default {
        name: 'Home',
        components: {
            GoogleMap,
            Hero,
            HomeSectionPost,
            HomeSectionHospital,
            SearchSection,
            HomePopUp,
            HomeSectionSupplier,
        },
        data() {
            return {
                mapLocation: [],
                show_modal: true,
                sumObject: 0,
                sumMoney: 0
            }
        },
        created() {
            if (!this.$session.exists("popup")) {
                this.$session.set("popup", "show")
            } else {
                if (this.$session.get("popup") == "show") {
                    this.show_modal = true
                } else {
                    this.show_modal = false
                }
            }
        },
        methods: {

            close() {
                console.log("fffffff")
                this.show_modal = false
                this.$session.set("popup", "hide")
            }
        }
    }
</script>

<style scoped>
</style>
