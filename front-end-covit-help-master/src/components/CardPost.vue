<template>
    <div class="card" style="margin-bottom: 15px">
        <img class="card-img-top w-32 h-32 mx-auto" src="../assets/logo.png" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">Card title</h5>
            <p class="">ขาดอีก <span class="text-red">123</span> หน่วย</p>
            <a @click="goPost" class="btn bg-green text-white w-full mt-3">ดูรายละเอียดเพิ่ม</a>
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
            goPost(){
                this.$router.push({
                    name:"DashboardPost"
                })
            }
        }
    }
</script>