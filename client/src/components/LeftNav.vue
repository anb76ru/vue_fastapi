<template>
    <div class="left-nav">
        <q-list>
            <template v-for="(menuItem, index) in menuList" :key="index">
                <!-- <q-item clickable :active="visible===menuItem.label" active-class="router-link-active" v-ripple @click="visible=menuItem.label"> -->
                <q-item :clickable="menuItem.label" :to="{name: menuItem.name}" v-ripple active-class="router-link-active">
                  <q-item-section avatar>
                  <q-icon :name="menuItem.icon" />
                  </q-item-section>
                  <q-item-section>
                  {{ menuItem.label }}
                  </q-item-section>
                  <i class="q-icon fas fa-users"></i>

              </q-item>
            </template>
        </q-list>
    </div>
  </template>
  
  <script>
import { ref } from 'vue'
  
  const menuList = [
    {
      icon: 'inbox',
      label: 'HelloWorld',
      name: 'hw'
    },
    {
      icon: 'calculate',
      label: 'Calculate',
      name: 'calculate'
    },
    {
      icon: 'fas fa-users',
      label: 'Users',
      name: 'users'
    }
  
  ]
  
  export default {
    setup () {
      return {
        drawer: ref(false),
        menuList
      }
    }, 
    data () {
      return {
        visible: '',
      }
    },     
    computed: {
      owl(){
        return true;
      }
    }
  }
  </script>
<style>
.left-nav{
    background-color: #2d3e50;
    height: 100vh;
    color: aliceblue;
}
.router-link-active {
  background-color: rgb(71, 148, 196);
}
</style>