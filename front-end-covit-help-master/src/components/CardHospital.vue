<template>
    <div class="shadow-lg h-full card" style="margin-bottom: 15px;border-radius: 10px;border: 0">
        <img v-if="data.picture != null" class="card-img h-40 mx-auto object-cover" style="border-radius: 10px"
             :src="$store.state.host+ data.picture" :alt="data.name">
        <img v-else class="card-img h-40 mx-auto object-cover"
             style="border-radius: 10px"
             src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg" :alt="data.name">
        <div class="card-body" style="padding-bottom: 0">
            <h5 class="card-title text-md font-bold">{{data.name}}</h5>
            <p class="text-sm text-gray"><i class="fas fa-map-marker-alt mr-2 "></i>{{data.address}}</p>
        </div>
        <div class="card-footer bg-white" style="border-radius: 10px;border: 0px;padding: 0px 10px 10px 10px">
            <button @click="goHospital(data.id)" class="btn bg-green text-white w-full">ดูรายละเอียดเพิ่ม</button>
        </div>
    </div>
</template>

<script>
    export default {
        props:[
            "data"
        ],
        data(){
            return{

            }
        },
        methods:{
            goHospital(id){
                this.$router.push({
                    name:"DashboardHospital",
                    params:{id:id}
                })
            }
        }
    }
</script>

<style scoped>
    .card-img{
        border-radius: 10px 10px 0 0 !important;
    }
</style>