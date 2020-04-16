<template>
    <div>
        <h1 class="text-2xl mt-5 mb-3">สถานพยาบาล</h1>

        <div class="row">
            <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardHospital :data="hospital"/>
            </div>
            <div v-if="showSeeMore" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 hover:no-underline">
                <router-link to="/all-hospital">
                    <div class="shadow-lg  h-full text-center" style="margin-bottom: 15px;border-radius: 10px">
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
</template>

<script>
    import axios from 'axios'
    import CardHospital from "../components/CardHospital";

    export default {
        components: {
            CardHospital
        },
        data() {
            return {
                dataHospital: [],
                showSeeMore: false
            }
        },
        created() {
            if (this.$store.state.dataAllHospital.length == 0) {
                this.dataHospital = []
            } else if (this.$store.state.dataAllHospital.length > 12) {
                this.dataHospital = this.$store.state.dataAllHospital.slice(0, 11)
                this.showSeeMore = true
            } else {
                this.dataHospital = this.$store.state.dataAllHospital.slice(0, 12)
                this.showSeeMore = false
            }
            this.loadData()
        },
        methods: {
            loadData() {
                axios.get(`${this.$store.state.host}/api/accounts/hospital/`)
                    .then(res => {
                        this.$store.commit("setDataAllHospital", res.data.data);
                        if (this.$store.state.dataAllHospital.length == 0) {
                            this.dataHospital = []
                        } else if (this.$store.state.dataAllHospital.length > 12) {
                            this.dataHospital = this.$store.state.dataAllHospital.slice(0, 11)
                            this.showSeeMore = true
                        } else {
                            this.dataHospital = this.$store.state.dataAllHospital.slice(0, 12)
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