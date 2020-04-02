<template>
    <div id="signupbox"
         class="mainbox mx-auto bg-white col-md-8 col-lg-6 col-md-offset-3 col-sm-8 col-sm-offset-2 mb-16">
        <div v-if="tokenPass==true" class="panel panel-info">
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
                        <label class="col-md-12">อีเมลล์ของเจ้าหน้าที่สถานพยาบาล</label>
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
                            <el-select v-model="accountBank" filterable placeholder="เลือกธนาคาร">
                                <el-option
                                        v-for="item in dataBank"
                                        :key="item.title"
                                        :label="item.title"
                                        :value="item.title">
                                    <span style="float: left;margin-right: 10px">
                                        <img style="width: 1.75rem;height: 1.75rem" :src="item.icon"></span>
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
        <TypeTokenSection v-else @returnToken="changeStatus"/>
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

                <Loader v-if="isLoading"/>
            </section>
        </el-dialog>

    </div>
</template>

<script>
    import {Validator} from "../main";
    import axios from 'axios'
    import Loader from "./Loader";
    import TypeTokenSection from "./TypeTokenSection";

    export default {
        components: {
            Loader,
            TypeTokenSection
        },
        data() {
            return {
                token:'',
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
                        title: 'ไทยพาณิชย์',
                        icon: 'https://i0.wp.com/www.myshineyhineythailand.com/wp-content/uploads/2019/01/scb-icon.png'
                    },
                    {
                        title: 'ธ.ก.ส',
                        icon: 'https://i.pinimg.com/236x/d3/9a/f8/d39af8e316ffe895c915f6bafa1fbdc7.jpg'
                    },
                    {
                        title: 'กรุงศรี',
                        icon: 'https://www.job4thai.com/wp-content/uploads/job-bank-of-ayudhya.jpg'
                    },
                    {
                        title: 'กรุงไทย'
                        , icon: 'https://www.ttmkshop.com/store/image/catalog/ktb_01.png'
                    },
                    {
                        title: 'ซีไอเอ็มบี'
                        , icon: 'https://s3-ap-southeast-1.amazonaws.com/o77site/njLqHWJUKLA50wJ.svg'
                    },
                    {
                        title: 'ซีตี้แบงก์'
                        ,
                        icon: 'https://lh3.googleusercontent.com/newHcOQB4Yoat7TSDFNkUaz2pD9S8YC0Ylpbq8alCu7A41IQgPQS2oIS_NDBsxcm0wki=s180-rw'
                    },
                    {
                        title: 'ดอยซ์แบงก์'
                        ,
                        icon: 'https://upload.wikimedia.org/wikipedia/commons/7/7b/Deutsche_Bank_logo_without_wordmark.svg'
                    },
                    {
                        title: 'อาคารสงเคราะห์'
                        , icon: 'https://pbs.twimg.com/profile_images/924691693269540864/UjR818gg_400x400.jpg'
                    },
                    {
                        title: 'ออมสิน'
                        ,
                        icon: 'https://scontent.fbkk4-3.fna.fbcdn.net/v/t1.0-9/1011860_414966468616320_2126862519_n.jpg?_nc_cat=106&_nc_sid=85a577&_nc_eui2=AeH__RqUlkVLoxdc1PLP7JS7paHN631IZROPTYwnZswIUIpDQ56joLIC1NlmwGKM0mTG5cpCueFsWOujTwywh18abUT69Zkcz4mClaTQntCMLw&_nc_ohc=DRjuOvCp0KMAX-ndjFR&_nc_ht=scontent.fbkk4-3.fna&oh=443eeb578c18c385cccba46af46c912f&oe=5EA9AB71'
                    },
                    {
                        title: 'เอชเอสบีซี'
                        ,
                        icon: 'https://upload.wikimedia.org/wikipedia/commons/3/3d/HSBC_%E6%BB%99%E8%B1%90_%28logo_only%29.svg'
                    },
                    {
                        title: 'ไอซีบีซี'
                        ,
                        icon: 'https://interprogram.pim.ac.th/uploads/content/2015/04/o_19ie9jlrr1gh21dkntrt1lv913eqa.jpg'
                    },
                    {
                        title: 'ธนาคารอิสลาม'
                        , icon: 'http://baanhathairak.org/wp-content/uploads/2017/12/ibank.png'
                    },
                    {
                        title: 'กสิกรไทย'
                        , icon: 'https://www.ttmkshop.com/store/image/catalog/bank_logo.png'
                    },
                    {
                        title: 'เกียรนาคิน'
                        , icon: 'https://pbs.twimg.com/profile_images/924831197720600578/oRBgHpyi_400x400.jpg'
                    },
                    {
                        title: 'แลนด์ แอนด์ เฮ้าส์'
                        , icon: 'https://iservice.aia.co.th/content/dam/th/th/payment/P3_Mobileapp/9LH_mobile.png'
                    },
                    {
                        title: 'มิซูโฮ'
                        , icon: 'https://upload.wikimedia.org/wikipedia/commons/e/e9/Mizuho_logo.svg'
                    },
                    {
                        title: 'สแตนดาร์ดชาร์เตอร์ด'
                        , icon: 'https://image.flaticon.com/icons/svg/825/825502.svg'
                    },
                    {
                        title: 'ซูมิโตโม'
                        ,
                        icon: 'https://d1p9wirkq0k00v.cloudfront.net/wp-content/uploads/2019/06/27054453/smbc_group_kihon.jpg'
                    },
                    {
                        title: 'ธนชาต'
                        , icon: 'https://s3-ap-southeast-1.amazonaws.com/o77site/BEzryXJ2kSIhXVc.svg'
                    },
                    {
                        title: 'ไทยเครดิต'
                        , icon: 'https://s3-ap-southeast-1.amazonaws.com/o77site/N0irZ0uZbUOAJPx.svg'
                    },
                    {
                        title: 'ทหารไทย'
                        , icon: 'https://s3-ap-southeast-1.amazonaws.com/o77site/xCA8zVQzDcyB0t2.svg'
                    },
                    {
                        title: 'ทิสโก้'
                        , icon: 'https://iservice.aia.co.th/content/dam/th/th/payment/P3_Mobileapp/Tisco.png'
                    },
                    {
                        title: 'ยูโอบี'
                        , icon: 'https://s3-ap-southeast-1.amazonaws.com/o77site/kQMxMy27c1loRiR.svg'
                    },
                ],
                error: '',
                isLoading: false,
                tokenPass: false
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
                    .minLength(9, "กรุณาใส่เบอร์โทรศัพท์เป็นตัวเลขอย่างน้อย 9 หลัก")
                    .maxLength(10, "กรุณาใส่เบอร์โทรศัพท์เป็นตัวเลขไม่เกิน 10 หลัก")
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
            changeStatus(token){
                this.token = token
                this.tokenPass = true
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
            },
            regis() {
                this.isLoading = true
                let formData = new FormData();
                formData.append('token', this.token);
                formData.append('username', this.username);
                formData.append('first_name', this.fname);
                formData.append('last_name', this.lname);
                formData.append('email', this.email);
                formData.append('user_tel', this.user_tel);
                formData.append('password', this.password);
                formData.append('name', this.name);
                formData.append('address', this.address);
                formData.append('hospital_tel', this.tel);
                formData.append('bank_account_name', this.accountName);
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

                axios.post(this.$store.state.host + '/api/accounts/register/', formData)
                    .then(() => {
                        this.isLoading = false
                        this.registerStatus = 'complete'
                    }).catch(e => {
                    this.registerStatus = 'error';
                    this.error = e.response.data.error
                    this.isLoading = false
                    console.log(e.response.data)
                })
            },
            closeModal() {
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
        border-radius: 10px;

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
        z-index: 5 !important;
    }

    .el-dialog__wrapper {
        z-index: 3 !important;
    }

    .v-modal {
        z-index: 2 !important;
    }
</style>