<template>
    <div class="Map"/>
</template>

<script>
    import gmapsInit from "../gmaps";
    import axios from "axios";

    export default {
        props: ["position"],
        name: 'Map',
        data() {
            return {
                positionHospital: []
            }
        },
        created() {
            axios.get(`${this.$store.state.host}/api/accounts/location/`)
                .then(async res => {
                    this.positionHospital = res.data.data
                    try {
                        const google = await gmapsInit();
                        const geocoder = new google.maps.Geocoder();
                        const map = new google.maps.Map(this.$el)

                        geocoder.geocode({address: 'Bangkok'}, (results, status) => {
                            if (status !== 'OK' || !results[0]) {
                                throw new Error(status);
                            }

                            map.setCenter(results[0].geometry.location);
                            map.fitBounds(results[0].geometry.viewport);
                            map.setZoom(6);
                        });

                        const markerClickHandler = (marker) => {
                            if (map.getZoom() >= 18) {
                                marker.setAnimation(google.maps.Animation.BOUNCE);
                                this.$router.push({
                                    name: 'DashboardHospital',
                                    params: {id: parseInt(marker.getCursor())}
                                })
                            } else {
                                map.setZoom(18);
                                marker.setAnimation(google.maps.Animation.BOUNCE);
                                map.setCenter(marker.getPosition())
                            }
                        };

                        const markers = this.positionHospital
                            .map((location) => {
                                const marker = new google.maps.Marker({...location, map});
                                const image = {
                                    url: 'https://i.imgur.com/s1l9Ogh.png',
                                    size: new google.maps.Size(35, 35),
                                    scaledSize: new google.maps.Size(28, 35),
                                    origin: new google.maps.Point(0, 0),
                                    anchor: new google.maps.Point(14, 35)
                                };
                                marker.setIcon(image)
                                marker.setAnimation(google.maps.Animation.BOUNCE);
                                marker.setCursor(`${location.id}`)

                                marker.addListener('click', () => markerClickHandler((marker)));
                                return marker
                            })

                    } catch (e) {
                        console.error(e)
                    }
                })
                .catch(e => {
                    console.log(e)
                })
        },
        methods: {},
        async mounted() {

        },
        watch: {
            position() {
                if (this.position == null) {
                    console.log("null")
                } else {
                    console.log(this.position)
                }
            }
        }
    }
</script>

<style scoped>
    .Map {
        width: 100%;
        height: 80vh;
        border-radius: 10px;
        -webkit-box-shadow: 4px 2px 47px -30px rgba(0, 0, 0, 0.75);
        -moz-box-shadow: 4px 2px 47px -30px rgba(0, 0, 0, 0.75);
        box-shadow: 4px 2px 47px -30px rgba(0, 0, 0, 0.75);
    }
</style>