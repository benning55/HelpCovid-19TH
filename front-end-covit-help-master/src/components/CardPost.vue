<template>
    <div class="card h-full" style="margin-bottom: 15px">

        <img v-if="data.picture != null" class="card-img-top h-40 mx-auto object-cover"
             :src="$store.state.host+data.picture" alt="Card image cap">
        <img v-else class="card-img-top h-40 mx-auto object-cover"
             src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg" alt="Card image cap">
        <div class="card-body">
            <h5 class="card-title">{{data.title}}</h5>
            <p class="">ขาดอีก <span class="text-red">123</span> หน่วย</p>
            <a @click="goPost(data.id)" class="btn bg-green text-white w-full mt-3">ดูรายละเอียดเพิ่ม</a>
        </div>
    </div>
</template>

<script>
    export default {
        props:["data"],
        data(){
            return{

            }
        },
        methods:{
            goPost(id){
                this.$router.push({
                    name:"DashboardPost",
                    params:{id:id}
                })
            }
        }
    }
</script>