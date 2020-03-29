<template>
    <div id="signupbox"
         class="mainbox mx-auto bg-white col-md-8 col-lg-6 col-md-offset-3 col-sm-8 col-sm-offset-2 mb-16">
        <div class="panel panel-info">
            <div class="panel-heading text-center text-3xl">
                <div class="panel-title">ลงทะเบียนในนามของสถานพยาบาล</div>
            </div>
            <div class="panel-body">
                <form id="signupform" class="form-horizontal" role="form">
                    <div class="panel-title text-xl">ข้อมูลของสถานพยาบาล</div>
                    <hr>
                    <p class="mb-2 text-sm text-gray">ในส่วนนี้จะต้องใส่ข้อมูลต่าง ๆ ของสถานพยาบาล
                        รวมไปถึงบัญชีธนาคารสำหรับรับบริจาคเงินในรูปแบบการโอนเงินบริจาค</p>
                    <div class="form-group">
                        <label class="col-12">ชื่อสถานพยาบาล</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="name" class="form-control"
                                   :class="{'is-invalid':validation.firstError('name')}"
                                   placeholder="ใส่ชื่อสถานพยาบาล">
                            <div class="invalid-feedback">
                                {{validation.firstError('name')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-12">รูปภาพเกี่ยวกับสถานพยาบาล</label>
                        <p class="mb-2 text-sm text-gray col-12">เช่น รูปสัญลักษณ์ หรือเป็นรูปสถานที่
                            (ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-12 upload-section">
                            <div class="upload-btn-wrapper w-full">
                                <div class="">
                                    <div class="image-cropper border-2 border-dashed border-black text-center">
                                        <img
                                                v-if="imageData!=null"
                                                :src="profileImageURL"
                                                alt="avatar"
                                                class="profile-pic"
                                        />
                                        <p v-else class="center-y">อัปโหลดรูปภาพ</p>
                                    </div>
                                </div>
                                <input type="file" @change="previewImage" accept="image/*"/>
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-12 ">ที่อยู่ของสถานพยาบาล</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-12">
                            <textarea v-model="address" class="form-control" name="passwd"
                                      :class="{'is-invalid':validation.firstError('address')}"
                                      placeholder="ใส่ที่อยู่ของสถานพยาบาล"></textarea>
                            <div class="invalid-feedback">
                                {{validation.firstError('address')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-12 ">เบอร์โทรศัพท์ที่ติดต่อได้ของสถานพยาบาล</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="tel" type="number" class="form-control" name="passwd"
                                   :class="{'is-invalid':validation.firstError('tel')}"
                                   placeholder="ใส่เบอร์โทรศัพท์ที่ติดต่อได้ของสถานพยาบาล">
                            <div class="invalid-feedback">
                                {{validation.firstError('tel')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-12">อีเมลล์ของสถานพยาบาล</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="email" type="text" class="form-control" name="email"
                                   :class="{'is-invalid':validation.firstError('email')}"
                                   placeholder="ใส่อีเมลล์ของสถานพยาบาล">
                            <div class="invalid-feedback">
                                {{validation.firstError('email')}}
                            </div>
                        </div>
                    </div>

                    <div class="panel-title text-xl">บัญชีธนาคาร</div>
                    <hr>
                    <p class="mb-2 text-sm text-gray">
                        ข้อมูลในส่วนนี้จะแสดงให้เห็นแก่ผู้มีความประสงค์จะบริจาคผ่านการโอนเงิน</p>

                    <div class="form-group">
                        <label class="col-12 ">ชื่อบัญชี</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="accountName" class="form-control"
                                   :class="{'is-invalid':validation.firstError('accountName')}"
                                   placeholder="ใส่ชื่อบัญชี">
                            <div class="invalid-feedback">
                                {{validation.firstError('accountName')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-12 ">เลขบัญชี</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="accountNumber" type="number" class="form-control"
                                   :class="{'is-invalid':validation.firstError('accountNumber')}"
                                   placeholder="ใส่เลขบัญชี">
                            <div class="invalid-feedback">
                                {{validation.firstError('accountNumber')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-12 ">ธนาคาร</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <!--                            <input v-model="accountBank" type="number" class="form-control"-->
                            <!--                                   :class="{'is-invalid':validation.firstError('accountBank')}"-->
                            <!--                                   placeholder="ธนาคาร">-->
                            <el-select v-model="accountBank" filterable placeholder="เลือกธนาคาร">
                                <el-option
                                        v-for="item in dataBank"
                                        :key="item.title"
                                        :label="item.title"
                                        :value="item.title">
                                    <span style="float: left;margin-right: 10px"><img style="height: 1.75rem"
                                                                                      src="../assets/logo.png"></span>
                                    <span style="float: left">{{ item.title }}</span>
                                </el-option>
                            </el-select>
                            <div v-if="validation.firstError('accountBank')" class="text-sm text-red">
                                {{validation.firstError('accountBank')}}
                            </div>
                        </div>
                    </div>

                    <div class="panel-title text-xl">ข้อมูลเจ้าหน้าที่</div>
                    <hr>
                    <p class="mb-2 text-sm text-gray">เจ้าหน้าที่จะมีหน้าที่ตรวจสอบการหลักฐานการบริจาค</p>

                    <div class="form-group">
                        <label class="col-12 ">ชื่อผู้ใช้งาน</label>
                        <p class="mb-2 text-sm text-green col-12">กรุณาจดชื่อผู้ใช้งานเพื่อใช้ในการลงชื่อเข้าใช้งาน</p>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="username" type="text" class="form-control" name="email"
                                   :class="{'is-invalid':validation.firstError('username')}"
                                   placeholder="ใส่ชื่อผู้ใช้งาน">
                            <div class="invalid-feedback">
                                {{validation.firstError('username')}}
                            </div>
                        </div>
                    </div>

                    <div class="form-group">
                        <label class="col-md-12">ชื่อจริง</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="fname" type="text" class="form-control" name="firstname"
                                   :class="{'is-invalid':validation.firstError('fname')}"
                                   placeholder="ใส่ชื่อจริง">
                            <div class="invalid-feedback">
                                {{validation.firstError('fname')}}
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-12">นามสกุล</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="lname" type="text" class="form-control" name="lastname"
                                   :class="{'is-invalid':validation.firstError('lname')}"
                                   placeholder="ใส่นามสกุล">
                            <div class="invalid-feedback">
                                {{validation.firstError('lname')}}
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-12">เบอร์โทรศัพท์ของเจ้าหน้าที่</label>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="user_tel" type="text" class="form-control" name="lastname"
                                   :class="{'is-invalid':validation.firstError('user_tel')}"
                                   placeholder="ใส่เบอร์ของเจ้าหน้าที่">
                            <div class="invalid-feedback">
                                {{validation.firstError('user_tel')}}
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-12">รหัสผ่าน</label>
                        <p class="mb-2 text-sm text-green col-12">กรุณาจดรหัสผ่านเพื่อใช้ในการลงชื่อเข้าใช้</p>
                        <p class="mb-2 text-sm text-gray col-12">(ไม่สามารถเปลี่ยนแปลงได้ภายหลัง)</p>
                        <div class="col-md-12">
                            <input v-model="password" type="password" class="form-control" name="passwd"
                                   :class="{'is-invalid':validation.firstError('password')}"
                                   placeholder="ใส่รหัสผ่าน">
                            <div class="invalid-feedback">
                                {{validation.firstError('password')}}
                            </div>
                        </div>
                    </div>
                    <div class="form-group">
                        <label class="col-md-12">รหัสผ่านอีกครั้ง</label>
                        <div class="col-md-12">
                            <input v-model="repassword" type="password" class="form-control" name="passwd"
                                   :class="{'is-invalid':validation.firstError('repassword')}"
                                   placeholder="ใส่รหัสผ่านอีกครั้ง">
                            <div class="invalid-feedback">
                                {{validation.firstError('repassword')}}
                            </div>
                        </div>
                    </div>

                    <div class="">
                        <div class="col-sm-12 text-center">
                            <a @click="showDialog" class="btn bg-green text-white w-32 mb-8">ลงทะเบียน</a>
                        </div>
                    </div>
                </form>
            </div>
        </div>
        <el-dialog title="ลงทะเบียน" :visible.sync="confirmDialog" @closed="closeModal">
            <section>
                <!--                        show when complete-->
                <div v-if="registerStatus == 'complete'" class="h-full flex flex-wrap">
                    <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-check-circle"></i></div>
                    <p class="pb-5">การลงทะเบียนสำเร็จ กรุณารอการติดต่อกลับเพื่อรับการยืนยันจากผู้ดูแลระบบ
                        เมื่อได้รับการยืนยันแล้วจะสามารถลงชื่อเข้าใช้ได้</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button type="primary" @click="goHome">กลับไปหน้าหลัก</el-button>
                    </span>
                </div>

                <div v-else-if="registerStatus == 'error'" class="h-full ">
                    <div class="w-full text-center text-red" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-times-circle"></i></div>
                    <h1 class="pb-3 text-center">การลงทะเบียนไม่สำเร็จ</h1>
                    <div v-for="err in error[Object.keys(error)[0]][Object.keys(error[Object.keys(error)[0]])[0]]"
                         :key="error.id" class="alert bg-red text-white mb-1" role="alert">
                        {{err}}
                    </div>
                    <span slot="footer" class="dialog-footer w-full">
                        <el-button @click="confirmDialog = false">ตรวจสอบอีกครั้ง</el-button>
                    </span>
                </div>

                <!--                        show before select-->
                <div v-else class="flex flex-wrap content-between">
                    <p class="mb-12">ข้อมูลที่จะบันทึกจะไม่สามารถแก้ไขในภายหลังได้ คุณแน่ใจที่จะลงทะเบียนหรือไม่</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="confirmDialog = false">ตรวจสอบอีกครั้ง</el-button>
                        <el-button @click="regis" type="primary">ลงทะเบียน</el-button>
                    </span>
                </div>
            </section>
        </el-dialog>
    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from 'axios'

    export default {
        data() {
            return {
                username: '',
                fname: '',
                lname: '',
                email: '',
                user_tel: '',
                password: '',
                repassword: '',
                name: '',
                address: '',
                tel: '',
                accountName: "",
                accountNumber: "",
                accountBank: "",
                imageData: null,
                profileImageURL: null,
                confirmDialog: false,
                registerStatus: 'none',
                dataBank: [
                    {
                        title: 'ไทยพาณิชย์'
                    },
                    {
                        title: 'ธ.ก.ส'
                    },
                    {
                        title: 'กรุงศรี'
                    },
                    {
                        title: 'กรุงไทย'
                    },
                    {
                        title: 'ซีไอเอ็มบี'
                    },
                    {
                        title: 'ซีตี้แบงก์'
                    },
                    {
                        title: 'ดอยซ์แบงก์'
                    },
                    {
                        title: 'อาคารสงเคราะห์'
                    },
                    {
                        title: 'ออมสิน'
                    },
                    {
                        title: 'เอชเอสบีซี'
                    },
                    {
                        title: 'ไอซีบีซี'
                    },
                    {
                        title: 'ธนาคารอิสลาม'
                    },
                    {
                        title: 'กสิกรไทย'
                    },
                    {
                        title: 'เกียรนาคิน'
                    },
                    {
                        title: 'แลนด์ แอนด์ เฮ้าส์'
                    },
                    {
                        title: 'มิซูโฮ'
                    },
                    {
                        title: 'สแตนดาร์ดชาร์เตอร์ด'
                    },
                    {
                        title: 'ซูมิโตโม'
                    },
                    {
                        title: 'ธนชาต'
                    },
                    {
                        title: 'ไทยเครดิต'
                    },
                    {
                        title: 'ทหารไทย'
                    },
                    {
                        title: 'ทิสโก้'
                    },
                    {
                        title: 'ยูโอบี'
                    },
                ],
                error: ''
            }
        },
        validators: {
            username(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อผู้ใช้");
            },
            fname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อจริง");
            },
            lname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่นามสกุล");
            },
            user_tel(value) {
                return Validator.value(value)
                    .required("กรุณาเบอร์ของเจ้าหน้าที่")
                    .length(10, "กรุณาใส่เบอร์โทรศัพท์เป็นตัวเลข 10 หลัก");
            },
            email(value) {
                return Validator.value(value)
                    .required("กรุณาอีเมลล์")
                    .email("รูปแบบอีเมลล์ไม่ถูกต้อง");
            },
            password(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่าน")
                    .minLength(8, "รหัสต้องมีมากกว่า 8 ตัว")
            },
            repassword(value) {
                return Validator.value(value)
                    .required("กรุณาใส่รหัสผ่านอีกครั้ง")
                    .match(this.password, 'รหัสผ่านไม่ตรงกัน')
            },
            name(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อสถานพยาบาล");
            },
            address(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ที่อยู่สถานพยาบาล");
            },
            tel(value) {
                return Validator.value(value)
                    .required("กรุณาใส่เบอร์โทรศัพท์")
                    .length(10, "กรุณาใส่เบอร์โทรศัพท์เป็นตัวเลข 10 หลัก");
            },
            accountName(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อบัญชี");
            },
            accountNumber(value) {
                return Validator.value(value)
                    .required("กรุณาใส่เลขบัญชี");
            },
            accountBank(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ธนาคาร");
            }

        },
        methods: {
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            showDialog() {
                this.$validate(["username", "fname", "lname", "user_tel", "email", "password", "repassword", "name", "address", "tel", "accountName", "accountNumber", "accountBank"]);
                if (
                    this.validation.firstError("username") == null &&
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null &&
                    this.validation.firstError("user_tel") == null &&
                    this.validation.firstError("email") == null &&
                    this.validation.firstError("password") == null &&
                    this.validation.firstError("repassword") == null &&
                    this.validation.firstError("name") == null &&
                    this.validation.firstError("address") == null &&
                    this.validation.firstError("tel") == null &&
                    this.validation.firstError("accountName") == null &&
                    this.validation.firstError("accountNumber") == null &&
                    this.validation.firstError("accountBank") == null
                ) {
                    $(".el-dialog").css({"max-width": "350px"});
                    this.confirmDialog = true
                }

                this.confirmDialog = true
            },
            regis() {
                let formData = new FormData();
                formData.append('username', this.username);
                formData.append('first_name', this.fname);
                formData.append('last_name', this.lname);
                formData.append('email', this.email);
                formData.append('user_tel', this.user_tel);
                formData.append('password', this.password);
                formData.append('name', this.name);
                formData.append('address', this.address);
                formData.append('hospital_tel', this.tel);
                formData.append('back_account_name', this.accountName);
                formData.append('bank_account_number', this.accountNumber);
                formData.append('bank_name', this.accountBank)
                formData.append('picture', this.imageData)

                // formData.append('username', 'anusornleon');
                // formData.append('first_name', 'leffsef');
                // formData.append('last_name', 'fsefsef');
                // formData.append('email', 'anusornleo@gmail.com');
                // formData.append('user_tel', '0215152021');
                // formData.append('password', 'leo123456');
                // formData.append('name', 'โรงบาลนะครับ')
                // formData.append('address', 'sfrsf wef s');
                // formData.append('hospital_tel', '0215555555');
                // formData.append('back_account_name', "this.accountName");
                // formData.append('bank_account_number', "5484984989484");
                // formData.append('bank_name', "this.accountBank")
                // formData.append('picture', this.imageData)


                for (let pair of formData.entries()) {
                    console.log(pair[0] + ', ' + pair[1]);
                }

                axios.post(this.$store.state.host + '/api/accounts/register/', formData)
                    .then(res => {
                        console.log(res)
                        this.registerStatus = 'complete'
                    }).catch(e => {
                    this.registerStatus = 'error';
                    this.error = e.response.data.error
                    console.log(e.response.data.error)
                })


            },
            closeModal() {
                console.log('close')
                this.registerStatus = 'none'
                this.error = ''
            },
            goHome() {
                this.$router.push({
                    name: "Home"
                })
            }
        }
    }
</script>

<style>
    .upload-btn-wrapper {
        position: relative;
        overflow: hidden;
        display: inline-block;
    }

    .upload-btn-wrapper input[type="file"] {
        font-size: 30px;
        position: absolute;
        left: 0;
        top: 0;
        opacity: 0;
        width: 100%;
        height: 100%;
    }

    .image-cropper {
        width: 100%;
        height: 290px;
        position: relative;
        overflow: hidden;
        margin: auto;
    }

    .profile-pic {
        object-fit: contain;
        height: 100%;
        width: 99.8%;
    }

    .el-dialog {
        width: 95% !important;
        top: 30%;
        -ms-transform: translate(0%, -50%);
        transform: translate(0%, -50%);
    }
</style>