<template>
    <div class="container mt-5">
        <h1 class="text-3xl text-center">รับบริจาค</h1>
        <form>
            <div class="form-group">
                <label>หัวข้อ</label>
                <input v-model="title" class="form-control"
                       :class="{'is-invalid':validation.firstError('title')}"
                       placeholder="กรุณาใส่ชื่อหัวข้อ">
                <div class="invalid-feedback">
                    {{validation.firstError('title')}}
                </div>
            </div>
            <div class="form-group">
                <label>รายละเอียด</label>
                <textarea v-model="description" class="form-control"
                          placeholder="กรุณาใส่รายระเอียดเกี่ยวกับของรับบริจาค"
                          :class="{'is-invalid':validation.firstError('description')}">
                </textarea>
                <div class="invalid-feedback">
                    {{validation.firstError('description')}}
                </div>
            </div>

            <div class="form-group">
                <label>รูปของโพสต์ เช่น รูปตัวอย่างของที่รับบริจาค</label>
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
                <label class="col-12">จำนวน</label>
                <input v-model="amount" class="form-control"
                       type="number"
                       :class="{'is-invalid':validation.firstError('amount')}"
                       placeholder="กรุณาจำนวนที่ต้องการรับบริจาค">
                <div class="invalid-feedback">
                    {{validation.firstError('amount')}}
                </div>
            </div>
        </form>
        <button @click="createPost" type="button" class="btn bg-green text-white mb-5">ลงรับบริจาค</button>

        <el-dialog title="ยืนยัน" :visible.sync="confirmDialog" @closed="closeModal">
            <section>
                <!--                        show when complete-->
                <div v-if="sentStatus == 'complete'" class="h-full flex flex-wrap">
                    <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-check-circle"></i></div>
                    <p class="pb-5">บันทึกข้อมูลการรับบริจาคเรียบร้อย</p>
                    <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button type="primary" @click="closeModal">กลับไปหน้า Dashboard</el-button>
                    </span>
                </div>

                <div v-else-if="sentStatus == 'error'" class="h-full ">
                    <div class="w-full text-center text-red" style="font-size: 6.2rem;padding-bottom: 26px">
                        <i class="far fa-times-circle"></i></div>
                    <h1 class="pb-3 text-center">การบันทึกข้อมูลไม่สำเร็จ กรุณาลองใหม่ในภายหลัง</h1>
                    <span slot="footer" class="dialog-footer w-full">
                        <el-button @click="confirmDialog = false">ปิด</el-button>
                    </span>
                </div>
                <Loader v-if="isLoading"/>
            </section>
        </el-dialog>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import Loader from "../components/Loader";

    export default {
        components:{
            Loader
        },
        data() {
            return {
                isLoading:false,
                title: '',
                description: '',
                amount: 1,
                imageData: null,
                profileImageURL: null,
                sentStatus: 'none',
                confirmDialog: false,
                error: ''
            }
        },
        validators: {
            title(value) {
                return Validator.value(value)
                    .required("กรุณาระบุหัวข้อ");
            },
            description(value) {
                return Validator.value(value)
                    .required("กรุณาระบุรายละเอียด");
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
                    this.$router.push({
                        name: "DashboardHospital",
                        params: {id: this.$store.state.authUser.hospital.id}
                    })
                } else if (this.sentStatus == 'error') {
                    this.sentStatus = 'none'
                }
            },
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            createPost() {
                this.$validate(["title", "description", "amount"]);
                if (
                    this.validation.firstError("title") == null &&
                    this.validation.firstError("description") == null &&
                    this.validation.firstError("amount") == null
                ) {
                    this.isLoading = true
                    let formData = new FormData();
                    formData.append('picture', this.imageData);
                    formData.append('title', this.title);
                    formData.append('description', this.description);
                    formData.append('amount', this.amount);

                    for (let pair of formData.entries()) {
                        console.log(pair[0] + ', ' + pair[1]);
                    }

                    this.confirmDialog = true

                    axios.post(`${this.$store.state.host}/api/posts/create-need/`, formData, {
                        headers: {
                            // Set your Authorization to 'JWT', not Bearer!!!
                            Authorization: `JWT ${this.$store.state.jwt}`,
                            'Content-Type': 'application/json'
                        },
                        xhrFields: {
                            withCredentials: true
                        }
                    })
                        .then(() => {
                            this.isLoading = false
                            this.sentStatus = 'complete'
                            $(".el-dialog").css({"max-width": "350px"});
                        })
                        .catch(e => {
                            this.isLoading = false
                            this.sentStatus = 'error'
                            $(".el-dialog").css({"max-width": "350px"});
                        })


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
        border-radius: 10px;
    }

    .profile-pic {
        object-fit: contain;
        height: 100%;
        width: 99.8%;
    }
</style>