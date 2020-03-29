<template>
    <div>
        <h1 class="text-2xl">Post</h1>
        <div class="row">
            <div v-for="post in dataNeed" :key="post.id" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardPost :data="post" />
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import CardPost from "../components/CardPost";

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
            axios.get(`${this.$store.state.host}/api/posts/need/`)
                .then(res => {
                    this.dataNeed = res.data.data
                })
                .catch()
        }
    }
</script>