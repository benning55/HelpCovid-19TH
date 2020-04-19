<template>
    <div>


        <div class="container mt-5">
            <h1 class="text-3xl text-center">แก้ไขข้อมูลการรับบริจาค</h1>
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

                {{oldImage == null}}
                <div class="form-group">
                    <label>รูปของโพสต์ เช่น รูปตัวอย่างของที่รับบริจาค</label>
                    <div class="col-12 upload-section">
                        <div class="upload-btn-wrapper w-full">
                            <div class="">
                                <div class="image-cropper border-2 border-dashed border-black text-center">
                                    <!--choose new image-->
                                    <img v-if="imageData!=null"
                                         :src="profileImageURL"
                                         alt="avatar"
                                         class="profile-pic"
                                    />
                                    <!--have old image but not choose new image-->
                                    <img v-if="oldImage!=null"
                                         :src="this.$store.state.host+oldImage"
                                         alt="avatar"
                                         class="profile-pic"
                                    />
                                    <!--no old image-->
                                    <p v-else class="center-y">อัปโหลดรูปภาพที่นี่</p>
                                </div>
                            </div>
                            <input type="file" @change="previewImage" accept="image/*"/>
                        </div>
                    </div>
                </div>


                <div class="form-group">
                    <label class="col-12">จำนวน (หน่วย)</label>
                    <input v-model="amount" class="form-control"
                           type="number"
                           :class="{'is-invalid':validation.firstError('amount')}"
                           placeholder="กรุณาจำนวนที่ต้องการรับบริจาค">
                    <div class="invalid-feedback">
                        {{validation.firstError('amount')}}
                    </div>
                </div>
            </form>
            <button @click="validate" type="button" class="btn bg-green text-white mb-5 hover:bg-hover_blue">
                แก้ไขข้อมูล
            </button>

            <el-dialog title="ยืนยัน" :visible.sync="confirmDialog" @closed="closeModal">
                <section>
                    <!--                        show when complete-->
                    <div v-if="sentStatus == 'complete'" class="h-full flex flex-wrap">
                        <div class="w-full text-center text-green" style="font-size: 6.2rem;padding-bottom: 26px">
                            <i class="far fa-check-circle"></i></div>
                        <p class="pb-5">บันทึกข้อมูลเรีบยร้อย</p>
                        <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button type="primary" @click="$router.go(-1)">กลับไปหน้าหลัก</el-button>
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
                        <p class="mb-12">คุณต้องการแก้ไขข้อมูลหรือไม่</p>
                        <span slot="footer" class="dialog-footer flex justify-between w-full">
                        <el-button @click="confirmDialog = false">ยกเลิก</el-button>
                        <el-button @click="sent" type="primary">แก้ไขข้อมูล</el-button>
                    </span>
                    </div>

                    <Loader v-if="isLoading"/>
                </section>
            </el-dialog>
        </div>
        <Footer/>
    </div>
</template>

<script>
    import axios from 'axios'
    import {Validator} from "../main";
    import Loader from "../components/Loader";
    import Footer from "../components/Footer";

    export default {
        components: {
            Loader,
            Footer
        },
        data() {
            return {
                isLoading: false,
                title: '',
                description: '',
                amount: 1,
                imageData: null,
                profileImageURL: null,
                confirmDialog: false,
                sentStatus: 'none',
                oldImage: ''
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
                    .digit("กรุณาระบุจำนวนเป็นตัวเลข")
                    .greaterThan(0, "กรุณาระบุจำนวนเป็นตัวเลขที่มีค่ามากกว่า 0")
            },

        },
        created() {
            axios.get(`${this.$store.state.host}/api/posts/need/${this.$route.params.id}/`)
                .then(res => {
                    this.title = res.data.data[0].title
                    this.description = res.data.data[0].description
                    this.amount = Math.floor(res.data.data[0].base_amount)
                    this.oldImage = res.data.data[0].picture
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลการรับบิจาคสินของ' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        },
        methods: {
            closeModal() {
                if (this.sentStatus == 'complete') {
                    this.$router.go(-1)
                } else {
                    this.confirmDialog = false
                }
            },
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            validate() {
                this.$validate(["title", "description", "amount"]);
                if (
                    this.validation.firstError("title") == null &&
                    this.validation.firstError("description") == null &&
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
                if (this.imageData != null) {
                    formData.append('picture', this.imageData);
                }
                formData.append('title', this.title);
                formData.append('description', this.description);
                formData.append('base_amount', this.amount);

                axios.put(`${this.$store.state.host}/api/posts/create-need/${this.$route.params.id}/`, formData, {
                    headers: {
                        // Set your Authorization to 'JWT', not Bearer!!!
                        Authorization: `JWT ${this.$store.state.jwt}`,
                        'Content-Type': 'application/json'
                    },
                })
                    .then(() => {
                        this.sentStatus = 'complete'
                        this.isLoading = false

                    })
                    .catch(e => {
                        this.sentStatus = 'error'
                        this.isLoading = false
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