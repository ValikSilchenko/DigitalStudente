import { createStore } from 'vuex'
import { map } from '../Ymaps/ymaps.js'

export default createStore({
  state: {
    isMapLoaded: false,
    marksConfigs: [
      {
        id: 'universities', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/purpleMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      }
    ]
  },
  mutations: {
  },
  actions: {
    addMarks({ state, commit }, btnId) {
        if (!map) {
          return
        };

        let universitiesCollection = new ymaps.GeoObjectCollection(null);
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
        
        let config = state.marksConfigs.find(item => item.id === btnId).config;
        
        for(let place of universitiesArr) {
          universitiesCollection.add(new ymaps.Placemark(place.coordinates, {
            balloonContent: place.name
          }, config))
        }
        
        map.geoObjects.add(universitiesCollection);
    },
  },
})
