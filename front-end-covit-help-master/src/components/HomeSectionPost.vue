<template>
    <div>

        <h1 class="text-2xl mt-5 mb-3">รับบริจาคสิ่งของ</h1>


        <div class="row">
            <div v-for="post in dataNeed" :key="post.id" class=" col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardPost :data="post"/>
            </div>
            <div v-if="showSeeMore" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 hover:no-underline">
                <router-link to="/all-post">
                    <div class="shadow-lg  h-full text-center" style="margin-bottom: 15px;border-radius: 10px">
                        <div class="card-title font-bold text-key_column opacity-50 h-full" style="">
                            <div class="relative w-full" style="top: 50%;transform: translateY(-50%);">
                                <i class="fas fa-plus mb-4" style="font-size: 5rem"></i>
                                <h1 class="hover:no-underline">ดูเพิ่มเติม</h1>
                            </div>
                        </div>
                    </div>
                </router-link>
            </div>
        </div>
        <LoaderFull v-if="loading" />
    </div>
</template>

<script>
    import axios from 'axios'
    import CardPost from "../components/CardPost";
    import LoaderFull from "./LoaderFull";

    export default {
        components: {
            CardPost,
            LoaderFull
        },
        data() {
            return {
                dataNeed: [],
                showSeeMore:false,
                loading:false
            }
        },
        created() {
            this.loading = true
            if (this.$store.state.dataAllPost.length == 0) {
                this.dataNeed = []
            } else if (this.$store.state.dataAllPost.length > 12) {
                this.dataNeed = this.$store.state.dataAllPost.slice(0, 11)
                this.showSeeMore = true
            } else {
                this.dataNeed = this.$store.state.dataAllPost.slice(0, 12)
                this.showSeeMore = false
            }
            this.loadData()
        },
        methods: {
            loadData() {
                axios.get(`${this.$store.state.host}/api/posts/need/`)
                    .then(res => {
                        this.$store.commit("setDataAllPost", res.data.data);
                        if (this.$store.state.dataAllPost.length == 0) {
                        } else if (this.$store.state.dataAllPost.length > 12) {
                            this.dataNeed = this.$store.state.dataAllPost.slice(0, 11)
                            this.showSeeMore = true
                        } else {
                            this.dataNeed = this.$store.state.dataAllPost.slice(0, 12)
                            this.showSeeMore = false
                        }
                        this.loading = false
                    })
                    .catch(e => {
                        this.loading = false
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration: 10
                        });
                    })
            }
        }
    }
</script>