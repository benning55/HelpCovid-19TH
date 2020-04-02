<template>
    <div class="container">
        <div class="rounded mt-4 text-center">
            <h1 class="text-2xl mt-5 mb-3">เกี่ยวกับเว็บไซต์</h1>
            <div v-for="data in datas" :key="data.id" class="my-5">
                <p>{{data.description}}</p>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                datas: ''
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/about-me/`)
                .then(res => {
                    this.datas = res.data.data
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการโหลดข้อมูล' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        }
    }
</script>
