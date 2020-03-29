<template>
    <div class="container">
        <h1 class="text-2xl">บริจาคสิ่งของ</h1>
        <div class="row">
            <div v-for="post in dataNeed" :key="post.id" class="col-12 col-sm-6 col-md-4 col-lg-3">
                <CardPost :data="post" />
            </div>
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardPost/>-->
<!--            </div>-->
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardPost/>-->
<!--            </div>-->
<!--            <div class="col-12 col-sm-6 col-md-4 col-lg-3">-->
<!--                <CardPost/>-->
<!--            </div>-->
        </div>
    </div>
</template>

<script>
    import CardPost from "../components/CardPost";
    import axios from 'axios'

    export default {
        components: {
            CardPost
        },
        data(){
            return{
                dataNeed:[]
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/posts/need/`)
            .then(res=>{
                this.dataNeed = res.data.data
            })
            .catch()
        }
    }
</script>