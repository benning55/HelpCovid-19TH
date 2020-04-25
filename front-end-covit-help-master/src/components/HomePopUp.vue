<template>
    <transition name="fade">
        <div @click.self="close" class="opacity-background w-full h-screen fixed bg-green z-30">
            <div class="center-y bg-white">
                <div class="header h-12 bg-red flex justify-between items-center bg-white">
                    <div class=" text-black text-center m-2 items-center">
                        <div style="display: flex; padding: 5px 0;">
                            <h1 class="ml-2">ยอดเงินบริจาครวม <span class="text-green text-lg font-medium">{{numberWithCommas(total_money)}}</span>
                            บาท</h1>
<!--                        <h1 class="ml-2">ยอดเงินบริจาครวม <span class="text-green text-lg font-medium">{{numberWithCommas(total_money)}}</span>-->
<!--                            บาท</h1>-->
                            <h1 class="ml-2">ยอดสิ่งของบริจาครวม <span class="text-green text-lg font-medium">{{numberWithCommas(total_donate)}}</span>
                                ชิ้น</h1>
                        </div>
                    </div>
                    <div class="text-black text-center m-2">
                        <a @click="close" class="text-xl mr-2"><i class="fas fa-times"></i></a>
                    </div>
                </div>
                <swiper class="swiper" style="height: 90%" :options="swiperOption">
                    <swiper-slide v-for="c in listCarousal" :key="c.id">
                        <img :src="$store.state.host+c.picture" :alt="c.description" class="object-contain"
                             style="background-color: black;height: 72%">
                        <p class="p-2 limitline">{{c.description}}..
                        </p>
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
                total_money: 0,
                total_donate: 0,
                listCarousal: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/util/popup/`)
                .then(res => {
                    this.total_money = res.data.total_money
                    this.total_donate = res.data.total_donate
                    this.listCarousal = res.data.data
                    if (this.listCarousal.length == 0) {
                        this.$emit("close")
                    }
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
            numberWithCommas(x) {
                return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
            },
            close() {
                this.$emit("close")
            }
        }
    }
</script>

<style scoped>
    .limitline {
        display: block;
        text-overflow: ellipsis;
        word-wrap: break-word;
        overflow: hidden;
        max-height: 5.6em;
        line-height: 1.8em;
    }

    .swiper-pagination {
        bottom: 0;
    }

    .center-y {
        margin: 0;
        position: absolute;
        top: 44%;
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
</style>