<template>
    <div>
        <div class="container">
            <div class="container">
                <div class="rounded mt-4">

                    <div v-if="$store.state.authUser.id == dataHospital.id">
                        <div class="bg-light_green border-l-4 border-green text-black p-4" role="alert">
                            <p>หากต้องการแก้ไขข้อมูล กรุณาติดต่อผู้ดูแลระบบ โดยส่งเมลล์มาที่ admin@covid19th.org</p>
                        </div>
                    </div>

                    <div class="row">
                        <!--                    {{$store.state.authUser}}-->
                        <hr>
                        <!--                    {{dataHospital.id}}-->
                        <div class="col-sm-6">
                            <div class=" h-full">
                                <div class="card-body flex md:justify-end justify-start">
                                    <img v-if="dataHospital.hospital.picture != null"
                                         :src='$store.state.host+dataHospital.hospital.picture'
                                         class="w-24 h-24 object-contain mr-3 border-image shadow-lg"
                                         :alt="dataHospital.hospital.name">
                                    <img v-else src='../assets/undefine.jpg'
                                         class="w-24 h-24 object-contain mr-3 border-image shadow-lg"
                                         :alt="dataHospital.hospital.name">
                                    <div>
                                        <p class="card-title font-bold">{{dataHospital.hospital.name}}</p>
                                        <p><i class="fas fa-map-marker-alt mr-2"></i>{{dataHospital.hospital.address}}
                                        </p>
                                        <p><i class="fas fa-phone-alt mr-2"></i>{{dataHospital.hospital.tel}}</p>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-sm-6">
                            <div class=" h-full">
                                <div class="card-body">
                                    <small class="text-gray">ช่องทางการติดต่อ</small>
                                    <h5 class="card-title mt-3"><i class="fas fa-user mr-2"></i>{{dataHospital.first_name}}
                                        {{dataHospital.last_name}}</h5>
                                    <h5 class="card-title"><i class="fas fa-envelope mr-2"></i>{{dataHospital.email}}
                                    </h5>
                                    <h5 class="card-title"><i class="fas fa-phone-alt mr-2"></i>{{dataHospital.hospital.tel}}
                                    </h5>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="card-body text-center">
                        <h1 class="my-4">ขณะนี้มีผู้บริจาคผ่านระบบไปแล้ว</h1>
                        <h1 class="text-5xl my-5"> {{numberWithCommas(dataHospital.hospital.donated_money)}} <a
                                class="text-sm">บาท *</a></h1>
                        <h1 class="">บริจาคได้ที่</h1>

                        <div v-if="dataHospital.hospital.bank_account_number == '-'"
                             class="card p-3 bg-white col-12 col-sm-9 col-md-7 col-lg-5 mx-auto shadow-lg my-4"
                             style="border: 0">
                            <h1 class="my-2 text-key_column"><span class="text-black">ยังไม่ขอรับบริจาคเงิน</span></h1>
                        </div>

                        <div v-else class="card p-3 bg-white col-12 col-sm-9 col-md-7 col-lg-5 mx-auto shadow-lg my-4"
                             style="border: 0">
                            <h1 class="my-2 text-key_column">เลขบัญชี : <span class="text-2xl text-black">{{dataHospital.hospital.bank_account_number}}</span>
                            </h1>
                            <h1 class="my-2 text-key_column">ชื่อบัญชี :
                                <span class="text-black">{{dataHospital.hospital.bank_account_name}}</span></h1>
                            <h1 class="my-2 text-key_column">ธนาคาร : <span class="text-black">{{dataHospital.hospital.bank_name}}</span>
                            </h1>
                        </div>

                        <div v-if="dataHospital.hospital.bank_account_number != '-'">
                            <a href="#point" v-if="$store.state.authUser.id == dataHospital.id">
                                <button type="button"
                                        class="btn bg-green text-white hover:bg-hover_blue">
                                    ดูรายการบริจาค
                                </button>
                            </a>

                            <button v-else @click="goDonateMoney(dataHospital.hospital.id)" type="button"
                                    class="btn bg-green text-white">
                                บริจาคเงิน
                            </button>
                        </div>

                        <p class="text-red mt-5" style="font-size: 10px">*ยอดบริจาคที่ปรากฎจะนับจากการบริจาคที่แจ้งผ่าน
                            Website เท่านั้น ซึ่งอาจจะไม่ตรงกับจำนวนเงินบริจาคที่อยู่ในบัญชีของสถาพยาบาล</p>

                    </div>

                    <h1 class="ml-3 mt-5 mb-4 text-lg col-12 col-md-10 col-lg-8 mx-auto">
                        สิ่งของที่ {{dataHospital.hospital.name}} ต้องการรับบริจาค</h1>
                    <DashboardHospitalPost :id="$route.params.id"/>

                    <a id="point"></a>

                    <div v-if="$store.state.authUser.id != dataHospital.id" class="col-12 col-md-10 col-lg-8 mx-auto">
                        <h1 class=" my-3 text-xl">ผู้ร่วมบริจาคเงิน
                            <el-tooltip slot="i" class="item" effect="dark"
                                        content="ชื่อของผู้บริจาคจะแสดงก็ต่อเมื่อได้รับการยืนยันจากเจ้าหน้าที่ของสถานพยาบาลแล้ว"
                                        placement="right">
                                <i class="fas fa-info-circle"></i>
                            </el-tooltip>
                        </h1>
                        <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                        <table v-else class="table">
                            <thead>
                            <tr>
                                <th scope="col">ชื่อ/บริษัท</th>
                                <th scope="col" style="width: 110px">จำนวน(บาท)</th>
                            </tr>
                            </thead>
                            <tbody>

                            <!--people case-->
                            <tr v-for="user in donateUser" :key="user.id">
                                <td v-if="user.company_name == ''||user.company_name == null"><i
                                        class="fas fa-user-alt"></i> {{user.first_name}}
                                    {{user.last_name}}
                                </td>
                                <td v-else><i class="fas fa-building"></i> {{user.company_name}}</td>
                                <td>{{numberWithCommas(user.amount)}}</td>
                            </tr>
                            </tbody>
                        </table>
                    </div>
                    <AdminCheckMoney v-else @refresh="refresh"/>
                </div>
            </div>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import axios from 'axios'
    import DashboardHospitalPost from "../components/DashboardHospitalPost";
    import AdminCheckMoney from "../components/AdminCheckMoney";
    import Footer from "../components/Footer";

    export default {
        components: {
            DashboardHospitalPost,
            AdminCheckMoney,
            Footer
        },
        data() {
            return {
                dataHospital: {},
                donateUser: [
                    {
                        first_name: 'x',
                        last_name: 'y',
                        amount: 15
                    }, {
                        first_name: 'x',
                        last_name: 'y',
                        amount: 15
                    }]
            }
        },
        created() {
            this.getData()
        },
        methods: {
            numberWithCommas(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            getData() {
                axios.get(`${this.$store.state.host}/api/accounts/hospital/${this.$route.params.id}/`)
                    .then(res => {
                        this.dataHospital = res.data.data[0]
                        axios.get(`${this.$store.state.host}/api/posts/money-donate/${this.dataHospital.hospital.id}/`)
                            .then(res => {
                                this.donateUser = res.data.data
                            })
                            .catch(e => {
                                this.$message({
                                    showClose: true,
                                    message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลโรงพยาบาล' + ' Error : ' + e.response.status,
                                    type: 'error',
                                    duration: 10
                                });
                            })
                    })
                    .catch()
            }
            ,
            goDonateMoney(id) {
                this.$router.push({
                    name: "DonateMoney",
                    params: {id: id}
                })
            }
            ,
            goViewDonateMoney() {
                this.$router.push({
                    name: "DonateMoney"
                })
            }
            ,
            refresh() {
                this.getData()
            }
        }
    }
</script>