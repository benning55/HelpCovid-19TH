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
                <p class="mb-2 text-sm text-gray">หากไม่มีให้ใส่เครื่องหมายขีด (-)</p>
                <input v-model="email" class="form-control"
                       :class="{'is-invalid':validation.firstError('email')}"
                       placeholder="กรุณาใส่ Email ที่ใช้ในการติดต่อกลับ">
                <div class="invalid-feedback">
                    {{validation.firstError('email')}}
                </div>
            </div>
            <div class="form-group">
                <label>เบอร์โทรศัพท์ที่สามารถติดต่อได้</label>
                <p class="mb-2 text-sm text-green">ระบบจะไม่แสดงอีเมลล์ให้ผู้อื่นเห็น</p>
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
            <div class="flex justify-between my-5">
                <button @click="$router.go(-1)" type="button" class="btn bg-white text-black">ย้อนกลับ</button>
                <button @click="sent" type="button" class="btn bg-green text-white">ส่งความประสงค์จะบริจาคให้เจ้าหน้าที่</button>
            </div>
        </form>
    </div>

</template>

<script>
    import {Validator} from "../main";

    export default {

        data() {
            return {
                fname: '',
                lname: '',
                email: '',
                tel: '',
                amount: ''
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
                    .required("กรุณาระบุหัวข้อ");
            },
            tel(value) {
                return Validator.value(value)
                    .required("กรุณาระบุรายละเอียด")
                    .integer("กรุณาระบุจำนวนเป็นตัวเลข")
                    .length(10,"กรุณาระบุจำนวนเป็นตัวเลขจำนวน 10 หลัก");
            },
            amount(value) {
                return Validator.value(value)
                    .required("กรุณาระบุจำนวน")
                    .integer("กรุณาระบุจำนวนเป็นตัวเลข")
                    .greaterThan(0, "กรุณาระบุจำนวนเป็นตัวเลขที่มีค่ามากกว่า 0")
            },

        },
        methods:{
            sent(){
                this.$validate(["fname", "lname", "email","tel","amount"]);
                if (
                    this.validation.firstError("fname") == null &&
                    this.validation.firstError("lname") == null &&
                    this.validation.firstError("email") == null &&
                    this.validation.firstError("tel") == null &&
                    this.validation.firstError("amount") == null
                ) {
                    let formData = new FormData();
                    formData.append('fname', this.fname);
                    formData.append('lname', this.lname);
                    formData.append('email', this.email);
                    formData.append('tel', this.tel);
                    formData.append('amount', this.amount);

                    for (let pair of formData.entries()) {
                        console.log(pair[0] + ', ' + pair[1]);
                    }
                }
            }
        }
    }
</script>