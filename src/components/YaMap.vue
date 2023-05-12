<template>
  <div class="yandex__map" id="map"></div>
</template>

<script>
  export default {
    mounted() {
      ymaps.ready(() => {
        const map = new ymaps.Map('map', {
          center: [55.76, 37.64],
          zoom: 10
        });
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