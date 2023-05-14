import { createStore } from 'vuex'
import { map } from '../Ymaps/ymaps.js'
import axios from 'axios'

export default createStore({
  state: {
    universities: [],
    placesArr: [],
    coords: [],
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
      {
        id: 'ownUniversity', 
        config: {
          iconLayout: 'default#image',
          iconImageHref: '/placeMarks/whiteMark.svg',
          iconImageSize: [55, 55],
          iconImageOffset: [-30, -40],  
        }
      },
    ]
  },
  getters: {
    getCoords(state) {
      return state.coords
    }
  },
  mutations: {
    SET_COORDS(state, coords) {
      state.coords = coords;
    }
  },
  actions: {
    async addMarksFromType({ state, commit }, btnId) {
        if (!map) {
          return
        };

        try {
          const response = await axios.get(`http://194.87.248.192:8001/point/category/${btnId}`);
          let newCollection = new ymaps.GeoObjectCollection(null);
          state.placesArr = response.data;

          let config = state.marksConfigs.find(item => item.id === btnId).config;

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
        } catch(e) {
          alert("Ошибка")
        }
    },
    async loadUniversities({ state }) {
      try {
        const response = await axios.get(`http://194.87.248.192:8001/point/category/ВУЗ`);
        state.universities = response.data.sort((universityFirst, universitySecond) => universityFirst.name.localeCompare(universitySecond.name));
      } catch(e) {
        alert("Не удалось загрузить университеты")
      }
    },
    async loadCoordsByAdress({ state, commit }, addressArray) {
      state.coords = [];
      for (let address of addressArray) {
        try {
          const geocoder = await axios.get(`https://geocode-maps.yandex.ru/1.x/?format=json&apikey=ae41d663-6a01-4379-a21a-0eb098b48a57&geocode=${address}`);
          let featureMember = geocoder.data.response.GeoObjectCollection.featureMember;
          state.coords.push(featureMember[0].GeoObject.Point.pos.split(' ').reverse());
          commit("SET_COORDS", state.coords)
        } catch {
          alert("Ошибка геокодирования")
        }
      }
    }
  },
})
