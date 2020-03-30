<template>
    <div class="Map"/>
</template>

<script>
    import gmapsInit from "../gmaps";
    export default {
        name: 'Map',
        data() {
            return {

            }
        },
        methods: {
        },
        async mounted(){
            try {
                const google =  await gmapsInit();
                const geocoder = new google.maps.Geocoder();
                const map = new google.maps.Map(this.$el)

                geocoder.geocode({ address: 'Bangkok' }, (results, status) => {
                    if (status !== 'OK' || !results[0]) {
                        throw new Error(status);
                    }

                    map.setCenter(results[0].geometry.location);
                    map.fitBounds(results[0].geometry.viewport);
                    map.setZoom(6);
                });

                const markerClickHandler = (marker) => {
                  map.setZoom(18);
                  map.setCenter(marker.getPosition())
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

                const markers = locations
                    .map((location) => {
                        const marker = new google.maps.Marker({ ...location, map });
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