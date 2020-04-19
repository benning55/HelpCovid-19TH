<template>
    <div>
        <div class="container">
            <div class="rounded mt-4">
                <div class="card-body text-center">
                    <img v-if="dataSupplier.picture != null" :src="$store.state.host+dataSupplier.picture"
                         style="max-width: 500px;max-height: 300px"
                         class="mx-auto w-full object-contain border-image shadow-lg" :alt="dataSupplier.title">
                    <img v-else src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg"
                         style="max-width: 500px;max-height: 300px"
                         class="mx-auto w-full object-contain border-image shadow-lg" :alt="dataSupplier.title">
                    <p class=" text-2xl mt-3 font-bold">{{dataSupplier.title}}</p>
                    <p class=" text-xl mt-3 mb-5">{{dataSupplier.company}}</p>

                    <div class="col-12 col-md-10 col-lg-8 mx-auto text-left mb-4">
                        <h1 class=" mb-2 text-md text-center font-medium">รายละเอียด</h1>
                        <p>{{dataSupplier.description}}</p>
                    </div>

                    <div class="col-12 col-md-10 col-lg-8 mx-auto text-left mb-4">
                        <h1 class=" mb-2 text-md text-center">ช่องทางการติดต่อ</h1>
                        <ul class="list-group list-group-flush">
                            <li class="list-group-item flex justify-between">
                                <h1>เบอร์โทรศัพท์</h1>
                                <h1>{{dataSupplier.tel}}</h1>
                            </li>
                            <li class="list-group-item flex justify-between">
                                <h1>อีเมลล์</h1>
                                <h1 v-if="dataSupplier.email != null">{{dataSupplier.email}}</h1>
                                <h1 v-else>-</h1>
                            </li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import axios from "axios"
    import Footer from "../components/Footer";

    export default {
        components: {
            Footer
        },
        data() {
            return {
                dataSupplier: {},
                donateUser: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/util/maker/${this.$route.params.id}/`)
                .then(res => {
                    this.dataSupplier = res.data.data[0]
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        },
        methods: {
            numberWithCommas(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            goDonateObject() {
                this.$router.push({
                    name: "DonateObject",
                    // params:{id:id}
                })
            },
            goDashboardHospital(id) {
                this.$router.push({
                    name: "DashboardHospital",
                    params: {id: id}
                })
            },
            leftItem() {
                return Math.floor(this.dataPost.amount)
            },
            percent() {
                return Math.floor(100 - ((this.dataPost.amount / this.dataPost.base_amount) * 100))
            },
            goEdit(id) {
                this.$router.push({
                    name: 'PostEdit',
                    params: {id: id}
                })
            }
        }
    }
</script>

<style>

</style>