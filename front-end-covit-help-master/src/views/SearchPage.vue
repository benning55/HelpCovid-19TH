<template>
    <div class="container">
        <h1 class="text-2xl mt-5 mb-3">โรงพยาบาล</h1>
        <div v-if="dataHospital.length == 0" class="w-full h-32">
            <h1 class="center-y">ไม่พบสิ่งของที่คุณค้นหา</h1>
        </div>
        <div v-else class="row">
            <div v-for="hospital in dataHospital" :key="hospital.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardPost :data="hospital"/>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import CardPost from "../components/CardPost";

    export default {
        data() {
            return {
                dataHospital: []
            }
        },
        created() {
            axios.post(`${this.$store.state.host}/api/posts/search/`, {
                title: this.$route.params.title
            })
                .then(res => {
                    this.dataHospital = res.data.data
                })
                .catch()
        },
        components: {
            CardPost
        }
    }
</script>

<style>
    .center-y {
        margin: 0;
        position: absolute;
        top: 50%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
</style>