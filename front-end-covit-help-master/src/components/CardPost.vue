<template>
    <div class="shadow-lg  h-full" style="margin-bottom: 15px;border-radius: 10px">
        {{data.base_amount}} | {{data.amount}}
        <img v-if="data.picture != null" class=" h-40 mx-auto object-cover card-img"
             :src="$store.state.host+data.picture" :alt="data.title">
        <img v-else class=" h-40 mx-auto object-cover card-img"
             src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg" :alt="data.title">
        <div class="card-body content-between ">
            <div class="w-full">
                <h5 class="card-title">{{data.title}}</h5>
                <p v-if="leftItem() > 0">ขาดอีก <span class="text-red">{{leftItem()}}</span> หน่วย</p>
                <p v-else class="text-green">ครบแล้ว</p>
            </div>
            <button @click="goPost(data.id)" class="btn bg-green text-white w-full mt-3">ดูรายละเอียดเพิ่ม</button>
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