<template>
    <div class="container">
        <div class="rounded mt-4">
            <h1>This is an about page</h1>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        data(){
            return{
                // axios.get(`${this.$store.state.host}`)
            }
        }
    }
</script>
