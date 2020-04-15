<template>
    <div class="bg-light_green py-1">

        <div class="container">

            <h1 class="text-2xl mt-3 mb-3">ผู้ผลิต</h1>

            <div class="row">
                <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                    <CardSupplier :data="hospital"/>
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
                dataHospital: []
            }
        },
        created() {
            this.dataHospital = this.$store.state.dataHospital
            this.loadData()
        },
        methods: {
            loadData() {
                axios.get(`${this.$store.state.host}/api/util/maker/`)
                    .then(res => {
                        this.dataHospital = res.data.data
                        this.$store.commit("setDataAllSupplier", res.data.data);
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