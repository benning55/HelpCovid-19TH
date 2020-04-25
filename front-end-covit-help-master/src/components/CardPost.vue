<template>
    <div class="card shadow-lg h-full" style="margin-bottom: 15px;border-radius: 10px;border: 0">
        <!--        {{data.base_amount}} | {{data.amount}}-->

        <img v-if="data.picture != null" class=" h-40 mx-auto object-contain card-img"
             :src="$store.state.host+data.picture" :alt="data.title">
        <img v-else class=" h-40 mx-auto object-cover card-img"
             src="../assets/undefine.jpg" :alt="data.title">
        <div class="card-body content-between" style="padding-bottom: 0">
            <div class="w-full">
                <h5 class="card-title font-bold">{{data.title}}</h5>
            </div>
        </div>
        <div class="card-footer bg-white" style="border-radius: 10px;border: 0px;padding: 0px 10px 10px 10px">
            <p class="text-gray text-sm my-2"><i class="fas fa-hospital"></i> {{data.hospital.name}}</p>
            <p v-if="leftItem() > 0">ขาดอีก <span class="text-red">{{leftItem()}}</span> หน่วย</p>
            <p v-else class="text-green">ครบแล้ว</p>
            <button @click="goPost(data.id)" class="btn bg-green text-white w-full mt-2 hover:bg-hover_blue">ดูรายละเอียดเพิ่ม</button>
        </div>
    </div>
</template>

<script>
    export default {
        props: ["data"],
        data() {
            return {}
        },
        methods: {
            goPost(id) {
                this.$router.push({
                    name: "DashboardPost",
                    params: {id: id}
                })
            },
            leftItem() {
                return Math.floor(this.data.amount)
            }
        }
    }
</script>

<style scoped>
    .card-img {
        border-radius: 10px 10px 0 0 !important;
    }
</style>