<template>
  <main class="main_container">
    <aside class="menu_left"><MenuLeft></MenuLeft></aside>
    <section class="ya_map"><YaMap></YaMap></section>
  </main>
</template>

<script>
  import MenuLeft from './MenuLeft.vue';
  import YaMap from './YaMap.vue';

  export default {
    name: 'MainContainer',
    components: {
      MenuLeft,
      YaMap,
    }
  }
</script>

<style scoped>
.main_container {
    display: flex;
    justify-content: center;
    height: 80vh;
    font-size: 20px;
    flex-grow: 1;
    margin: 0 50px
  }
  .menu_left {
    background-color: rgb(226, 226, 226);
    margin-right: 30px;
    border-radius: 7px;
    flex-basis: 350px;
  }
  .ya_map {
    display: flex;
    flex-grow: 2;
    background-color: aqua;
    border-radius: 10px;
  }
</style>