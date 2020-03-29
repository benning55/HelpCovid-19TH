<template>
    <div id="loginbox"
         class="mainbox bg-white mx-auto col-md-8 col-lg-6 col-md-offset-3 col-sm-8 col-sm-offset-2">
        <div class="panel panel-info">
            <div class="panel-heading">
                <div class="panel-title text-center text-3xl">ลงชื่อเข้าใช้ในนามของสถานพยาบาล</div>
            </div>

            <div style="padding-top:30px" class="panel-body mb-8">

                <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>

                <form id="loginform" class="form-horizontal" role="form">

                    <div style="margin-bottom: 25px" class="form-group">
                        <label class="">ชื่อผู้ใช้งาน</label>
                        <input v-model="username" type="text" class="form-control" placeholder="ใส่ชื่อผู้ใช้งาน">
                    </div>

                    <div style="margin-bottom: 25px" class="form-group">
                        <label class="">รหัสผ่าน</label>
                        <input v-model="password" type="password" class="form-control" placeholder="ใส่รหัสผ่าน">
                    </div>


                    <div style="margin-top:10px" class="form-group">
                        <div class="col-sm-12 text-center">
                            <a @click="login" class="btn bg-green text-white w-32 mb-8">Login </a>
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

    export default {
        data() {
            return {
                username: '',
                password: ''
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
                    let formData = new FormData();
                    formData.append('username', this.username);
                    formData.append('password', this.password);

                    // axios.post(this.$store.state.host+'/auth/obtain_token/',formData)
                    // .then(res=>{
                    //     console.log(res)
                    // })
                    // .catch(e=>{
                    //     console.log(e)
                    // })
                    axios.post(this.$store.state.host + '/auth/obtain_token/', {
                        username: this.username,
                        password: this.password
                    })
                        .then((response) => {
                            this.$store.commit('updateToken', response.data.token);
                            //get and set auth user
                            const base = {
                                baseURL: this.$store.state.host + '/api/accounts/',
                                headers: {
                                    // Set your Authorization to 'JWT', not Bearer!!!
                                    Authorization: `JWT ${this.$store.state.jwt}`,
                                    'Content-Type': 'application/json'
                                },
                                xhrFields: {
                                    withCredentials: true
                                }
                            };
                            const axiosInstance = axios.create(base);
                            axiosInstance({
                                url: "/user/",
                                method: "get",
                                params: {}
                            }).then((response) => {
                                this.$store.commit("setAuthUser",
                                    {authUser: response.data, isAuthenticated: true}
                                );
                                this.$router.push("/")
                                // location.reload();
                            }).catch(e => {

                                this.$message.error('Oops, Something is Error. code ' + e.response.status + ', at Login');
                            })
                        })
                        .catch((error) => {
                            console.log(error.response)
                            // if (error.response.status == '400') {
                            //     this.error = 'error_user_alert_username_password_incorrect'
                            // } else {
                            //     this.error = 'something_is_wrong_try_again_later'
                            // }
                        })
                }
            }
        }
    }
</script>