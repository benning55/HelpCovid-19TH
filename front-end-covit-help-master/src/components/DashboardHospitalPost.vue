<template>
    <div class="row">
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <CardPost/>
        </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <CardPost/>
        </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <CardPost/>
        </div>
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
            <CardPost/>
        </div>
    </div>
</template>

<script>
    import CardPost from "./CardPost";

    export default {
        components: {
            CardPost
        }
    }
</script>