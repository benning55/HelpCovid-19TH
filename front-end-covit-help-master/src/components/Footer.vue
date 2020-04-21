<template>
    <footer id="sticky-footer" class="py-4 bg-light_green text-white-50">
        <div class="px-4 flex-none lg:flex lg:justify-between">
            <div class="mb-4 lg:mb-0">
                <div class="flex">
                    <img src="https://www.dct.or.th/images/sustain3/icon/logo.png"
                         alt="DCT สภาดิจิทัลเพื่อเศรษฐกิจและสังคมแห่งประเทศไทย"
                         class="h-16">
                    <el-tooltip content="มูลนิธิโรงพยาบาลพระมงกุฎเกล้า" placement="top">
                        <img src="../assets/logoPMK.jpg" alt="มูลนิธิโรงพยาบาลพระมงกุฎเกล้า"
                             class="h-16 rounded-lg ml-3">
                    </el-tooltip>

                    <el-tooltip content="สภากาชาดไทย" placement="top">
                        <img src="https://www.egov.go.th/upload/eservice-thumbnail/img_0bdc3e3694c16d8b06ce1f7636024ec7.png"
                             alt="สภากาชาดไทย"
                             class="h-16 rounded-lg ml-3">
                    </el-tooltip>
                </div>
                <h1 class="py-2 text-lg font-medium">สภาดิจิทัลเพื่อเศรษฐกิจและสังคมแห่งประเทศไทย</h1>
                <p class="w-full lg:w-1/3">ชั้น 31 อาคาร เอไอเอ แคปปิตอล เซ็นเตอร์ ถ.รัชดาภิเษก แขวงดินแดง เขตดินแดง
                    กรุงเทพฯ
                    10400</p>
                <p class="mt-2"><i class="fas fa-phone-alt"></i> 02-858-1209</p>
                <p><i class="fas fa-envelope"></i> contact@dct.or.th</p>
            </div>

            <div>
                <img class="h-12 my-3" src="../assets/logo.png">
                <router-link to="/all-post">
                    <h1 class="py-1 text-left lg:text-right cursor-pointer hover:text-green">บริจาคสิ่งของ</h1>
                </router-link>

                <router-link to="/all-hospital">
                    <h1 class="py-1 text-left lg:text-right cursor-pointer hover:text-green">บริจาคเงิน</h1>
                </router-link>

                <router-link to="/all-supplier">
                    <h1 class="py-1 text-left lg:text-right cursor-pointer hover:text-green">ผู้ผลิตสิ่งของบริจาค</h1>
                </router-link>

                <router-link to="/about">
                    <h1 class="py-1 text-left lg:text-right cursor-pointer hover:text-green">เกี่ยวกับเรา</h1>
                </router-link>

                <router-link to="/login">
                    <h1 class="py-1 text-left lg:text-right cursor-pointer hover:text-green">ลงทะเบียน
                        <router-link to="/all-hospital"></router-link>
                        (สำหรับสถานพยาบาล)
                    </h1>
                </router-link>

                <div class="text-left lg:text-right pt-4">
                    <small>Copyright &copy; helpital.org</small>
                </div>
            </div>
        </div>


    </footer>
</template>

<script>
    export default {
        
    }
</script>