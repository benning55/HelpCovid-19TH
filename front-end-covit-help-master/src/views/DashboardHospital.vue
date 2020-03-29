<template>
    <div class="container">
        <div class="container">
            <div class=" shadow-lg rounded mt-4">
                <div class="row">
<!--                    {{$store.state.authUser}}-->
                    <hr>
<!--                    {{dataHospital.id}}-->
                    <div class="col-sm-6">
                        <div class=" h-full">
                            <div class="card-body flex md:justify-end justify-start">
                                <img v-if="dataHospital.hospital.picture != null" :src='$store.state.host+dataHospital.hospital.picture'
                                     class="w-24 h-24 object-contain mr-3"
                                     alt="Card image cap">
                                <img v-else src='http://ecx.images-amazon.com/images/I/41Ail0vAGbL._SX300_.jpg'
                                     class="w-24 h-24 object-contain mr-3"
                                     alt="Card image cap">
                                <div>
                                    <p class="card-title">{{dataHospital.hospital.name}}</p>
                                    <p><i class="fas fa-map-marker-alt mr-2"></i>{{dataHospital.hospital.address}}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-6">
                        <div class=" h-full">
                            <div class="card-body">
                                <small class="text-gray">ช่องทางการติดต่อ</small>
                                <h5 class="card-title"><i class="fas fa-user mr-2"></i>{{dataHospital.first_name}}
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
                    <button v-if="$store.state.authUser.id == dataHospital.id" @click="goViewDonateMoney" type="button" class="btn bg-green text-white">
                        ดูรายการบริจาค
                    </button>
                    <button v-else @click="goDonateMoney" type="button" class="btn bg-green text-white">
                        บริจาคเงิน
                    </button>
                </div>

                <h1 class="ml-3 mt-5 mb-3 text-lg col-12 col-md-10 col-lg-8 mx-auto">สิ่งของที่ {{dataHospital.hospital.name}} ต้องการรับบริจาค</h1>
                <DashboardHospitalPost :id="$route.params.id"/>


                <div class="col-12 col-md-10 col-lg-8 mx-auto">
                    <h1 class=" my-3 text-xl">ผู้ร่วมบริจาคเงิน</h1>
                    <table class="table">
                        <thead>
                        <tr>
                            <th scope="col">ชื่อ</th>
                            <th scope="col">นามสกุล</th>
                            <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                        </tr>
                        </thead>
                        <tbody>
                        <tr>
                            <td>Mark</td>
                            <td>Otto</td>
                            <td>@mdo</td>
                        </tr>
                        <tr>
                            <td>Jacob</td>
                            <td>Thornton</td>
                            <td>@fat</td>
                        </tr>
                        <tr>
                            <td>1</td>
                            <td>3</td>
                            <td>4</td>
                        </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import DashboardHospitalPost from "../components/DashboardHospitalPost";

    export default {
        components: {
            DashboardHospitalPost
        },
        data() {
            return {
                dataHospital: {}
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/accounts/hospital/${this.$route.params.id}/`)
                .then(res => {
                    this.dataHospital = res.data.data[0]
                })
                .catch()
        },
        methods: {
            goDonateMoney() {
                this.$router.push({
                    name: "DonateMoney"
                })
            },
            goViewDonateMoney(){
                this.$router.push({
                    name: "DonateMoney"
                })
            }
        }
    }
</script>