<template>
    <div>
        <div class="bg-image fixed w-full h-screen"></div>
        <div class="container" style="padding-top: 50px">

            <div class="mainbox mx-auto bg-white col-md-8 col-lg-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
                <div class="sm:px-10 md:px-16 lg:px-16 w-full text-center py-3">
                    <el-radio-group v-model="toggle_isLogin">
                        <el-radio-button label="ลงชื่อเข้าใช้"></el-radio-button>
                        <el-radio-button label="ลงทะเบียน"></el-radio-button>
                    </el-radio-group>
                </div>
            </div>
            <LoginSection v-if="toggle_isLogin == 'ลงชื่อเข้าใช้'"/>
            <RegisterSection v-else/>
        </div>
    </div>
</template>

<script>
    import LoginSection from '../components/LoginSection'
    import RegisterSection from '../components/RegisterSection'

    export default {
        components: {
            RegisterSection,
            LoginSection,
        },
        data() {
            return {
                toggle_isLogin: 'ลงชื่อเข้าใช้'
            }
        }
    }
</script>

<style scoped>
    .bg-image {
        background-image: url("https://www.risenow.com/hs-fs/hubfs/GettyImages-670810492.jpg?width=1086&name=GettyImages-670810492.jpg");
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
        opacity: .5;
    }
</style>