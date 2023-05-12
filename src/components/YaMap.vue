<template>
  <div class="yandex__map" id="map"></div>
</template>

<script>
  import {map} from "core-js/internals/array-iteration";

  export default {
    mounted() {
      ymaps.ready(() => {
        let map = new ymaps.Map('map', {
          center: [59.938955, 30.315644],
          zoom: 10,
          controls: []
        });
          // let location = ymaps.geolocation.get();
          // location.then(
          //     function(result) {
          //         map.geoObjects.add(result.geoObjects);
          //     },
          //     function(error) {
          //         console.log('Ошибка: ' + error);
          //     }
          // )
      })
    },

  }
</script>

<style scoped>
  .yandex__map {
    border-radius: 5px;
    width: 100%;
  }

</style>