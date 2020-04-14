<template>
    <transition name="fade">
        <div @click.self="close" class="opacity-background w-full h-screen fixed bg-green z-30">
            <div class="center-y bg-white">
                <div class="header h-12 bg-red flex justify-between items-center bg-white">
                    <div class=" text-black text-center m-2 flex items-center">
                        <h1 class="ml-2">ยอดเงินบริจาค <a class="text-green">{{total_money}}</a> บาท</h1>
                    </div>
                    <div class="text-black text-center m-2">
                        <a @click="close" class="text-xl mr-2"><i class="fas fa-times"></i></a>
                    </div>
                </div>
                <swiper class="swiper" style="height: 90%" :options="swiperOption">
                    <swiper-slide v-for="c in listCarousal" :key="c.id">
                        <img :src="$store.state.host+c.picture" alt="description" class="object-cover h-100">
                    </swiper-slide>
<!--                    <swiper-slide>-->
<!--                        <img src="../assets/logo.png" class="object-cover h-100">-->
<!--                    </swiper-slide>-->
                    <div class="swiper-pagination" slot="pagination"></div>
                    <div class="swiper-button-prev" slot="button-prev"></div>
                    <div class="swiper-button-next" slot="button-next"></div>
                </swiper>
            </div>
        </div>
    </transition>
</template>

<script>
    import axios from 'axios'

    export default {
        data() {
            return {
                swiperOption: {
                    pagination: {
                        el: '.swiper-pagination',
                        type: 'fraction'
                    },
                    navigation: {
                        nextEl: '.swiper-button-next',
                        prevEl: '.swiper-button-prev'
                    }
                },
                total_money:0,
                listCarousal:[]
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/util/popup/`)
                .then(res => {
                    this.total_money = res.data.total_money
                    this.listCarousal = res.data.data
                })
                .catch(e => {
                    this.$message({
                        showClose: true,
                        message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                        type: 'error',
                        duration: 10
                    });
                })
        },
        methods: {
            close() {
                this.$emit("close")
            }
        }
    }
</script>

<style scoped>

    .center-y {
        margin: 0;
        position: absolute;
        top: 47%;
        left: 50%;
        -ms-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
        max-width: 500px;
        width: 90%;
        height: 80%;
        border-radius: 10px;
    }

    .opacity-background {
        background-color: rgba(0, 0, 0, .5);
    }

    .header {
        border-radius: 10px 10px 0px 0px;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .5s;
    }

    .fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */
    {
        opacity: 0;
    }

    .swiper-button-prev, .swiper-container-rtl {
        background-image: url("data:image/svg+xml;charset=utf-8,<svg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%2027%2044'><path%20d%3D'M0%2C22L22%2C0l2.1%2C2.1L4.2%2C22l19.9%2C19.9L22%2C44L0%2C22L0%2C22L0%2C22z'%20fill%3D'%23FFFFFF'%2F><%2Fsvg>");
        right: auto;
        left: 10px;
    }

    .swiper-button-next, .swiper-container-rtl {
        background-image: url("data:image/svg+xml;charset=utf-8,<svg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%2027%2044'><path%20d%3D'M27%2C22L27%2C22L5%2C44l-2.1-2.1L22.8%2C22L2.9%2C2.1L5%2C0L27%2C22L27%2C22z'%20fill%3D'%23FFFFFF'%2F><%2Fsvg>");
        right: 10px;
        left: auto;
    }

    .swiper-button-next {
        position: absolute;
        width: 27px;
        height: 44px;
        margin-top: -22px;
        z-index: 10;
        cursor: pointer;
        background-size: 17px 44px;
        background-position: center;
        background-repeat: no-repeat;
    }

    .swiper-button-prev {
        position: absolute;
        width: 27px;
        height: 44px;
        margin-top: -22px;
        z-index: 10;
        cursor: pointer;
        background-size: 17px 44px;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>