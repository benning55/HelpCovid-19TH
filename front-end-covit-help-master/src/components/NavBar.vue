<template>
    <div>
        <nav class="navbar navbar-light navbar-expand-lg text-black bg-white fixed w-full z-50 shadow-lg">
            <a @click="goHome" class="navbar-brand cursor-pointer">
                <img src="../assets/logo.png" class="h-10" alt="Helpital">
            </a>
            <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent"
                    aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
            </button>

            <div class="collapse navbar-collapse text-black" id="navbarSupportedContent">
                <ul v-if="!$store.state.isAuthenticated" class="navbar-nav ml-auto topnav text-black">
                    <li @click="goDonatePageObject" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">บริจาคสิ่งของ</a>
                    </li>
                    <li @click="goDonatePageMoney" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">บริจาคเงิน</a>
                    </li>
                    <li @click="goDanateSupplier" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">ผู้ผลิตสิ่งของ</a>
                    </li>
                    <li @click="goAbout" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">เกี่ยวกับเรา</a>
                    </li>
                </ul>
                <ul v-else class="navbar-nav ml-auto topnav text-black">
                    <li @click="goDonateDashBoard" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">{{this.$store.state.authUser.hospital.name}}</a>
                    </li>
                    <li @click="goDonateCratePost" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">เปิดรับบริจาคสิ่งของ</a>
                    </li>
                    <li @click="goDanateSupplier" class="nav-item rounded-lg cursor-pointer hover:bg-lightGray">
                        <a class="nav-link">ผู้ผลิตสิ่งของ</a>
                    </li>
                    <li class="nav-item cursor-pointer">
                        <button @click="openModal" type="button"
                                class="btn bg-red hover:bg-hover_red text-white ml-2">
                            ออกจากระบบ
                        </button>
                    </li>
                </ul>
            </div>
        </nav>
        <div style="height: 56px"></div>
        <el-dialog title="ยืนยัน" :visible.sync="confirmDialog" @closed="closeModal">
            <section>
                <div class="flex flex-wrap content-between">
                    <p class="mb-12">คุณต้องการออกจากระบบหรือไม่</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="confirmDialog = false">ยกเลิก</el-button>
                        <el-button @click="logout" type="danger">ออกจากระบบ</el-button>
                    </span>
                </div>

                <!--                <Loader v-if="isLoading"/>-->
            </section>
        </el-dialog>
    </div>

</template>

<script>
    export default {
        name: 'NavBar',
        data() {
            return {
                menuToggle: false,
                confirmDialog: false
            }
        },
        methods: {
            openModal() {
                this.confirmDialog = true
                $(".el-dialog").css({"max-width": "350px"});
            },
            closeModal() {
                this.confirmDialog = false
            },
            goAbout() {
                this.$router.push({
                    name: "About"
                })
            },
            goHome() {
                this.$router.push({
                    name: "Home"
                })
            },
            goDonatePageObject() {
                if ($(window).width() < 992) {
                    $('#navbarSupportedContent').collapse('toggle');
                }
                this.$router.push({
                    name: "DonatePageObject"
                })
            },
            goDonatePageMoney() {
                if ($(window).width() < 992) {
                    $('#navbarSupportedContent').collapse('toggle');
                }
                this.$router.push({
                    name: "DonatePageMoney"
                })
            },
            goDanateSupplier(){
                if ($(window).width() < 992) {
                    $('#navbarSupportedContent').collapse('toggle');
                }
                this.$router.push({
                    name: "DonatePageSupplier"
                })
            },
            goDonateDashBoard() {
                if ($(window).width() < 992) {
                    $('#navbarSupportedContent').collapse('toggle');
                }
                this.$router.push({
                    name: "DashboardHospital",
                    params: {id: this.$store.state.authUser.hospital.id}
                })
            },
            goDonateCratePost() {
                if ($(window).width() < 992) {
                    $('#navbarSupportedContent').collapse('toggle');
                }
                this.$router.push({
                    name: "PostCreate"
                })
            },
            logout() {
                this.$store.commit('removeToken');
                this.$router.push('/');
                location.reload()
            }
        },
        mounted() {
            /** CLOSE MAIN NAVIGATION WHEN CLICKING OUTSIDE THE MAIN NAVIGATION AREA**/
            $(document).on('click', function (e) {
                /* bootstrap collapse js adds "in" class to your collapsible element*/
                var menu_opened = $('#navbarSupportedContent').hasClass('show');

                if (!$(e.target).closest('#navbarSupportedContent').length && !$(e.target).is('#navbarSupportedContent') && menu_opened === true) {
                    $('#navbarSupportedContent').collapse('toggle');
                }

            });
        }
    }
</script>

<style>

</style>