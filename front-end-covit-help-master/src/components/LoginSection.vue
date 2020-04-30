<template>
    <div id="loginbox"
         class="mainbox bg-white mx-auto col-md-8 col-lg-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
        <Loader v-if="isLoading"/>
        <div class="panel panel-info">
            <div class="panel-heading">
                <div class="panel-title text-center text-3xl">ลงชื่อเข้าใช้ในนามของสถานพยาบาล</div>
            </div>

            <div style="padding-top:30px" class="panel-body mb-8">

                <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>

                <form id="loginform" class="form-horizontal" role="form">
                    <el-alert v-if="error" @close="error=''"
                              :title="error"
                              type="error"
                              show-icon>
                    </el-alert>

                    <div style="margin-bottom: 25px" class="form-group">
                        <label class="">ชื่อบัญชีผู้ใช้ (username)</label>
                        <input v-model="username" type="text" class="form-control" placeholder="ใส่ชื่อผู้ใช้งาน"
                               :class="{'is-invalid':validation.firstError('username')}">
                        <div class="invalid-feedback">
                            {{validation.firstError('username')}}
                        </div>
                    </div>

                    <div style="margin-bottom: 25px" class="form-group">
                        <label class="">รหัสผ่าน</label>
                        <input v-model="password" type="password" class="form-control" placeholder="ใส่รหัสผ่าน"
                               :class="{'is-invalid':validation.firstError('password')}">
                        <div class="invalid-feedback">
                            {{validation.firstError('password')}}
                        </div>
                    </div>


                    <div style="margin-top:10px" class="form-group">
                        <div class="col-sm-12 text-center">
                            <a @click="login" class="btn bg-green text-white w-32 mb-8 hover:bg-hover_blue">ลงชื่อเข้าใช้</a>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from 'axios'
    import Loader from "./Loader";

    export default {
        components: {
            Loader
        },
        data() {
            return {
                isLoading: false,
                username: '',
                password: '',
                error: ''
            }
        },
        validators: {
            username(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อผู้ใช้งาน");
            },
            password(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน");
            },
        },
        methods: {
            login() {
                this.$validate(["username", "password"]);
                if (
                    this.validation.firstError("username") == null &&
                    this.validation.firstError("password") == null
                ) {
                    this.isLoading = true
                    let formData = new FormData();
                    formData.append('username', this.username);
                    formData.append('password', this.password);

                    axios.post(this.$store.state.host + '/auth/obtain_token/', formData)
                        .then((response) => {
                            this.$store.commit('updateToken', response.data.token);
                            axios.get(`${this.$store.state.host}/api/accounts/user/`, {
                                baseURL: this.$store.state.host + '/api/accounts/',
                                headers: {
                                    // Set your Authorization to 'JWT', not Bearer!!!
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                                xhrFields: {
                                    withCredentials: true
                                }
                            }).then(res => {
                                this.isLoading = false
                                this.$store.commit("setAuthUser", {authUser: res.data.data[0], isAuthenticated: true});
                                this.$router.push("/")
                            }).catch(e => {
                                this.isLoading = false
                                this.$message({
                                    showClose: true,
                                    message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                                    type: 'error',
                                    duration: 10
                                });
                            })
                        })
                        .catch((error) => {
                            this.isLoading = false
                            if (error.response.status == '400') {
                                this.error = 'ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง'
                            } else {
                                this.error = 'มีบางอย่างผิดพลาด กรุณาลองใหม่ในภายหลัง'
                            }
                        })
                }
            }
        }
    }
</script>