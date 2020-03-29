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
                <label v-if="validation.firstError('imageData')" class="text-red">{{validation.firstError('imageData')}}</label>
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
    </div>
</template>

<script>
    import {Validator} from "../main";

    export default {
        data() {
            return {
                fname: '',
                lname: '',
                amount: '',
                imageData: null,
                profileImageURL: null,
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
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            sent() {
                this.$validate(["fname", "lname", "amount","imageData"]);
                if (
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null &&
                    this.validation.firstError("amount") == null &&
                    this.validation.firstError("imageData") == null
                ) {
                    let formData = new FormData();
                    formData.append('fname', this.fname);
                    formData.append('lname', this.lname);
                    formData.append('amount', this.amount);
                    formData.append('imageData', this.imageData);

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