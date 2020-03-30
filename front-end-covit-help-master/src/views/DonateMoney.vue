<template>
    <div class="container mt-5">
        <h1 class="text-3xl text-center">บริจาคเงิน</h1>
        <form>
            <div class="form-group">
                <label>ชื่อจริง</label>
                <p class="mb-2 text-sm text-gray">หากไม่ต้องการระบุให้ใส่เครื่องหมายขีด (-)</p>
                <input v-model="fname" class="form-control"
                       :class="{'is-invalid':validation.firstError('fname')}"
                       placeholder="กรุณาใส่ชื่อจริง">
                <div class="invalid-feedback">
                    {{validation.firstError('fname')}}
                </div>
            </div>
            <div class="form-group">
                <label>นามสกุล</label>
                <p class="mb-2 text-sm text-gray">หากไม่ต้องการระบุให้ใส่เครื่องหมายขีด (-)</p>
                <input v-model="lname" class="form-control"
                       placeholder="กรุณาใส่นามสกุล"
                       :class="{'is-invalid':validation.firstError('lname')}">
                <div class="invalid-feedback">
                    {{validation.firstError('lname')}}
                </div>
            </div>

            <div class="form-group">
                <label v-if="validation.firstError('imageData')"
                       class="text-red">{{validation.firstError('imageData')}}</label>
                <label v-else>รูปของหลักฐานการบริจาค เช่น สลิปโอนเงิน</label>
                <p class="mb-2 text-sm text-gray">หลักฐานการโอนเงินของคุณจะถูกเก็บไว้เป็นความลับ</p>
                <div class="col-12 upload-section">
                    <div class="upload-btn-wrapper w-full">
                        <div class="">
                            <div class="image-cropper border-2 border-dashed border-black text-center">
                                <img v-if="imageData!=null"
                                     :src="profileImageURL"
                                     alt="avatar"
                                     class="profile-pic"
                                />
                                <p v-else class="center-y">อัปโหลดรูปภาพที่นี่</p>
                            </div>
                        </div>
                        <input type="file" @change="previewImage" accept="image/*"/>
                    </div>
                </div>
            </div>


            <div class="form-group">
                <label>จำนวนเงินที่บริจาค</label>
                <input v-model="amount" class="form-control"
                       type="number"
                       :class="{'is-invalid':validation.firstError('amount')}"
                       placeholder="กรุณาจำนวนเงินรับบริจาค">
                <div class="invalid-feedback">
                    {{validation.firstError('amount')}}
                </div>
            </div>
        </form>
        <button @click="sent" type="button" class="btn bg-green text-white">ส่งหลักฐานการบริจาค</button>


        <el-dialog title="ยืนยัน" :visible.sync="confirmDialog" @closed="closeModal" center>
            <span v-if="sentStatus == 'complete'" class="h-full flex flex-wrap">
                <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                    <i class="far fa-check-circle"></i>
                </div>
                <p class="pb-5">ส่งข้อมูลให้เจ้าหน้าที่แล้ว กรุณารอการติดต่อกลับจากเจ้าหน้าที่</p>

                    <span class="w-full">
                            <el-button @click="closeModal" type="primary" style="width: 50%;margin-left: 50%;transform: translateX(-50%);">ตกลง</el-button>

                </span>
            </span>
            <span v-else-if="sentStatus == 'error'" class="h-full ">
                <div class="w-full text-center text-red" style="font-size: 6.2rem;padding-bottom: 26px">
                    <i class="far fa-times-circle"></i>
                </div>
                <h1 class="pb-3 text-center">การส่งข้อมูลไม่สำเร็จ กรุณาลองใหม่ในภายหลัง</h1>
                <span class="w-full">
                    <el-button @click="confirmDialog = false"
                               style="width: 50%;margin-left: 50%;transform: translateX(-50%);">ปิด</el-button>
                </span>
            </span>
        </el-dialog>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";

    export default {
        data() {
            return {
                fname: '',
                lname: '',
                amount: '',
                imageData: null,
                profileImageURL: null,
                confirmDialog: false,
                sentStatus: "none"
            }
        },
        validators: {
            fname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่ชื่อจริง");
            },
            lname(value) {
                return Validator.value(value)
                    .required("กรุณาใส่นามสกุลจริง");
            },
            amount(value) {
                return Validator.value(value)
                    .required("กรุณาระบุจำนวน")
                    .integer("กรุณาระบุจำนวนเป็นตัวเลข")
                    .greaterThan(0, "กรุณาระบุจำนวนเป็นตัวเลขที่มีค่ามากกว่า 0")
            },
            imageData(value) {
                return Validator.value(value)
                    .required("กรุณาอัปโหลดหลักฐานการบริจาค");
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
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            sent() {
                this.$validate(["fname", "lname", "amount", "imageData"]);
                if (
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null &&
                    this.validation.firstError("amount") == null &&
                    this.validation.firstError("imageData") == null
                ) {
                    let formData = new FormData();
                    formData.append('hospital_id', this.$route.params.id);
                    formData.append('first_name', this.fname);
                    formData.append('last_name', this.lname);
                    formData.append('amount', this.amount);
                    formData.append('receipt', this.imageData);

                    axios.post(`${this.$store.state.host}/api/posts/money-donate/`,
                        formData,
                        {
                            headers: {
                                'Content-Type': 'multipart/form-data'
                            },
                        }
                    )
                        .then(res => {
                            console.log(res)
                            this.confirmDialog = true
                            $(".el-dialog").css({"max-width": "350px"});
                            this.sentStatus = 'complete'
                        })
                        .catch(e => {
                            this.confirmDialog = true
                            $(".el-dialog").css({"max-width": "350px"});
                            this.sentStatus = 'error'
                            console.log(e)
                        })

                    for (let pair of formData.entries()) {
                        console.log(pair[0] + ', ' + pair[1]);
                    }
                }
            }
        }
    }
</script>

<style scoped>
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
</style>