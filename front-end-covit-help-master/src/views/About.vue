<template>
    <div>
        <div class="pad2up"></div>
        <div>
            <img src="https://scontent.fbkk2-7.fna.fbcdn.net/v/t1.0-9/93315091_236529851090631_2716085859987226624_n.jpg?_nc_cat=106&_nc_sid=e007fa&_nc_ohc=uQa9x-nPOpAAX8GerRp&_nc_ht=scontent.fbkk2-7.fna&oh=d1d7fe84207a2dd5e5e22f7790968761&oe=5EBF14D4" alt="" style="border: 1px solid #42a0c5;">
        </div>
        <div class="pad2up"></div>
        <button type="button" class="btn" style="background-color: #42a0c5; color: white">วัตถุประสงค์</button>
        <ul class="pad2up">
            <li>* ตัวกลางในการรวบรวมความต้องการเวชภัณฑ์ของโรงพยาบาลและเหล่าบุคลากรทางการแพทย์ทั่วประเทศในสภาวะสภานการณ์วิกฤตไวรัสในปัจจุบัน</li>
            <li>* ตัวกลางในการระดมเงินทุนบริจาค เวชภัณฑ์บริจาคจากทั่วประเทศเพื่อส่งมอบให้แก่โรงพยาบาลและบุคลากรทางการแพทย์ที่ขาดแคลน</li>
            <li>* ตัวกลางช่วยให้คนไทยทราบถึงความต้องการของโรงพยาบาลและบุคคลากรจากทั่วประเทศเพื่อสามารถช่วยเหลือได้อย่างทั่วถึง</li>
            <li>* ต้องการเป็บเว็บสื่อกลางเพื่อช่วยเหลือสังคมโดยไม่หวังผลตอบแทน</li>
        </ul>
        <div style="background-color: #42a0c5;">
            <div class="pt-2"></div>
            <button type="button" class="btn" style="background-color: white; color: #42a0c5">ทีมงานโครงการ</button>
            <div class="pb-2"></div>
        </div>
<!--        <div class="rounded mt-4 text-center">-->
<!--            <img src="https://scontent.fbkk2-7.fna.fbcdn.net/v/t1.0-9/93315091_236529851090631_2716085859987226624_n.jpg?_nc_cat=106&_nc_sid=e007fa&_nc_ohc=uQa9x-nPOpAAX8GerRp&_nc_ht=scontent.fbkk2-7.fna&oh=d1d7fe84207a2dd5e5e22f7790968761&oe=5EBF14D4" alt="">-->
<!--            <button type="button" class="btn btn-primary">Primary</button>-->
<!--            <h1 class="text-2xl mt-5 mb-3">เกี่ยวกับเว็บไซต์</h1>-->
<!--            <div v-for="data in datas" :key="data.id" class="my-5">-->
<!--                <p>{{data.description}}</p>-->
<!--            </div>-->
<!--            <h2>Benning</h2>-->
<!--        </div>-->
    </div>

</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                datas: ''
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/about-me/`)
                .then(res => {
                    this.datas = res.data.data
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการโหลดข้อมูล' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        }
    }
</script>

<style scoped>
    .pad2up {
        padding: 2em 0;
    }
    ul li {
        color: #42a0c5;
    }
</style>
