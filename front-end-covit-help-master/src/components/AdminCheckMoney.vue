<template>
    <div>
        <el-divider>ผู้บริจาค</el-divider>
        <el-tabs type="card" @tab-click="handleClick">
            <el-tab-pane>
                <span :class="{'text-red':thisTap == 0}" slot="label"><i
                        class="el-icon-warning"></i>หลักฐานการโอนเงินที่ยังไม่ยืนยัน</span>
                <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <div v-else class="row">
                    <template v-for="(user,index) in donateUser">
                        <transition name="fade" :key="user.id">
                            <div v-if="user.approve_status == false" class="col-sm-6 mb-4" :key="user.id">
                                <div class="shadow-lg">
                                    <a :href="$store.state.host+ user.receipt" data-toggle="lightbox"
                                       data-max-width="800">
                                        <img :src="$store.state.host+ user.receipt"
                                             style="width:100%;height: 300px;object-fit: contain">
                                    </a>
                                    <div class="card-body">
                                        <h1 class="text-3xl">{{numberWithCommas(user.amount)}} ฿</h1>
                                        <td v-if="user.company_name == ''||user.company_name == null">
                                            <i class="fas fa-user-alt"></i> {{user.first_name}} {{user.last_name}}
                                        </td>
                                        <td v-else><i class="fas fa-building"></i>
                                            {{user.company_name}}
                                            <el-popover
                                                    placement="top-start"
                                                    trigger="click">
                                                <table class="table">
                                                    <tbody>
                                                    <tr>
                                                        <th scope="row">ชื่อ-นามสกุล</th>
                                                        <td class="text-right">{{user.first_name}} {{user.last_name}}
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">อีเมลล์</th>
                                                        <td class="text-right">{{user.email}}</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">ใบกำกับภาษี</th>
                                                        <td class="text-right">{{user.tax_id}}</td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                                <el-button slot="reference">ดูข้อมูลบริษัทเพิ่มเติ่ม</el-button>
                                            </el-popover>
                                        </td>
                                        <h1 class="my-2">เบอร์โทร {{user.tel}}</h1>
                                        <h1 class="my-2">ส่งเมื่อเวลา {{time(user.created)}} น.</h1>
                                        <h1 class="my-2">วันที่ {{date(user.created)}} น.</h1>
                                        <!--                                    <h5 class="card-title">{{user}}</h5>-->
                                        <div class="w-10 h-32" style="position: absolute;bottom: 0px;right: 0;">
                                            <label class="switch" style="top:45px;right: 20px">
                                                <input v-model="user.approve_status"
                                                       @change="approve(user.id,index,user.approve_status)"
                                                       type="checkbox"
                                                       class="default">
                                                <span class="slider"></span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </transition>
                    </template>
                </div>
            </el-tab-pane>

            <el-tab-pane label="หลักฐานการโอนเงินที่ยืนยันแล้ว">
                <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <div v-else class="row">
                    <template v-for="(user,index) in donateUser">
                        <transition name="fade" :key="user.id">
                            <div v-if="user.approve_status == true" class="col-sm-6 mb-4" :key="user.id">
                                <div class="shadow-lg ">
                                    <a :href="$store.state.host+ user.receipt" @click="showImage"
                                       data-max-width="800">
                                        <img :src="$store.state.host+ user.receipt"
                                             style="width:100%;height: 300px;object-fit: contain">
                                    </a>
                                    <div class="card-body">
                                        <h1 class="text-3xl">{{numberWithCommas(user.amount)}} ฿</h1>
                                        <td v-if="user.company_name == ''||user.company_name == null">
                                            <i class="fas fa-user-alt"></i> {{user.first_name}} {{user.last_name}}
                                        </td>
                                        <td v-else><i class="fas fa-building"></i>
                                            {{user.company_name}}
                                            <el-popover
                                                    placement="top-start"
                                                    trigger="click">
                                                <table class="table">
                                                    <tbody>
                                                    <tr>
                                                        <th scope="row">ชื่อ-นามสกุล</th>
                                                        <td class="text-right">{{user.first_name}} {{user.last_name}}
                                                        </td>

                                                    </tr>
                                                    <tr>
                                                        <th scope="row">อีเมลล์</th>
                                                        <td class="text-right">{{user.email}}</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row">ใบกำกับภาษี</th>
                                                        <td class="text-right">{{user.tax_id}}</td>
                                                    </tr>
                                                    </tbody>
                                                </table>
                                                <el-button slot="reference">ดูข้อมูลบริษัทเพิ่มเติ่ม</el-button>
                                            </el-popover>
                                        </td>
                                        <h1 class="my-2">ส่งเมื่อเวลา {{time(user.created)}} น.</h1>
                                        <h1 class="my-2">วันที่ {{date(user.created)}} น.</h1>
                                        <!--                                    <h5 class="card-title">{{user}}</h5>-->
                                        <div class="w-10 h-32" style="position: absolute;bottom: 0px;right: 0;">
                                            <label class="switch" style="top:45px;right: 20px">
                                                <input v-model="user.approve_status"
                                                       @change="approve(user.id,index,user.approve_status)"
                                                       type="checkbox"
                                                       class="default">
                                                <span class="slider"></span>
                                            </label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </transition>
                    </template>
                </div>
            </el-tab-pane>

            <el-tab-pane>
                <span :class="{'text-red':thisTap == 2}" slot="label"><i
                        class="el-icon-warning"></i>สิ่งของบริจาครอการยืนยัน</span>
                <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <table v-else class="table">
                    <thead>
                    <tr>
                        <th scope="col">ชื่อ/บริษัท</th>
                        <th scope="col">เบอร์โทรศัพท์</th>
                        <th scope="col">รายการสิ่งของ</th>
                        <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                        <th scope="col" class="text-right">สถานะ</th>
                    </tr>
                    </thead>
                    <tbody>
                    <template v-for="(user,index) in donateObject">
                        <transition name="fade" :key="user.id">
                            <tr v-if="user.approve_status == false" :key="user.id">
                                <td v-if="user.company_name == ''||user.company_name == null">
                                    <i class="fas fa-user-alt"></i> {{user.first_name}} {{user.last_name}}
                                </td>
                                <td v-else><i class="fas fa-building"></i>
                                    {{user.company_name}}
                                    <el-popover
                                            placement="top-start"
                                            trigger="click">
                                        <table class="table">
                                            <tbody>
                                            <tr>
                                                <th scope="row">ชื่อ</th>
                                                <td class="text-right">{{user.first_name}} {{user.last_name}}</td>

                                            </tr>
                                            <tr>
                                                <th scope="row">อีเมลล์</th>
                                                <td class="text-right">{{user.email}}</td>
                                            </tr>
                                            <tr>
                                                <th scope="row">ใบกำกับภาษี</th>
                                                <td class="text-right">{{user.tax_id}}</td>
                                            </tr>
                                            </tbody>
                                        </table>
                                        <el-button slot="reference">ดูข้อมูลบริษัทเพิ่มเติ่ม</el-button>
                                    </el-popover>
                                </td>
                                <td>{{user.tel}}</td>
                                <td>{{user.need.title}}</td>
                                <td>{{Math.floor(user.amount)}}</td>
                                <td>
                                    <label class="switch">
                                        <input v-model="user.approve_status"
                                               @change="approveObj(user.id,index,user.approve_status)" type="checkbox"
                                               class="default">
                                        <span class="slider"></span>
                                    </label>
                                </td>
                            </tr>
                        </transition>
                    </template>
                    </tbody>
                </table>
            </el-tab-pane>

            <el-tab-pane label="สิ่งของบริจาคที่ยืนยันแล้ว">
                <p v-if="donateUser.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <table v-else class="table">
                    <thead>
                    <tr>
                        <th scope="col">ชื่อ</th>
                        <th scope="col">เบอร์โทรศัพท์</th>
                        <th scope="col">รายการสิ่งของ</th>
                        <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                        <th scope="col" class="text-right">สถานะ</th>
                    </tr>
                    </thead>
                    <tbody>
                    <template v-for="(user,index) in donateObject">
                        <transition name="fade" :key="user.id">
                            <tr v-if="user.approve_status == true" :key="user.id">
                                <td v-if="user.company_name == ''||user.company_name == null">
                                    <i class="fas fa-user-alt"></i> {{user.first_name}} {{user.last_name}}
                                </td>
                                <td v-else><i class="fas fa-building"></i>
                                    {{user.company_name}}
                                    <el-popover
                                            placement="top-start"
                                            trigger="click">
                                        <table class="table">
                                            <tbody>
                                            <tr>
                                                <th scope="row">ชื่อ</th>
                                                <td class="text-right">{{user.first_name}} {{user.last_name}}</td>

                                            </tr>
                                            <tr>
                                                <th scope="row">อีเมลล์</th>
                                                <td class="text-right">{{user.email}}</td>
                                            </tr>
                                            <tr>
                                                <th scope="row">ใบกำกับภาษี</th>
                                                <td class="text-right">{{user.tax_id}}</td>
                                            </tr>
                                            </tbody>
                                        </table>
                                        <el-button slot="reference">ดูข้อมูลบริษัทเพิ่มเติ่ม</el-button>
                                    </el-popover>
                                </td>
                                <td>{{user.tel}}</td>
                                <td>{{user.need.title}}</td>
                                <td>{{Math.floor(user.amount)}}</td>
                                <td>
                                    <label class="switch">
                                        <input v-model="user.approve_status"
                                               @change="approveObj(user.id,index,user.approve_status)" type="checkbox"
                                               class="default">
                                        <span class="slider"></span>
                                    </label>
                                </td>
                            </tr>
                        </transition>
                    </template>

                    </tbody>
                </table>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
    import axios from 'axios'
    import moment from 'moment'

    export default {
        data() {
            return {
                activeName: 'first',
                donateUser: [],
                donateObject: [],
                thisTap: 0
            };
        },
        created() {
            this.loadData()
        },
        methods: {
            numberWithCommas(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            showImage() {
                $(document).on('click', '[data-toggle="lightbox"]', function (event) {
                    event.preventDefault();
                    $(this).ekkoLightbox();
                });
            },
            handleClick(tab) {
                this.thisTap = tab.index;
            },
            loadData() {
                axios.get(`${this.$store.state.host}/api/officer/officer-donate-money/`, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(res => {
                        this.donateUser = res.data.data
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration:10
                        });
                    })
                axios.get(`${this.$store.state.host}/api/officer/officer-donate/`, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(res => {
                        this.donateObject = res.data.data
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration:10
                        });
                    })
            },
            time(time) {
                moment.locale('th');
                return moment(time).format('LT')
            },
            date(time) {
                moment.locale('th');
                return moment(time).format('LL')
            },
            approve(id, index, approve) {
                let stringApprove = ''
                if (approve == true) {
                    stringApprove = 'True'
                } else {
                    stringApprove = 'False'
                }
                axios.put(`${this.$store.state.host}/api/officer/officer-donate-money/`, {
                    id: id,
                    approve_status: stringApprove
                }, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(() => {
                        this.donateUser[index].approve_status = approve
                        this.$emit("refresh")
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการรีเฟรชข้อมูล' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration:10
                        });
                    })
            },
            approveObj(id, index, approve) {
                let stringApprove = ''
                if (approve == true) {
                    stringApprove = 'True'
                } else {
                    stringApprove = 'False'
                }
                axios.put(`${this.$store.state.host}/api/officer/officer-donate/`, {
                    id: id,
                    approve_status: stringApprove
                }, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(() => {
                        this.donateObject[index].approve_status = approve
                    })
                    .catch(e=>{
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการเปลี่ยนข้อมูล' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration:10
                        });
                    })
            }
        },
        mounted() {

        }
    }
</script>

<style scoped>
    /* The switch - the box around the slider */
    .switch {
        position: relative;
        display: inline-block;
        width: 60px;
        height: 34px;
        float: right;
    }

    /* Hide default HTML checkbox */
    .switch input {
        display: none;
    }

    /* The slider */
    .slider {
        position: absolute;
        cursor: pointer;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: #f67575;
        -webkit-transition: .4s;
        transition: .4s;
    }

    .slider:before {
        position: absolute;
        content: "";
        height: 26px;
        width: 26px;
        left: 4px;
        bottom: 4px;
        background-color: white;
        -webkit-transition: .4s;
        transition: .4s;
    }

    input.default:checked + .slider {
        background-color: #1eb2a6;
    }


    /*input:focus + .slider {*/
    /*    box-shadow: 0 0 1px #2196F3;*/
    /*}*/

    input:checked + .slider:before {
        -webkit-transform: translateX(26px);
        -ms-transform: translateX(26px);
        transform: translateX(26px);
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity 1.2s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0;
    }
</style>