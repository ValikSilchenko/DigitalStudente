import { createStore } from 'vuex'

export default createStore({
  state: {
    map: null,
  },
  getters: {
  },
  mutations: {
    CREATE_MAP(state) {
      state.map = ymaps.Map('map', {
        center: [59.938955, 30.315644],
        zoom: 10,
        controls: []
      });
    }
  },
  actions: {
    createMap({state, commit}) {
      
    }
  },
  modules: {
  }
})
