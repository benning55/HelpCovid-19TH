<template>
    <div class="bg-light_green py-1">

        <div class="container">

            <h1 class="text-2xl mt-3 mb-3">สถานที่ฉีดวัคซีน</h1>

            <div class="row">
                <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                    <CardSupplier :data="hospital"/>
                </div>
                <div v-if="showSeeMore" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 hover:no-underline">
                    <router-link to="/all-supplier">
                        <div class="shadow-lg bg-white h-full text-center" style="margin-bottom: 15px;border-radius: 10px">
                            <div class="card-title font-bold text-key_column opacity-50 h-full" style="">
                                <div class="relative w-full" style="top: 50%;transform: translateY(-50%);">
                                    <i class="fas fa-plus mb-4" style="font-size: 5rem"></i>
                                    <h1 class="hover:no-underline">ดูเพิ่มเติม</h1>
                                </div>
                            </div>
                        </div>
                    </router-link>
                </div>
            </div>

        </div>


    </div>
</template>

<script>
    import axios from 'axios'
    import CardSupplier from "./CardSupplier";

    export default {
        components: {
            CardSupplier
        },
        data() {
            return {
                dataHospital: [],
                showSeeMore: false
            }
        },
        created() {
            if (this.$store.state.dataAllSupplier.length == 0) {
                this.dataHospital = []
            } else if (this.$store.state.dataAllSupplier.length > 12) {
                this.dataHospital = this.$store.state.dataAllSupplier.slice(0, 11)
                this.showSeeMore = true
            } else {
                this.dataHospital = this.$store.state.dataAllSupplier.slice(0, 12)
                this.showSeeMore = false
            }
            this.loadData()
        },
        methods: {
            loadData() {
                axios.get(`${this.$store.state.host}/api/util/maker/`)
                    .then(res => {
                        this.$store.commit("setDataAllSupplier", res.data.data);
                        if (this.$store.state.dataAllSupplier.length == 0) {
                            this.dataHospital = []
                        } else if (this.$store.state.dataAllSupplier.length > 12) {
                            this.dataHospital = this.$store.state.dataAllSupplier.slice(0, 11)
                            this.showSeeMore = true
                        } else {
                            this.dataHospital = this.$store.state.dataAllSupplier.slice(0, 12)
                            this.showSeeMore = false
                        }
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration: 10
                        });
                    })
            }
        }
    }
</script>