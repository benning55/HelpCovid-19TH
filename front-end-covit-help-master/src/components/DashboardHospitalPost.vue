<template>
    <div>
        <div v-if="dataPost.length == 0" class="text-center my-5 text-gray">ยังไม่เปิดรับบริจาคสิ่งของ</div>
        <div v-else class="row">
            <div v-for="post in dataPost" :key="post.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-3">
                <CardPost :data="post"/>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import CardPost from "./CardPost";

    export default {
        props: ["id"],
        components: {
            CardPost
        },
        data() {
            return {
                dataPost: []
            }
        },
        created() {
            axios.post(`${this.$store.state.host}/api/posts/need/`, {
                hospital_id: this.id
            })
                .then(res => {
                    this.dataPost = res.data.data
                })
                .catch(e => {
                    console.log(e.response)
                })
        }
    }
</script>