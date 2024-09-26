<template>
  <div>Time: {{ getTime() }}</div>
</template>


<script setup>


var now;
function getTime() {
  now = new Date().toLocaleTimeString();
  return now;
}


module.exports = getTime;
</script>


<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>