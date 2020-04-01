<template>
    <div id="loginbox"
         class="mainbox bg-white mx-auto col-12">
        <Loader v-if="isLoading"/>
        <div class="panel panel-info">
            <div class="panel-heading">
                <div class="panel-title text-center text-3xl">Token ที่ได้รับจากผู้ดูแลระบบ</div>
            </div>

            <hr>
            <p class="mb-2 text-sm text-gray">Token คือ รหัสเพื่อใช้ในการลงทะเบียนสำหรับสถานพยาบาล
                ซึ่งจะได้รับหลังจากติดต่อกับผู้ดูแลระบบ
                ภายหลังจากที่ผู้ดูแลระบบได้ยืนยันความถูกต้องให้กับสถานพยาบาลหรือหน่วยงานแล้ว หลังจากที่ใส่ Token
                ไปแล้วก็จะสามารถลงทะเบียนได้</p>

            <div style="padding-top:30px" class="panel-body mb-8">

                <div style="display:none" id="login-alert" class="alert alert-danger col-sm-12"></div>

                <form class="form-horizontal" role="form">
                    <el-alert v-if="error" @close="error=''"
                              :title="error"
                              type="error"
                              show-icon>
                    </el-alert>

                    <div style="margin-bottom: 25px" class="form-group">
                        <label class="">Token</label>
                        <input v-model="token" type="text" class="form-control" placeholder="ใส่ Token"
                               :class="{'is-invalid':validation.firstError('token')}">
                        <div class="invalid-feedback">
                            {{validation.firstError('token')}}
                        </div>
                    </div>


                    <div style="margin-top:10px" class="form-group">
                        <div class="col-sm-12 text-center">
                            <a @click="checkToken" class="btn bg-green text-white w-32 mb-8">ยืนยัน Token</a>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'
    import Loader from "./Loader";
    import {Validator} from "../main";

    export default {
        components: {
            Loader
        },
        data() {
            return {
                isLoading: false,
                token: '',
                error: ''
            }
        },
        validators: {
            token(value) {
                return Validator.value(value)
                    .required("กรุณา Token")
                    .length(10,'กรุณาใส่ให้ครบ 10 หลัก')
            },
        },
        methods: {
            checkToken() {
                this.$validate(["token"]);
                if (this.validation.firstError("token") == null) {
                    this.isLoading = true

                    axios.post(`${this.$store.state.host}/api/accounts/register-token/`, {
                        token: this.token
                    })
                        .then(() => {
                                // if token true
                                this.isLoading = false
                                this.$emit('returnToken', this.token)
                            }
                        )
                        .catch(e=>{
                            this.isLoading = false
                            this.error = e.response.data.error
                        })

                }
            }
        }
    }
</script>