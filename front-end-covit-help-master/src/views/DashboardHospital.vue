<template>
    <div class="container">
        <div class="container">
            <div class="rounded mt-4">

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
                                <img v-else src='http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg'
                                     class="w-24 h-24 object-contain mr-3 border-image shadow-lg"
                                     :alt="dataHospital.hospital.name">
                                <div>
                                    <p class="card-title font-bold">{{dataHospital.hospital.name}}</p>
                                    <p><i class="fas fa-map-marker-alt mr-2"></i>{{dataHospital.hospital.address}}</p>
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
                                <h5 class="card-title"><i class="fas fa-envelope mr-2"></i>{{dataHospital.email}}</h5>
                                <h5 class="card-title"><i class="fas fa-phone-alt mr-2"></i>{{dataHospital.hospital.tel}}
                                </h5>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="card-body text-center">
                    <!--                <img src="../assets/logo.png" class="mx-auto w-40 h-40 object-contain" alt="Card image cap">-->
                    <!--                <p class=" text-2xl">Title xxxxxxxxxxxxxxxxxxxx</p>-->
                    <h1 class="my-4">ขณะนี้มีผู้บริจาคผ่านระบบไปแล้ว</h1>
                    <h1 class="text-5xl my-5"> {{dataHospital.hospital.donated_money}} <a class="text-sm">บาท</a></h1>

                    <h1 class="">บริจาคได้ที่</h1>
                    <div class="card p-3 bg-white col-12 col-sm-9 col-md-7 col-lg-5 mx-auto shadow-lg my-4"
                         style="border: 0">
                        <h1 class="my-2 text-key_column">เลขบัญชี : <span class="text-2xl text-black">{{dataHospital.hospital.bank_account_number}}</span>
                        </h1>
                        <h1 class="my-2 text-key_column">ชื่อบัญชี :
                            <span class="text-black">{{dataHospital.hospital.bank_account_name}}</span></h1>
                        <h1 class="my-2 text-key_column">ธนาคาร : <span class="text-black">{{dataHospital.hospital.bank_name}}</span>
                        </h1>

                    </div>

                    <a href="#point" v-if="$store.state.authUser.id == dataHospital.id">
                        <button type="button"
                                class="btn bg-green text-white">
                            ดูรายการบริจาค
                        </button>
                    </a>

                    <button v-else @click="goDonateMoney(dataHospital.hospital.id)" type="button"
                            class="btn bg-green text-white">
                        บริจาคเงิน
                    </button>
                </div>

                <h1 class="ml-3 mt-5 mb-4 text-lg col-12 col-md-10 col-lg-8 mx-auto">
                    สิ่งของที่ {{dataHospital.hospital.name}} ต้องการรับบริจาค</h1>
                <DashboardHospitalPost :id="$route.params.id"/>

                <a id="point"></a>

                <div v-if="$store.state.authUser.id != dataHospital.id" class="col-12 col-md-10 col-lg-8 mx-auto">
                    <h1 class=" my-3 text-xl">ผู้ร่วมบริจาคเงิน</h1>
                    <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                    <table v-else class="table">
                        <thead>
                        <tr>
                            <th scope="col">ชื่อ</th>
                            <th scope="col">นามสกุล</th>
                            <th scope="col" style="width: 110px">จำนวน(บาท)</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr v-for="user in donateUser" :key="user.id">
                            <td>{{user.first_name}}</td>
                            <td>{{user.last_name}}</td>
                            <td>{{user.amount}}</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
                <AdminCheckMoney v-else @refresh="refresh"/>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import DashboardHospitalPost from "../components/DashboardHospitalPost";
    import AdminCheckMoney from "../components/AdminCheckMoney";

    export default {
        components: {
            DashboardHospitalPost,
            AdminCheckMoney
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
            getData() {
                axios.get(`${this.$store.state.host}/api/accounts/hospital/${this.$route.params.id}/`)
                    .then(res => {
                        this.dataHospital = res.data.data[0]
                        axios.get(`${this.$store.state.host}/api/posts/money-donate/${this.dataHospital.hospital.id}/`)
                            .then(res => {
                                this.donateUser = res.data.data
                            })
                            .catch(e => {
                                console.log(e)
                            })
                    })
                    .catch()
            },
            goDonateMoney(id) {
                this.$router.push({
                    name: "DonateMoney",
                    params: {id: id}
                })
            },
            goViewDonateMoney() {
                this.$router.push({
                    name: "DonateMoney"
                })
            },
            refresh() {
                this.getData()
            }
        }
    }
</script>