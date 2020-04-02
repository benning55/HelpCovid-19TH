<template>
    <div>
        <nav class="navbar text-white navbar-expand-lg text-white navbar-dark bg-green fixed w-full z-10">
            <a @click="goHome" class="navbar-brand cursor-pointer">หน้าหลัก</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul v-if="!$store.state.isAuthenticated" class="navbar-nav ml-auto topnav text-white">
                    <li @click="goDonatePageObject" class="nav-item cursor-pointer hover:bg-darkgreen">
                        <a class="nav-link text-white">บริจาคสิ่งของ</a>
                    </li>
                    <li @click="goDonatePageMoney" class="nav-item cursor-pointer hover:bg-darkgreen">
                        <a class="nav-link text-white">บริจาคเงิน</a>
                    </li>
                </ul>
                <ul v-else class="navbar-nav ml-auto topnav text-white">
                    <li @click="goDonateDashBoard" class="nav-item cursor-pointer hover:bg-darkgreen">
                        <a class="nav-link text-white">{{this.$store.state.authUser.hospital.name}}</a>
                    </li>
                    <li @click="goDonateCratePost" class="nav-item cursor-pointer hover:bg-darkgreen">
                        <a class="nav-link text-white">เปิดรับบริจาคสิ่งของ</a>
                    </li>
                    <li class="nav-item cursor-pointer">
                        <button @click="logout" type="button" class="btn bg-red text-white">Logout</button>
                    </li>
                </ul>
            </div>
        </nav>
        <div style="height: 56px"></div>
    </div>

</template>

<script>
    export default {
        name: 'NavBar',
        data() {
            return {
                menuToggle: false
            }
        },
        methods: {
            goHome() {
                this.$router.push({
                    name: "Home"
                })
            },
            goDonatePageObject() {
                this.$router.push({
                    name: "DonatePageObject"
                })
            },
            goDonatePageMoney() {
                this.$router.push({
                    name: "DonatePageMoney"
                })
            },
            goDonateDashBoard(){
                this.$router.push({
                    name: "DashboardHospital",
                    params:{id:this.$store.state.authUser.hospital.id}
                })
            },
            goDonateCratePost(){
                this.$router.push({
                    name: "PostCreate"
                })
            },
            logout() {
                this.$store.commit('removeToken');
                this.$router.push('/');
                location.reload()
            }
        }
    }
</script>

<style>

</style>