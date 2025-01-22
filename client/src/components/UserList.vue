<template>
    <div class="label">Список пользователей</div>
    <div class="q-pa-md example-row-equal-width">
        <q-list>
            <template v-for="(user, index) in userList" :key=index>
                <q-item class="q-pa-md example-row-equal-width">
                    <div class="row">
                        <div class="col-6" style="font-size: 18px;">{{ user.username }}</div>
                        <div class="col-6">{{ user.user_info }}</div>
                    </div>
                </q-item>
            </template>
        </q-list>
    </div>
</template>
  
<script>
    import axios from "axios"
    export default {
      data() {
        return {
          userList: []
        }
      },
      methods: {
        getUserList() {
          axios.get('/api/users')
            .then(res => (this.userList = res.data))
        }
      },
      mounted() {
        this.getUserList()
      }
    }
</script>

<style>
.label {
    font-size: 5vh;
}
</style>