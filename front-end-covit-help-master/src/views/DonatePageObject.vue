<template>
    <div class="container">
        <h1 class="text-2xl mt-5 mb-3">รับบริจาคสิ่งของ</h1>
        <div class="row">
            <div v-for="post in dataNeed" :key="post.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardPost :data="post"/>
            </div>
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
        data() {
            return {
                dataNeed: []
            }
        },
        created() {
            this.dataNeed = this.$store.state.dataAllPost
            this.loadData()
        },
        methods: {
            loadData() {
                axios.get(`${this.$store.state.host}/api/posts/need/`)
                    .then(res => {
                        this.dataNeed = res.data.data
                        this.$store.commit("setDataAllPost", res.data.data);
                    })
                    .catch(e => {
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