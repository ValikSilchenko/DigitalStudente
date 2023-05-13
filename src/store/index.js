import { createStore } from 'vuex'
const ymaps = window.ymaps

export default createStore({
  state: {
    map: null,
    isMapLoaded: false,
    marksConfigs: [
      {
        id: 'universities', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/aquaMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],
          iconColor: '#ff0000'
        }
      }
    ]
  },
  mutations: {
    SET_MAP(state, { map, flag }) {
      state.map = map;
      state.isMapLoaded = flag;
    },
  },
  actions: {
    createMap({ commit }) {
      ymaps.ready(() => {
        const map = new ymaps.Map('map', {
          center: [59.938955, 30.315644],
          zoom: 10,
          controls: [],
        })
        commit('SET_MAP', {map: map, flag: true } )
      })
    },
    addMarks({ state }) {
      let { map, marksConfigs } = state;
      ymaps.ready(() => {
        if (!state.map) {
          return;
        }

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
  
        let config = state.marksConfigs.find(item => item.id === 'universities').config;
  
        for(let place of universitiesArr) {
          universitiesCollection.add(new ymaps.Placemark(place.coordinates, {
            balloonContent: place.name
          }, config))
        }
  
        state.map.geoObjects.add(universitiesCollection); 
      })
    },
  },
})
