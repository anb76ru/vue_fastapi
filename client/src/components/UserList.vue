<template>
    <div class="label" style="display: inline;">Список пользователей</div>
    <q-btn style="margin-left: 20px; background-color: #0b0;">Добавить</q-btn>

    <q-input 
      bottom-slots v-model="searchText" 
      label="Поиск пользователя" 
      counter maxlength="20" 
      :dense="dense"
      @update:model-value="searchUsers"
      style="max-width: 300px;"
      >
        <template v-slot:append>
          <q-icon v-show="searchText !== ''" name="close" @click="clearSearch" class="cursor-pointer" />
          <q-icon name="search" @click="searchUsers"/>
        </template>
    </q-input>

    <q-item style="background-color: lightblue;">
      <q-item-section class="col-1 text-bold text-">
      Порядковый номер
    </q-item-section>
      <q-item-section class="col-6 text-bold text-center">
      Имя пользователя
    </q-item-section>
    <q-item-section class="col-6 text-bold text-center">
      Увлечения
    </q-item-section>
    </q-item>
    <q-separator/>

    <div v-if="userList.length">
      <q-item v-for="(user, index) in userList" :key=index class="text-center">
        <q-item-section class="col-1">
          {{ index+1 }}
        </q-item-section>
        <q-item-section class="col-6">
          <div  style="font-size: 18px;">{{ user.username }}</div>
        </q-item-section>
        <q-item-section class="col-6">
          <div>{{ user.user_info }}</div>
        </q-item-section>
      </q-item>
    </div>
    <div v-else> Ни чего не найде </div>
</template>
  
<script>
    import axios from "axios"
    export default {
      data() {
        return {
          userList: [],
          searchText: ''
        }
      },
      created() {
        this.searchUsers()
      },
      methods: {
        async getUserList() {
          await axios.get('/api/users')
            .then(res => (this.userList = res.data))
            return this.userList
        },
        searchUsers() {
          if (this.searchText) {
            axios.post('/api/search-users', {"username": this.searchText})
            .then(res => (this.userList = res.data))
            } else {
              this.getUserList()
            }
        },
        clearSearch() {
          this.searchText = '',
          this.getUserList()
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