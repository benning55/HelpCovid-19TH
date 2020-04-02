<template>
    <div>
        <h1 class="text-2xl mt-5 mb-3">สถานพยาบาล</h1>
        <div class="row">
            <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardHospital :data="hospital"/>
            </div>

        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import CardHospital from "../components/CardHospital";

    export default {
        data() {
            return {
                dataHospital: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/accounts/hospital/`)
                .then(res => {
                    this.dataHospital = res.data.data
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        },
        components: {
            CardHospital
        }
    }
</script>