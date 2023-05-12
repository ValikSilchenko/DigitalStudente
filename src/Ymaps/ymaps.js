export default function init() {
  const map = new ymaps.Map('map', {
    center: [59.938955, 30.315644],
    zoom: 10,
    controls: []
  });

  let universitiesCollection = new ymaps.GeoObjectCollection(null);
  let universitiesMarkConfig = {
    iconLayout: 'default#image',
    iconImageHref: '/placeMarks/purpleSVG.svg',
    iconImageSize: [55, 55],
    iconImageOffset: [-30, -40],
    iconColor: '#ff0000'
  }

  let universitiesArr = [
    {
      name: "ЛЭТИ",
      coordinates: [59.971942, 30.324294],
    },
    {
      name: "СПБГУ",
      coordinates: [59.941636, 30.299563],
    },
    {
      name: "БОНЧ",
      coordinates: [59.902821, 30.489175],
    }
  ];

  for(let place of universitiesArr) {
    universitiesCollection.add(new ymaps.Placemark(place.coordinates, {
      balloonContent: place.name
    }, universitiesMarkConfig))
  }

  // let myPlacemark = new ymaps.Placemark([59.971942, 30.324294],{
  //   balloonContent: 'ЛЭТИ',
  // }, universitiesMarkConfig)

  map.geoObjects.add(universitiesCollection); 
}