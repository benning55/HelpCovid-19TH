<template>
    <div class="container mt-5">
        <h1 class="text-3xl text-center">แก้ไขข้อมูลโรงพยาบาล</h1>
        <form>
            <h1 class="text-xl">ข้อมูลส่วนโรงพยาบาล</h1>
            <hr>
            <div class="form-group">
                <label>ชื่อโรงพยาบาล</label>
                <input v-model="title" class="form-control"
                       :class="{'is-invalid':validation.firstError('title')}"
                       placeholder="กรุณาใสชื่อโรงพยาบาล">
                <div class="invalid-feedback">
                    {{validation.firstError('title')}}
                </div>
            </div>
            <div class="form-group">
                <label>ที่อยู่โรงพยาบาล</label>
                <textarea v-model="description" class="form-control"
                          placeholder="กรุณาใส่ที่อยู่โรงพยาบาล"
                          :class="{'is-invalid':validation.firstError('description')}">
                </textarea>
                <div class="invalid-feedback">
                    {{validation.firstError('description')}}
                </div>
            </div>

            <div class="form-group">
                <label>เบอร์โทรศัพท์ที่ใช้ติดต่อ</label>
                <textarea v-model="description" class="form-control"
                          placeholder="กรุณาใส่เบอร์โทรศัพท์ที่ใช้ติดต่อ"
                          :class="{'is-invalid':validation.firstError('description')}">
                </textarea>
                <div class="invalid-feedback">
                    {{validation.firstError('description')}}
                </div>
            </div>

            <div class="form-group">
                <label>รูปของโรงพยาบาล</label>
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

            <h1 class="text-xl">ข้อมูลของเจ้าหน้าที่</h1>
            <hr>

            <div class="form-group">
                <label class="col-12">ชื่อจริง</label>
                <input v-model="amount" class="form-control"
                       :class="{'is-invalid':validation.firstError('amount')}"
                       placeholder="กรุณาใส่ชื่อจริง">
                <div class="invalid-feedback">
                    {{validation.firstError('amount')}}
                </div>
            </div>

            <div class="form-group">
                <label class="col-12">นามสกุล</label>
                <input v-model="amount" class="form-control"
                       :class="{'is-invalid':validation.firstError('amount')}"
                       placeholder="กรุณาใส่นามสกุล">
                <div class="invalid-feedback">
                    {{validation.firstError('amount')}}
                </div>
            </div>
        </form>
        <button @click="createPost" type="button" class="btn bg-green text-white">บันทึกข้อมูล</button>
    </div>
</template>

<script>
    import {Validator} from "../main";

    export default {
        data() {
            return {
                name: '',
                address: '',
                tel: '',
                imageData: null,
                profileImageURL: null,
                fname:'',
                lname:''
            }
        },
        validators: {
            name(value) {
                return Validator.value(value)
                    .required("กรุณาระบุชื่อโรงพยาบาล");
            },
            address(value) {
                return Validator.value(value)
                    .required("กรุณาระบุที่อยู่ของโรงพยาบาล");
            },
            tel(value) {
                return Validator.value(value)
                    .required("กรุณาระบุเบอร์โทรติดต่อ");
            },
            fname(value) {
                return Validator.value(value)
                    .required("กรุณาระบุชื่อเจ้าหน้าที่");
            },
            lname(value) {
                return Validator.value(value)
                    .required("กรุณาระบุนามสกุลเจ้าหน้าที่");
            },

        },
        methods: {
            previewImage(event) {
                this.imageData = event.target.files[0]
                this.profileImageURL = URL.createObjectURL(this.imageData)
            },
            createPost() {
                this.$validate(["name", "address", "tel","fname","lname"]);
                if (
                    this.validation.firstError("name") == null &&
                    this.validation.firstError("address") == null &&
                    this.validation.firstError("tel") == null &&
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null
                ) {
                    let formData = new FormData();
                    formData.append('pic', this.imageData);
                    formData.append('name', this.name);
                    formData.append('address', this.address);
                    formData.append('tel', this.tel);
                    formData.append('fname', this.fname);
                    formData.append('lname', this.lname);

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