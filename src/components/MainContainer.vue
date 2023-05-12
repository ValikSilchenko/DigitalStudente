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
    height: 80vh;
    font-size: 20px;
  }
  .menu_left {
    background-color: aqua;
      width: 350px;
  }
  .ya_map {
    border-radius: 10px;
    display: flex;
  }
</style>