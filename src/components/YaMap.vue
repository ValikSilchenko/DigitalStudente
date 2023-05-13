<template>
  <div class="yandex__map" id="map"></div>
</template>

<script>
  import init from '../Ymaps/ymaps.js'
  import { mapActions } from 'vuex';

  export default {
    mounted() {
      this.createMap();
    },
    methods: {
      ...mapActions({
        createMap: 'createMap',
      }), 
    }
  }
</script>

<style scoped>
  .yandex__map {
    border-radius: 5px;
    width: 100%;
  }

</style>