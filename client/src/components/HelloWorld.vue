<template>
    {{ helloWorld }}
    <q-input></q-input>
</template>
  
<script>
    import axios from "axios"
    export default {
      data() {
        return {
          helloWorld: "hw"
        }
      },
      methods: {
        getJson() {
          axios.get('/api/hw')
            .then(res => (this.helloWorld = res.data.message))
        }
      },
      mounted() {
        this.helloWorld = this.getJson()
      }
    }
</script>