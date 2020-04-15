import {Bar, mixins} from 'vue-chartjs'

const {reactiveProp} = mixins

export default {
    extends: Bar,
    mixins: [reactiveProp],
    data() {
        return {
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
                height: 400
            },
        }
    },
    mounted() {
        // this.chartData is created in the mixin.
        // If you want to pass options please create a local options object
        this.renderChart(this.chartData, this.options)
    }
}