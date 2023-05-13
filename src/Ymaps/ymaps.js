let map = null;

function init() {
  map = new ymaps.Map('map', {
    center: [59.938955, 30.315644],
    zoom: 10,
    controls: ['typeSelector', 'zoomControl']
  });
}

export { init, map }
