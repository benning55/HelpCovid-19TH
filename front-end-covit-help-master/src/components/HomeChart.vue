<!--<template>-->
<!--    <div class="small">-->
<!--        {{datacollection}}-->
<!--    </div>-->
<!--</template>-->

<script>
    import axios from 'axios'
    import {Bar} from 'vue-chartjs'

    export default {
        extends: Bar,
        data() {
            return {
                datacollection: {
                    labels: ['Redxx', 'Blue', 'Yellow', 'Green'],
                    datasets: [{
                        maxBarThickness: 100,
                        data: [0, 0, 0, 0],
                        backgroundColor: [
                            'rgba(255, 99, 132, 1)',
                            'rgba(54, 162, 235, 1)',
                            'rgba(255, 206, 86, 1)',
                            'rgba(75, 192, 192, 1)',
                        ],
                    }]
                },
                options: {
                    scales: {
                        yAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            gridLines: {
                                display: true
                            }
                        }],
                        xAxes: [{
                            ticks: {
                                beginAtZero: true
                            },
                            gridLines: {
                                display: false
                            }
                        }]
                    },
                    legend: {
                        display: false
                    },
                    tooltips: {
                        enabled: true,
                        mode: 'single',
                        callbacks: {
                            label: function (tooltipItems) {
                                return tooltipItems.yLabel + " หน่วย";
                            }
                        }
                    },
                    responsive: true,
                    maintainAspectRatio: false,
                    height: 200
                },
            }
        },
        created() {
            this.getChat()
        },
        methods: {
            getChat() {
                axios.get(`${this.$store.state.host}/api/util/chart/`)
                    .then(res => {
                        console.log(res.data.data)
                        this.datacollection.labels = res.data.label
                        this.datacollection.datasets[0].data = res.data.data
                        let sum = res.data.data.reduce((a, b) => a + b, 0)
                        this.renderChart(this.datacollection, this.options)
                        this.$emit("data", [res.data.total_money,sum])
                    })
                    .catch(e => {
                        this.$message({
                            showClose: true,
                            message: 'มีข้อผิดพลาดเกิดขึ้น' + 'ในการในการดึงข้อมูลผู้บริจาคสิ่งของ' + ' Error : ' + e.response.status,
                            type: 'error',
                            duration: 10
                        });
                    })
            }
        },
        // mounted() {
        //     // this.chartData is created in the mixin
        //     this.renderChart(this.datacollection, this.options)
        // },
    }
</script>

<style>
    .small {
        max-width: 600px;
        margin: 150px auto;
    }
</style>