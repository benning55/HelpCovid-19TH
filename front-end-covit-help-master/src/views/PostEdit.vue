<template>
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
        <button @click="createPost" type="button" class="btn bg-green text-white">ลงรับบริจาค</button>
    </div>
</template>

<script>
    import {Validator} from "../main";

    export default {
        data() {
            return {
                title: '',
                description: '',
                amount: 1,
                imageData: null,
                profileImageURL: null
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
                    let formData = new FormData();
                    formData.append('pic', this.imageData);
                    formData.append('title', this.title);
                    formData.append('description', this.description);
                    formData.append('amount', this.amount);

                    for (let pair of formData.entries()) {
                        console.log(pair[0] + ', ' + pair[1]);
                    }
                }
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