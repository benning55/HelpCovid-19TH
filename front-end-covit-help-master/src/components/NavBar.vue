<template>
    <div>
        <nav class="navbar text-white navbar-expand-lg text-white navbar-dark bg-green fixed w-full z-10">
            <a @click="goHome" class="navbar-brand cursor-pointer">หน้าหลัก</a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto topnav text-white">
                    <li @click="goDonatePageObject" class="nav-item cursor-pointer">
                        <a class="nav-link text-white">บริจาคสิ่งของ</a>
                    </li>
                    <li @click="goDonatePageMoney" class="nav-item cursor-pointer">
                        <a class="nav-link text-white">บริจาคเงิน</a>
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
            }
        }
    }
</script>

<style>

</style>