<template>
    <div>
        <el-divider>ผู้บริจาค</el-divider>
        <el-tabs type="card" @tab-click="handleClick">
            <el-tab-pane>
                <span class="text-red" slot="label"><i class="el-icon-warning"></i>ยังไม่ยืนยัน</span>
                <p v-if="donater.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <table v-else class="table">
                    <thead>
                    <tr>
                        <th scope="col">ชื่อ</th>
                        <th scope="col">นามสกุล</th>
                        <th scope="col">เบอร์โทรศัพท์</th>
                        <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                        <th scope="col" class="text-right">สถานะ</th>
                    </tr>
                    </thead>
                    <tbody>
                    <template v-for="(user,index) in donater">
                        <tr v-if="user.approve_status == false" :key="user.id">
                            <td>{{user.first_name}}</td>
                            <td>{{user.last_name}}</td>
                            <td>{{user.tel}}</td>
                            <td>{{Math.floor(user.amount)}}</td>
                            <td>
                                <label class="switch">
                                    <input v-model="user.approve_status"
                                           @change="approve(user.id,index,user.approve_status)" type="checkbox"
                                           class="default">
                                    <span class="slider"></span>
                                </label>
                            </td>
                        </tr>
                    </template>

                    </tbody>
                </table>
            </el-tab-pane>
            <el-tab-pane label="ยืนยันแล้ว">
                <p v-if="donater.length == 0" class="my-5 text-center">ยังไม่มีผู้บริจาคในขณะนี้</p>
                <table v-else class="table">
                    <thead>
                    <tr>
                        <th scope="col">ชื่อ</th>
                        <th scope="col">นามสกุล</th>
                        <th scope="col">เบอร์โทรศัพท์</th>
                        <th scope="col" style="width: 110px">จำนวน(หน่วย)</th>
                        <th scope="col" class="text-right">สถานะ</th>
                    </tr>
                    </thead>
                    <tbody>
                    <template v-for="(user,index) in donater">
                        <tr v-if="user.approve_status == true" :key="user.id">
                            <td>{{user.first_name}}</td>
                            <td>{{user.last_name}}</td>
                            <td>{{user.tel}}</td>
                            <td>{{Math.floor(user.amount)}}</td>
                            <td>
                                <label class="switch">
                                    <input v-model="user.approve_status"
                                           @change="approve(user.id,index,user.approve_status)" type="checkbox"
                                           class="default">
                                    <span class="slider"></span>
                                </label>
                            </td>
                        </tr>
                    </template>

                    </tbody>
                </table>
            </el-tab-pane>
        </el-tabs>
    </div>
</template>

<script>
    import axios from "axios";

    export default {
        props: [
            "id"
        ],
        data() {
            return {
                donater: [],
                check: false
            }
        },
        created() {
            this.loadData()
        },
        methods: {
            handleClick(tab, event) {
                console.log(tab, event);
            },
            loadData() {
                axios.get(`${this.$store.state.host}/api/officer/officer-donate/${this.id}`, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(res => {
                        console.log(res)
                        this.donater = res.data.data
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
            approve(id, index, approve) {
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
                        this.donater[index].approve_status = approve
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration: 10
                        });
                    })
            }
        }
    }
</script>

<style>
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
</style>