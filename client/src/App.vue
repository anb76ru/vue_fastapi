<template>
  <div>
    <q-layout>
      <q-drawer show-if-above side="left" bordered :width="210">
        <left-nav></left-nav>
      </q-drawer>
      <q-page-container>
          <router-view/>
      </q-page-container>
    </q-layout>
  </div>
</template>

<script>
  export default {
    }
</script>