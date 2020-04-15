<template>
    <div class="jumbotron bg-light_green">
        <div class="container flex-none md:flex">
            <div class="w-full md:w-1/2 md:mr-5">
                <h1 class="display-4 mb-3">ศูนย์รวมรับบริจาค</h1>
                <p class="lead">WebSite สำหรับ Donation Matching เพื่อให้ โรงพยาบาล และหน่วยงานทางการแพทย์ สามารถสร้าง
                    Request
                    ว่าขาดอะไรแล้ว ให้ ภาคประชาชน/เอกชน เข้ามาบริจาคแบบตรงความต้องการ(มีตัวเลือกให้บริจาคเงินด้วย)
                    ซึ่งจะเป็นการช่วยลดขั้นตอน/เวลา ในการที่บุคลากรทางการแพทย์จะได้รับความช่วยเหลือ
                    และเป็นการแบ่งเบาภาระภาครัฐ</p>
                <hr class="my-4">
                <div v-if="!$store.state.isAuthenticated">
                    <h1>
                        โรงพยาบาลและหน่วยงานทางการแพทย์สามารถส่ง email รายชื่อตัวแทนของหน่วยงานของท่าน โดยระบุ
                        ชื่อ-นามสกุล
                        ตำแหน่ง และเบอร์โทรศัพท์ มาที่ admin@covid19th.org และทำการลงทะเบียนได้

                    </h1>
                    <router-link to="/login">
                        <button type="button" class="btn bg-green text-white mt-4 hover:bg-hover_blue">
                            คลิกเพื่อลงทะเบียน
                        </button>
                    </router-link>
                </div>
                <button v-else @click="goDonateDashBoard" type="button"
                        class="btn bg-green hover:bg-hover_blue text-white">
                    ไปที่ Dashboard ของ
                    {{this.$store.state.authUser.hospital.name}}
                </button>
            </div>
            <div class="my-4 w-full md:w-1/2">
                <div class="shadow-lg flex rounded bg-white">
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
        </div>
    </div>
</template>

<script>
    import HomeChart from "../components/HomeChart";

    export default {
        components: {
            HomeChart
        },
        data() {
            return {
                sumObject: 0,
                sumMoney: 0
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
            goDonateDashBoard() {
                this.$router.push({
                    name: "DashboardHospital",
                    params: {id: this.$store.state.authUser.hospital.id}
                })
            }
        }
    }
</script>

<style>
    #bar-chart {
        height: 100px;
    }
</style>