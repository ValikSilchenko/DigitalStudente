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
    height: 800px;
    font-size: 20px;
    margin: 50px 25px;
  }
  .menu_left {
    background-color: aqua;
  }
  .ya_map {
    background-color: green;
    border-radius: 10px;
  }
</style>