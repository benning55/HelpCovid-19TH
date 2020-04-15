<!--<template>-->
<!--    <bar :chart-data="datacollection"></bar>-->
<!--</template>-->

<!--<script>-->
<!--    import axios from 'axios'-->
<!--    import {Bar} from 'vue-chartjs'-->
<!--    import bar from '../bar.js'-->

<!--    export default {-->
<!--        extends: Bar,-->
<!--        components:{-->
<!--            bar-->
<!--        },-->
<!--        data() {-->
<!--            return {-->
<!--                datacollection: {-->
<!--                    labels: ['Redxx', 'Blue', 'Yellow', 'Green'],-->
<!--                    datasets: [{-->
<!--                        maxBarThickness: 100,-->
<!--                        data: [10, 0, 0, 0],-->
<!--                        backgroundColor: '#005a9b',-->
<!--                    }]-->
<!--                },-->
<!--                options: {-->
<!--                    scales: {-->
<!--                        yAxes: [{-->
<!--                            ticks: {-->
<!--                                beginAtZero: true-->
<!--                            },-->
<!--                            gridLines: {-->
<!--                                display: true-->
<!--                            }-->
<!--                        }],-->
<!--                        xAxes: [{-->
<!--                            ticks: {-->
<!--                                beginAtZero: true-->
<!--                            },-->
<!--                            gridLines: {-->
<!--                                display: false-->
<!--                            }-->
<!--                        }]-->
<!--                    },-->
<!--                    legend: {-->
<!--                        display: false-->
<!--                    },-->
<!--                    tooltips: {-->
<!--                        enabled: true,-->
<!--                        mode: 'single',-->
<!--                        callbacks: {-->
<!--                            label: function (tooltipItems) {-->
<!--                                return tooltipItems.yLabel + " หน่วย";-->
<!--                            }-->
<!--                        }-->
<!--                    },-->
<!--                    responsive: true,-->
<!--                    maintainAspectRatio: false,-->
<!--                    height: 400-->
<!--                },-->
<!--            }-->
<!--        },-->
<!--        // created() {-->
<!--        //     this.getChat()-->
<!--        // },-->
<!--        // methods: {-->
<!--        //     getChat() {-->
<!--        //         axios.get(`${this.$store.state.host}/api/util/chart/`)-->
<!--        //             .then(res => {-->
<!--        //                 console.log(res.data.data)-->
<!--        //                 this.datacollection.labels = res.data.label-->
<!--        //                 this.datacollection.datasets[0].data = res.data.data-->
<!--        //                 let sum = res.data.data.reduce((a, b) => a + b, 0)-->
<!--        //                 this.renderChart(this.datacollection, this.options)-->
<!--        //                 this.$emit("data", [res.data.total_money,sum])-->
<!--        //             })-->
<!--        //             .catch(e => {-->
<!--        //                 this.$message({-->
<!--        //                     showClose: true,-->
<!--        //                     message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,-->
<!--        //                     type: 'error',-->
<!--        //                     duration: 10-->
<!--        //                 });-->
<!--        //             })-->
<!--        //     }-->
<!--        // },-->
<!--    }-->
<!--</script>-->

<!--<style>-->

<!--</style>-->

<template>
    <div class="">
        <line-chart v-if="loaded" style="height: 300px" :chart-data="datacollection"></line-chart>
    </div>
</template>

<script>

    import axios from 'axios'
    import LineChart from '../bar.js'

    export default {
        components: {
            LineChart
        },
        data() {
            return {
                datacollection: null,
                loaded: false
            }
        },
        created() {
            this.getData()
            this.fillData()
        },
        // mounted() {
        //     this.getData()
        // },
        methods: {
            getData() {
                this.loaded = false
                axios.get(`${this.$store.state.host}/api/util/chart/`)
                    .then(res => {
                        this.datacollection.labels = res.data.label
                        this.datacollection.datasets[0].data = res.data.data
                        let sum = res.data.data.reduce((a, b) => a + b, 0)
                        // this.renderChart(this.datacollection, this.options)
                        this.$emit("data", [res.data.total_money, sum])
                        this.loaded = true
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response,
                            type: 'error',
                            duration: 10
                        });
                        this.loaded = true
                    })
            },
            fillData() {
                this.datacollection = {
                    labels: ["ss", "see", "ssz", "seez"],
                    datasets: [{
                        maxBarThickness: 100,
                        data: [90, 30, 50, 70],
                        backgroundColor: '#005a9b',
                    }]
                }
            }
        },
    }
</script>

<style>
    .small {
        max-width: 600px;
        margin: 150px auto;
    }
</style>