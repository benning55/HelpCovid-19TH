<template>
    <div class="container">
        <h1 class="text-2xl">บริจาคเงิน</h1>
        <div class="row">
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <CardHospital/>
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <CardHospital/>
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <CardHospital/>
            </div>
            <div class="col-12 col-sm-6 col-md-4 col-lg-3">
                <CardHospital/>
            </div>
        </div>
    </div>
</template>

<script>
    import CardHospital from "../components/CardHospital";

    export default {
        components: {
            CardHospital
        }
    }
</script>