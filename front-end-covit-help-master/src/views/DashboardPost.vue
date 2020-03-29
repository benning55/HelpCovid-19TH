<template>
    <div class="container">

        <div class=" shadow-lg rounded mt-4">
            <div class="card-body text-center">
                <img src="../assets/logo.png" class="mx-auto w-40 h-40 object-contain" alt="Card image cap">
                <p class=" text-2xl">Title xxxxxxxxxxxxxxxxxxxx</p>
                <h1 class="my-4">ขณะนี้มีผู้บริจาคไปแล้ว</h1>
                {{$store.state.host}}
                <h1 class="text-5xl"> 122 <a class="text-sm">หน่วย</a></h1>
                <div class="progress my-2 w-11/12 sm:w-7/12 mx-auto">
                    <div class="progress-bar w-75 bg-green" role="progressbar" aria-valuenow="75"
                         aria-valuemin="0"
                         aria-valuemax="100"></div>
                </div>
                <h1 class="my-4">จากความต้องการ 200 หน่วย</h1>
                <button @click="goDonateObject" type="button" class="btn bg-green text-white">
                    ส่งความประส่งในการบริจาค
                </button>
            </div>
            <div class="row">
                <div class="col-sm-6">
                    <div class=" h-full">
                        <div class="card-body flex md:justify-end justify-start">
                            <img src="../assets/logo.png" class="w-24 h-24 object-contain mr-3" alt="Card image cap">
                            <div>
                                <p class="card-title">โรงบาล gre erfef erferf erferf</p>
                                <p><i class="fas fa-map-marker-alt mr-2"></i>rgerg drgergerg ergferger ergerg 10212</p>
                                <a @click="goDashboardHospital" class="btn bg-green text-white">ดูข้อมูลเพิ่มเติม</a>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6">
                    <div class=" h-full">
                        <div class="card-body">
                            <small class="text-gray">ช่องทางการติดต่อ</small>
                            <h5 class="card-title">ชื่อออออออ นามสกุลลลลลลลลล</h5>
                            <h5 class="card-title">maildfsf@sfes.com</h5>
                            <h5 class="card-title">0215165165</h5>
                        </div>
                    </div>
                </div>
            </div>

            <div class="col-12 col-md-10 col-lg-8 mx-auto">
                <h1 class=" mb-2 text-xl">ผู้ร่วมบริจาค</h1>
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
</template>

<script>
    export default {
        methods: {
            goDonateObject() {
                this.$router.push({
                    name: "DonateObject"
                })
            },
            goDashboardHospital(){
                this.$router.push({
                    name: "DashboardHospital"
                })
            }
        }
    }
</script>