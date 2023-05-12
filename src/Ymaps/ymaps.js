export default function init() {
  const map = new ymaps.Map('map', {
    center: [59.938955, 30.315644],
    zoom: 10,
    controls: []
  });

  let myPlacemark = new ymaps.Placemark([59.971942, 30.324294],{
    balloonContent: 'ЛЭТИ',
  }, {
    iconLayout: 'default#image',
    iconImageHref: '/placeMarks/purpleMark.svg',
    iconImageSize: [55, 55],
    iconImageOffset: [-30, -40]
  })
  map.geoObjects.add(myPlacemark);
}