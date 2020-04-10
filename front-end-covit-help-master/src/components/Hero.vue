<template>
    <div class="jumbotron bg-light_green">
        <div class="container">
            <h1 class="display-4 mb-3">ศูนย์รวมรับบริจาค</h1>
            <p class="lead">WebSite สำหรับ Donation Matching เพื่อให้ โรงพยาบาล และหน่วยงานทางการแพทย์ สามารถสร้าง
                Request
                ว่าขาดอะไรแล้ว ให้ ภาคประชาชน/เอกชน เข้ามาบริจาคแบบตรงความต้องการ(มีตัวเลือกให้บริจาคเงินด้วย)
                ซึ่งจะเป็นการช่วยลดขั้นตอน/เวลา ในการที่บุคลากรทางการแพทย์จะได้รับความช่วยเหลือ
                และเป็นการแบ่งเบาภาระภาครัฐ</p>
            <hr class="my-4">
            <div v-if="!$store.state.isAuthenticated">
                <h1>
                    โรงพยาบาลและหน่วยงานทางการแพทย์สามารถส่ง email รายชื่อตัวแทนของหน่วยงานของท่าน โดยระบุ ชื่อ-นามสกุล
                    ตำแหน่ง และเบอร์โทรศัพท์ มาที่ admin@covid19th.org และทำการลงทะเบียนได้

                </h1>
                <router-link to="/login">
                    <button type="button" class="btn bg-green text-white mt-4 hover:bg-hover_blue">คลิกเพื่อลงทะเบียน</button>
                </router-link>
            </div>
            <button v-else @click="goDonateDashBoard" type="button" class="btn bg-green hover:bg-hover_blue text-white">
                ไปที่ Dashboard ของ
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