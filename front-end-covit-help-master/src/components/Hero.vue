<template>
    <div class="jumbotron bg-light_green">
        <div class="container">
            <h1 class="display-4 mb-3">ศูนย์รวมรับบริจาค</h1>
            <p class="lead">เว็บไซต์นี้มีจุดประสงค์เพื่อเป็นแหล่งรวมรับบริจาค
                ให้แก่สถานพยาบาลและหน่วยงานที่เกี่ยวข้องเพื่อรับมือกับโรงระบาด Covid-19</p>
            <hr class="my-4">
            <h1 v-if="!$store.state.isAuthenticated">
                สำหรับสถานพยาบาลหรือหน่วยงานที่เกี่ยวข้องสามารถลงทะเบียนเพื่อขอรับบริจาคได้
                <router-link to="/login"><span class="text-green">ที่นี่</span></router-link>
            </h1>
            <button v-else @click="goDonateDashBoard" type="button" class="btn bg-green hover:bg-darkgreen text-white">ไปที่ Dashboard ของ
                {{this.$store.state.authUser.hospital.name}}
            </button>
        </div>
    </div>
</template>

<script>
    export default {
        methods: {
            goDonateDashBoard() {
                this.$router.push({
                    name: "DashboardHospital",
                    params: {id: this.$store.state.authUser.hospital.id}
                })
            }
        }
    }
</script>