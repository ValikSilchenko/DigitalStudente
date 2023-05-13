<template>
  <div class="yandex__map" id="map"></div>
</template>

<script>
  //import init from '../Ymaps/ymaps.js'

  export default {
    mounted() {
      ymaps.ready(init);
    },
    methods: {
      initMap() {
        const map = new ymaps.Map('map', {
          center: [59.938955, 30.315644],
          zoom: 10,
          controls: []
        });
      },
    }
  }
</script>

<style scoped>
  .yandex__map {
    border-radius: 5px;
    width: 100%;
  }

</style>