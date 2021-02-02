<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
 
    <copy-paste></copy-paste>
  </div>
</template>

<script>

import CopyPaste from './components/CopyPaste.vue'

export default {
  name: 'App',
  components: {
    CopyPaste,
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
