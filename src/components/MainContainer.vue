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
.main_container, .ya_map {
    display: flex;
}
  .main_container {
    height: 80vh;
    font-size: 20px;
  }
  .menu_left {
    background-color: white;
      width: 350px;
      border-radius: 5px;
      border: 1px solid white;
      margin-right: 10px;
  }
  .ya_map {
    border-radius: 10px;
  }
</style>