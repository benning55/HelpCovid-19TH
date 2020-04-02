<template>
    <div class="form-group text-center">
        <input v-model="title" class="form-control"
               type="text" placeholder="พิมพ์สิ่งของที่ต้องการบริจาค">
        <button @click="search" type="button" class="btn bg-green text-white my-3">ค้นหา <i class="fas fa-search"></i></button>
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