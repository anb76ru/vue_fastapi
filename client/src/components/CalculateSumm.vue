<template>
    {{ helloWorld }}  

    <q-input v-model="firstValue" label="Введите первое число" style="max-width: 300px;"></q-input>
    <q-input v-model="secondValue" label="Введите первое число" style="max-width: 300px;"></q-input>

    <div style="padding: 10px;">
      <q-btn label="Вычислить сумму" @click="calculate"></q-btn>
    </div>


    <div>
      <q-label>{{ result }}</q-label>
    </div>


</template>
  
<script>
    import axios from "axios"
    export default {
      data() {
        return {
          helloWorld: "hw",
          result: 0,
          firstValue: null,
          secondValue: null
        }
      },
      methods: {
        getJson() {
          axios.get('/api/calculate')
            .then(res => (this.helloWorld = res.data.message))
        },
        calculate() {
            //this.firstValue = this.getFirstValue();
            //this.secondValue = this.getSecondValue()
            // axios.defaults.baseURL = "http://localhost:8000"
            // axios.post("/get-sum", 
            //            {"num1": this.firstValue, "num2": this.secondValue},
            //            {headers: { 'content-type': 'application/json' }})
            //   .then(res => (this.result = res))
            fetch("/api/get-sum", {
              method: "POST",
              body: JSON.stringify({
                "num1": Number(this.firstValue),
                "num2": Number(this.secondValue)
              }),
              headers: {
                'Accept': 'application/json',
                "Content-type": "application/json; charset=UTF-8",
              }
            })
              .then(res => res.json())
              .then(json => this.result = json.result)
        },
        getFirstValue(value='0'){
          this.firstValue = value
        },
        getSecondValue(value='0') {
          this.secondValue = value
        }
      },
      mounted() {
        this.helloWorld = this.getJson()
      }
    }
</script>