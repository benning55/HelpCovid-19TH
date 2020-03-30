<template>
    <div class="shadow-lg h-full" style="margin-bottom: 15px;border-radius: 10px">
        <img v-if="data.picture != null" class="card-img h-40 mx-auto object-cover" style="border-radius: 10px"
             :src="$store.state.host+ data.picture" :alt="data.name">
        <img v-else class="card-img h-40 mx-auto object-cover"
             style="border-radius: 10px"
             src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg" :alt="data.name">
        <div class="card-body">
            <h5 class="card-title text-md font-bold">{{data.name}}</h5>
            <p class="text-sm text-gray"><i class="fas fa-map-marker-alt mr-2 "></i>{{data.address}}</p>
            <a @click="goHospital(data.id)" class="btn bg-green text-white mt-3">ดูรายละเอียดเพิ่ม</a>
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