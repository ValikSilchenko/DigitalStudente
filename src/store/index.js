import { createStore } from 'vuex'
import { map } from '../Ymaps/ymaps.js'
import axios from 'axios'

export default createStore({
  state: {
    placesArr: [],
    marksConfigs: [
      {
        id: 'Коворкинг', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/yellowMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
      {
        id: 'ВУЗ', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/purpleMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
      {
        id: 'Библиотека', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/aquaMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
      {
        id: 'Кафе', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/orangeMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
      {
        id: 'Музей', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/greenMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
    ]
  },
  mutations: {
  },
  actions: {
    async addMarksFromType({ state, commit }, btnId) {
        if (!map) {
          return
        };

        try {
          console.log(btnId);
          const response = await axios.get(`http://194.87.248.192:8001/point/category/${btnId}`);

          let newCollection = new ymaps.GeoObjectCollection(null);
          state.placesArr = response.data;

          let category = state.marksConfigs.find(item => item.id === btnId);
          let config = category.config;
          console.log(state.placesArr)

          for(let place of state.placesArr) {
            newCollection.add(new ymaps.Placemark((() => {
              if(btnId === 'ВУЗ' || btnId === 'Музей') {
                return place.coords;
              }
              return place.coords.reverse();
            })(), {
              balloonContentHeader: place.name,
              balloonContentBody: place.address,
            }, config))
          };

          map.geoObjects.removeAll();
          map.geoObjects.add(newCollection);

        } catch (e) {
          alert("Ошибка")
        }
    },
  },
})
