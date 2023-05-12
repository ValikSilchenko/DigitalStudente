<template>
  <div class="yandex__map" id="map"></div>
</template>

<script>
  import init from '../Ymaps/ymaps.js'

  export default {
    mounted() {
      ymaps.ready(init);
    },

  }
</script>

<style scoped>
  .yandex__map {
    border-radius: 5px;
    width: 100%;
  }

</style>