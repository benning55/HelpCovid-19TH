<template>
    <div class="container mt-5">
        <h1 class="text-3xl text-center">ข้อมูลการบริจาค</h1>
        <form class="col-12">
            <div class="form-group ">
                <label>ชื่อจริง</label>
                <p class="mb-2 text-sm text-gray">หากไม่ต้องการระบุให้ใส่เครื่องหมายขีด (-)</p>
                <input v-model="fname" class="form-control"
                       :class="{'is-invalid':validation.firstError('fname')}"
                       placeholder="กรุณาใส่ชื่อจริงของท่าน">
                <div class="invalid-feedback">
                    {{validation.firstError('fname')}}
                </div>
            </div>
            <div class="form-group">
                <label>นามสกุล</label>
                <p class="mb-2 text-sm text-gray">หากไม่ต้องการระบุให้ใส่เครื่องหมายขีด (-)</p>
                <input v-model="lname" class="form-control"
                       :class="{'is-invalid':validation.firstError('lname')}"
                       placeholder="กรุณาใส่นามสกุลของท่าน">
                <div class="invalid-feedback">
                    {{validation.firstError('lname')}}
                </div>
            </div>
            <div class="form-group">
                <label>Email ที่ใช้ติดต่อกลับ</label>
                <p class="mb-2 text-sm text-green">ระบบจะไม่แสดงอีเมลล์ให้ผู้อื่นเห็น</p>
                <p class="mb-2 text-sm text-gray">หากไม่มีให้เว้นว่างไว้</p>
                <input v-model="email" class="form-control"
                       :class="{'is-invalid':validation.firstError('email')}"
                       placeholder="กรุณาใส่ Email ที่ใช้ในการติดต่อกลับ">
                <div class="invalid-feedback">
                    {{validation.firstError('email')}}
                </div>
            </div>
            <div class="form-group">
                <label>เบอร์โทรศัพท์ที่สามารถติดต่อได้</label>
                <p class="mb-2 text-sm text-green">ระบบจะไม่แสดงเบอร์โทรศัพท์ให้ผู้อื่นเห็น</p>
                <p class="mb-2 text-sm text-gray">เจ้าหน้าที่จะติดต่อผ่านเบอร์นี้กลับไปในภายหลัง</p>
                <input v-model="tel" class="form-control" type="number"
                       :class="{'is-invalid':validation.firstError('tel')}"
                       placeholder="กรุณาใส่เบอร์โทรศัพท์ที่สามารถติดต่อได้">
                <div class="invalid-feedback">
                    {{validation.firstError('tel')}}
                </div>
            </div>
            <div class="form-group">
                <label>จำนวนของที่จะบริจาค</label>
                <input v-model="amount" class="form-control" type="number"
                       :class="{'is-invalid':validation.firstError('amount')}"
                       placeholder="กรุณาใส่จำนวนของที่จะบริจาค">
                <div class="invalid-feedback">
                    {{validation.firstError('amount')}}
                </div>
            </div>
            <el-collapse>
                <el-collapse-item name="1">
                    <template slot="title">
                        <h1 style="font-size: 1rem;margin: 10px 0 10px 0">ข้อมูลสำหรับบริษัทสำหรับออกใบกำกับภาษี
                            (สำหรับบริษัท)</h1>
                    </template>
                    <div class="form-group col-12">
                        <label style="font-size: 1rem">ชื่อบริษัท</label>
                        <input v-model="company_name" class="form-control"
                               type="text"
                               placeholder="ใส่ชื่อบริษัท">
                    </div>

                    <div class="form-group col-12">
                        <label style="font-size: 1rem">เลขที่ใบกำกับภาษี</label>
                        <input v-model="tax_id" class="form-control"
                               type="number"
                               placeholder="ใส่เลขใบกำกับภาษี">
                    </div>
                </el-collapse-item>
            </el-collapse>
            <div class="flex justify-between my-5">
                <button @click="$router.go(-1)" type="button" class="btn bg-white text-black">ย้อนกลับ</button>
                <button @click="validate" type="button" class="btn bg-green text-white">
                    ส่งความประสงค์จะบริจาคให้เจ้าหน้าที่
                </button>
            </div>
        </form>

        <el-dialog title="ยืนยัน" :visible.sync="confirmDialog" @closed="closeModal">
            <section>
                <!--                        show when complete-->
                <div v-if="sentStatus == 'complete'" class="h-full flex flex-wrap">
                    <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-check-circle"></i></div>
                    <p class="pb-5">ส่งข้อมูลให้เจ้าหน้าที่แล้ว กรุณารอการติดต่อกลับจากเจ้าหน้าที่</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button type="primary" @click="goHome">กลับไปหน้าหลัก</el-button>
                    </span>
                </div>

                <div v-else-if="sentStatus == 'error'" class="h-full ">
                    <div class="w-full text-center text-red" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-times-circle"></i></div>
                    <h1 class="pb-3 text-center">การส่งข้อมูลไม่สำเร็จ กรุณาลองใหม่ในภายหลัง</h1>
                    <!--                    <div v-for="err in error[Object.keys(error)[0]][Object.keys(error[Object.keys(error)[0]])[0]]"-->
                    <!--                         :key="error.id" class="alert bg-red text-white mb-1" role="alert">-->
                    <!--                        {{err}}-->
                    <!--                    </div>-->
                    <span slot="footer" class="dialog-footer w-full">
                        <el-button @click="confirmDialog = false">ปิด</el-button>
                    </span>
                </div>

                <!--                        show before select-->
                <div v-else class="flex flex-wrap content-between">
                    <p class="mb-12">คุณต้องการส่งข้อมูลให้เจ้าหน้าที่หรือไม่</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="confirmDialog = false">แก้ไขข้อมูล</el-button>
                        <el-button @click="sent" type="primary">ส่งข้อมูลไปยังเจ้าหน้าที่</el-button>
                    </span>
                </div>
                <Loader v-if="isLoading"/>
            </section>
        </el-dialog>
    </div>
</template>

<script>
    import Loader from "../components/Loader";
    import axios from 'axios'
    import {Validator} from "../main";

    export default {
        components: {
            Loader
        },
        data() {
            return {
                isLoading: false,
                fname: '',
                lname: '',
                email: '',
                tel: '',
                amount: '',
                company_name: '',
                tax_id: '',
                confirmDialog: false,
                sentStatus: 'none'
            }
        },
        validators: {
            fname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อจริง");
            },
            lname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่นามสกุล");
            },
            email(value) {
                return Validator.value(value)
                    .email("รูปแบบอีเมลล์ไม่ถูกต้อง");
            },
            tel(value) {
                return Validator.value(value)
                    .required("กรุณาระบุรายละเอียด")
                    .integer("กรุณาระบุจำนวนเป็นตัวเลข")
                    .length(10, "กรุณาระบุจำนวนเป็นตัวเลขจำนวน 10 หลัก");
            },
            amount(value) {
                return Validator.value(value)
                    .required("กรุณาระบุจำนวน")
                    .integer("กรุณาระบุจำนวนเป็นตัวเลข")
                    .greaterThan(0, "กรุณาระบุจำนวนเป็นตัวเลขที่มีค่ามากกว่า 0")
            },

        },
        methods: {
            closeModal() {
                if (this.sentStatus == 'complete') {
                    this.$router.go(-1)
                } else if (this.sentStatus == 'error') {
                    this.sentStatus = 'none'
                }
            },
            validate() {
                this.$validate(["fname", "lname", "email", "tel", "amount"]);
                if (
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null &&
                    this.validation.firstError("email") == null &&
                    this.validation.firstError("tel") == null &&
                    this.validation.firstError("amount") == null
                ) {
                    this.sentStatus = 'none'
                    this.confirmDialog = true
                    $(".el-dialog").css({"max-width": "350px"});
                }
            },
            sent() {
                this.isLoading = true
                let formData = new FormData();
                formData.append('company_name', this.company_name);
                formData.append('tax_id', this.tax_id);
                formData.append('need_id', this.$route.params.id);
                formData.append('first_name', this.fname);
                formData.append('last_name', this.lname);
                formData.append('email', this.email);
                formData.append('tel', this.tel);
                formData.append('amount', this.amount);

                axios.post(`${this.$store.state.host}/api/posts/donate/`, formData)
                    .then(() => {
                        this.sentStatus = 'complete'
                        this.isLoading = false
                    })
                    .catch(e => {
                        this.sentStatus = 'error'
                        this.isLoading = false
                    })
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
    .el-dialog {
        width: 95% !important;
        top: 30%;
        -ms-transform: translate(0%, -50%);
        transform: translate(0%, -50%);
    }
</style>