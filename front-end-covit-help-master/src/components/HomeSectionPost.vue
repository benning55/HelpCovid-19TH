<template>
    <div>

        <h1 class="text-2xl mt-5 mb-3">รับบริจาคสิ่งของ</h1>
        <div class="row">
            <div v-for="post in dataNeed" :key="post.id" class=" col-12 col-sm-6 col-md-4 col-lg-3 mb-4">
                <CardPost :data="post"/>
            </div>
            <div v-if="cardLength > 12" class="col-12 col-sm-6 col-md-4 col-lg-3 mb-4 hover:no-underline">
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
                dataNeed: [],
                cardLength: 0
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/posts/need/`)
                .then(res => {
                    this.cardLength = res.data.data.length
                    if (res.data.data.length == 12) {
                        this.dataNeed = res.data.data.slice(0, 12)
                    } else {
                        this.dataNeed = res.data.data.slice(0, 11)
                    }

                })
                .catch()
        }
    }
</script>