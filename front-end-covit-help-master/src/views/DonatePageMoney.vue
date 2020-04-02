<template>
    <div class="container">
          <h1 class="text-2xl mt-5 mb-3">โรงพยาบาล</h1>
        <div class="row">
            <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardHospital :data="hospital"/>
            </div>
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardHospital/>-->
<!--            </div>-->
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardHospital/>-->
<!--            </div>-->
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardHospital/>-->
<!--            </div>-->
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
                .then(res=>{
                    this.dataHospital = res.data.data
                })
                .catch(e=>{
                    console.log(e.response)
                })
        },
        components: {
            CardHospital
        }
    }
</script>