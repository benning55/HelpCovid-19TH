<template>
    <div class="Map"/>
</template>

<script>
    import gmapsInit from "../gmaps";

    export default {
        name: 'Map',
        data() {
            return {
                positionHospital: [
                    {
                        id:0,
                        name:"fefef",
                        position: {
                            lat: 13.749274,
                            lng: 100.583502,
                        },
                    },
                    {
                        id:1,
                        name:"fefef",
                        position: {
                            lat: 48.174270,
                            lng: 16.329620,
                        }
                    },
                    {
                        id:2,
                        name:"fefef",
                        position: {
                            lat: 13.766043,
                            lng: 100.524511,
                        }

                    }
                ]
            }
        },
        methods: {},
        async mounted() {
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
                        console.log((marker.getCursor()))
                    } else {
                        map.setZoom(18);
                        map.setCenter(marker.getPosition())
                    }

                };

                const locations = [
                    {
                        position: {
                            lat: 13.749274,
                            lng: 100.583502,
                        },
                    },
                    {
                        position: {
                            lat: 48.174270,
                            lng: 16.329620,
                        }
                    }
                ];

                const markers = this.positionHospital
                    .map((location) => {
                        console.log(location.id)
                        marker.setCursor(`${location.id}`)
                        marker.setAnimation(google.maps.Animation.BOUNCE);
                        marker.addListener('click', () => markerClickHandler((marker)));
                        return marker
                    })

            } catch (e) {
                console.error(e)
            }
        }
    }
</script>

<style scoped>
    .Map {
        width: 100%;
        height: 50vh;
    }
</style>