<script setup lang="ts">
import Main from "@/components/Main.vue";
</script>

<template>
  <div class="container" >
    <Main  class="container"></Main>
  </div>
</template>
<style>
#all {
  background: linear-gradient(-45deg, #495057, #ccc5b9, #d6ccc2, #edede9);
  background-size: 1500vw 1500vh;
  animation: gradient 6s ease infinite;
}

@keyframes gradient {
  0% {
    background-position: 0 50%;
  }

  50% {
    background-position: 100% 50%;
  }

  100% {
    background-position: 0 50%;
  }
}
</style>
