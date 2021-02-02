<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
 
    <scratch></scratch>
  </div>
</template>

<script>

import Scratch from './components/scratch.vue'


export default {
  name: 'App',
  components: {
    Scratch,
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
