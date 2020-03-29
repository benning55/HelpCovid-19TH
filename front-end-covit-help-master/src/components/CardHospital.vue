<template>
    <div class="card" style="margin-bottom: 15px">
        <img class="card-img-top w-32 h-32 mx-auto" src="../assets/logo.png" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title text-md">Hospital title</h5>
            <p class="text-sm text-gray"><i class="fas fa-map-marker-alt mr-2 "></i>rgerg drgergerg ergferger ergerg 10212</p>
            <a @click="goHospital" class="btn bg-green text-white mt-3">ดูรายละเอียดเพิ่ม</a>
        </div>
    </div>
</template>

<script>
    export default {
        data(){
            return{

            }
        },
        methods:{
            goHospital(){
                this.$router.push({
                    name:"DashboardHospital"
                })
            }
        }
    }
</script>