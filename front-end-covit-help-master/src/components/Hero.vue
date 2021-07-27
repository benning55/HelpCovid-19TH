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
                        ตำแหน่ง และเบอร์โทรศัพท์ มาที่ info@helpital.org และทำการลงทะเบียนได้

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
                <!--                <HomeChart @data="emitData"/>-->
                <div class="shadow-lg rounded bg-white">
                    <div class="flex flex-wrap">
                        <div class="w-1/2 sm:w-1/4 md:w-1/2 lg:w-1/4 border-b sm:border-0 md:border-b lg:border-0 py-4 text-center border-right border-dark">
                            <h1 class="text-3xl text-green py-2">{{objects[0]}}</h1>
                            <h1 class="text-md">สิ่งก่อสร้าง</h1>
                        </div>
                        <div class="w-1/2 sm:w-1/4 md:w-1/2 lg:w-1/4 border-b sm:border-b-0 md:border-b lg:border-b-0 border-r-0 sm:border-r md:border-r-0 lg:border-r py-4 text-center  border-dark">
                            <h1 class="text-3xl text-green py-2">{{objects[1]}}</h1>
                            <h1 class="text-md">ปรับปรุงโครงสร้าง</h1>
                        </div>
                        <div class="w-1/2 sm:w-1/4 md:w-1/2 lg:w-1/4 py-4 text-center border-right border-dark">
                            <h1 class="text-3xl text-green py-2">{{objects[2]}}</h1>
                            <h1 class="text-md">เครื่องมือแพทย์</h1>
                        </div>
                        <div class="w-1/2 sm:w-1/4 md:w-1/2 lg:w-1/4 py-4 text-center">
                            <h1 class="text-3xl text-green py-2">{{objects[3]}}</h1>
                            <h1 class="text-md">วัสดุการแพทย์</h1>
                        </div>

                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import HomeChart from "../components/HomeChart";
    import axios from "axios";

    export default {
        components: {
            HomeChart
        },
        data() {
            return {
                sumObject: 0,
                sumMoney: 0,
                objects: []
            }
        },
        created() {
            this.getData()
        },
        methods: {
            getData() {
                axios.get(`${this.$store.state.host}/api/util/chart/`)
                    .then(res => {
                        this.objects = res.data.data
                        this.sumObject = res.data.data.reduce((a, b) => a + b, 0)
                        this.sumMoney = res.data.total_money
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response,
                            type: 'error',
                            duration: 10
                        });
                    })
            },
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