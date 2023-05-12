<template>
  <div class="main__app"><MainContainer></MainContainer></div>
</template>

<script>
  import MainContainer from './components/MainContainer.vue';

  export default {
    name: 'App',
    components: {
      MainContainer,
    }
  }
</script>

<style>
  body {
    margin: 0;
    padding: 0;
    background-color: rgb(65, 61, 61);
  }
  .main__app {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
</style>
