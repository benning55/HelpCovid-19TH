<template>
    <div>
        <div class="container">
            <div class="rounded mt-4">
                <div class="card-body text-center">
                    <img v-if="dataPost.picture != null" :src="$store.state.host+dataPost.picture"
                         class="mx-auto w-40 h-40 object-contain border-image shadow-lg" alt="Card image cap">
                    <img v-else src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg"
                         class="mx-auto w-40 h-40 object-contain border-image shadow-lg" alt="Card image cap">
                    <p class=" text-2xl">{{dataPost.title}}</p>
                    <h1 class="my-4">ขณะนี้มีผู้บริจาคไปแล้ว</h1>
                    <h1 class="text-5xl"> {{Math.floor(dataPost.total_donation)}} <a
                            class="text-sm">หน่วย</a></h1>
                    <div class="progress my-2 w-11/12 sm:w-7/12 mx-auto">
                        <div class="progress-bar bg-green" :style="{width: percent()+'%'}" role="progressbar"
                             aria-valuenow="75"
                             aria-valuemin="0"
                             aria-valuemax="100"></div>
                    </div>
                    <h1 class="my-4">จากความต้องการ {{Math.floor(dataPost.base_amount)}} หน่วย</h1>
                    <div class="col-12 col-md-10 col-lg-8 mx-auto text-left mb-4">
                        <h1 class=" mb-2 text-md">รายละเอียด</h1>
                        <p>{{dataPost.description}}</p>
                    </div>

                    <button v-if="$store.state.authUser.email != dataPost.user.email"
                            @click="goDonateObject(dataPost.id)"
                            type="button" class="btn bg-green text-white hover:bg-hover_blue">
                        ส่งความประสงค์ในการบริจาค
                    </button>
                    <button v-else @click="goEdit(dataPost.id)" type="button"
                            class="btn bg-green text-white hover:bg-hover_blue">
                        แก้ไขการรับบริจาค
                    </button>
                </div>
                <div class="row">
                    <div class="col-sm-6">
                        <div class=" h-full">
                            <div class="card-body flex md:justify-end justify-start">
                                <img v-if="dataPost.hospital.picture != null"
                                     :src="$store.state.host+dataPost.hospital.picture"
                                     class="w-24 h-24 object-contain mr-3 border-image shadow-lg"
                                     :alt="dataPost.hospital.name">
                                <img v-else src="http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg"
                                     class="w-24 h-24 object-contain mr-3 border-image shadow-lg"
                                     :alt="dataPost.hospital.name">
                                <div>
                                    <p class="card-title font-bold">{{dataPost.hospital.name}}</p>
                                    <p class="card-title"><i class="fas fa-map-marker-alt mr-2"></i>{{dataPost.hospital.address}}
                                    </p>
                                    <p class="card-title"><i class="fas fa-phone-alt mr-2"></i>{{dataPost.hospital.tel}}
                                    </p>
                                    <a @click="goDashboardHospital(dataPost.hospital.id)"
                                       class="btn bg-green text-white">ดูข้อมูลเพิ่มเติม</a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class=" h-full">
                            <div class="card-body">
                                <small class="text-gray">ช่องทางการติดต่อ</small>
                                <h5 class="card-title mt-3"><i class="fas fa-user mr-2"></i>{{dataPost.user.first_name}}
                                    {{dataPost.user.last_name}}</h5>
                                <h5 class="card-title"><i class="fas fa-envelope mr-2"></i>{{dataPost.user.email}}</h5>
                                <h5 class="card-title"><i class="fas fa-phone-alt mr-2"></i>{{dataPost.user.tel}}</h5>
                            </div>
                        </div>
                    </div>
                </div>

                <div v-if="$store.state.authUser.email != dataPost.user.email"
                     class="col-12 col-md-10 col-lg-8 mx-auto">
                    <h1 class=" mb-2 text-xl">ผู้ร่วมบริจาค</h1>
                    <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                    <table v-else class="table">
                        <thead>
                        <tr>
                            <th scope="col">ชื่อ/บริษัท</th>
                            <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                            <th scope="col" style="width: 150px">สถานะ</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="user in donateUser" :key="user.id">
                            <td v-if="user.company_name == ''||user.company_name == null">
                                <i class="fas fa-user-alt"></i> {{user.first_name}} {{user.last_name}}
                            </td>
                            <td v-else><i class="fas fa-building"></i> {{user.company_name}}</td>
                            <td>{{numberWithCommas(Math.floor(user.amount))}}</td>
                            <td v-if="user.approve_status"><h1 class="text-green">ดำเนินการสำเร็จ</h1></td>
                            <td v-else><h1 class="text-orange">กำลังดำเนินการ</h1></td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <AdminCheckObject v-else :id="$route.params.id"/>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import axios from "axios"
    import AdminCheckObject from "../components/AdminCheckObject";
    import Footer from "../components/Footer";

    export default {
        components: {
            AdminCheckObject,
            Footer
        },
        data() {
            return {
                dataPost: {},
                donateUser: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/posts/need/${this.$route.params.id}/`)
                .then(res => {
                    this.dataPost = res.data.data[0]
                    axios.get(`${this.$store.state.host}/api/posts/donate/${this.$route.params.id}/`)
                        .then(res => {
                            this.donateUser = res.data.data
                        })
                        .catch(e => {
                            this.$message({
                                showClose: true,
                                message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลการบริจาค' + ' Error : ' + e.response.status,
                                type: 'error',
                                duration: 10
                            });
                        })
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