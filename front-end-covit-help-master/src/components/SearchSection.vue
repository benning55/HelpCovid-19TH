<template>
    <div class="form-group text-center">
        <input v-model="title" class="form-control"
               type="text" placeholder="พิมพ์เพื่อค้นหาสิ่งของที่ โรงพยาบาลเปิดรับบริจาค เช่น PPE, N95">
        <button @click="search" type="button" class="btn bg-green text-white my-3 hover:bg-hover_blue"><i class="fas fa-search mr-2" style="transform: scaleX(-1)"></i> ค้นหา</button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                title: ''
            }
        },
        methods:{
            search(){
                this.$router.push({
                    name:'SearchPage',
                    params:{title:this.title}
                })
            }
        }
    }
</script>