<template>
    <div class="home">
        <HomePopUp v-show="show_modal" @close='close()'/>

        <Hero/>

        <div class="container">

            <SearchSection/>

            <div class="my-4">
                <div class="shadow-lg flex rounded bg-light_green">
                    <div class="w-1/2 py-4 text-center border-right border-dark">
                        <h1 class="text-3xl text-green py-2">{{numberWithCommas(sumMoney)}}</h1>
                        <h1 class="text-md">ยอดเงินบริจาคทั้งหมด</h1>
                    </div>
                    <div class="w-1/2 py-4 text-center">
                        <h1 class="text-3xl text-green py-2">{{sumObject}}</h1>
                        <h1 class="text-md">ยอดสิ่งของบริจาคทั้งหมด</h1>
                    </div>
                </div>
                <h1 class="text-2xl mt-3 mb-2">ยอดบริจาคสิ่งของแต่ละประเภท</h1>
                <HomeChart @data="emitData"/>
            </div>


            <h1 class="text-2xl mt-3 mb-2">ตำแหน่งของสถานที่รับบริจาค</h1>
            <p class="mb-3">(กดที่ไอคอนหมุดเพื่อขยาย กดอีกครั้งเพื่อไปยังหน้ารับบริจาค)</p>

            <GoogleMap/>

            <HomeSectionPost/>

            <HomeSectionSupplier/>

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
    import HomeChart from "../components/HomeChart";

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
            HomeChart
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
            emitData(data) {
                this.sumMoney = data[0]
                this.sumObject = data[1]
                // console.log(data)
            }, numberWithCommas(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
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
