<template>
  <div class="menu">
      <div class="studyPlaceSelection">
          <p>Выберите место учебы:</p>
          <CustomSelect
            :universities="universities"
            @changeSelect="changeUniversity"
          >
          </CustomSelect>
      </div>
      <CustomInput @change="findPlace()"></CustomInput>
      <div class="filterBtns">
          <CustomFilterBtn @click="addMarks(item.id)" v-for="item in menuList"
            :imgPath="item.imgPath"
            :description="item.description"
            :backgroundColor="item.backgroundColor"
          >
          </CustomFilterBtn>
      </div>
  </div>
</template>

<script>
import CustomInput from "./ui/CustomInput.vue";
import CustomSelect from "./ui/CustomSelect.vue";
import CustomFilterBtn from "./ui/CustomFilterBtn.vue";
import { mapActions, mapState, mapGetters } from "vuex";
import { map } from "@/Ymaps/ymaps";

export default {
    name: 'MenuLeft',
    components: {
        CustomInput,
        CustomSelect,
        CustomFilterBtn,
    },
    data() {
        return {
            menuList: [ 
                {
                    id: 'ВУЗ',
                    imgPath: '/menuImages/universImg.svg',
                    description: 'ВУЗы',
                    backgroundColor: 'rgb(183, 116, 245)',
                },
                {
                    id: "Коворкинг",
                    imgPath: '/menuImages/kovorkingImg.svg',
                    description: 'Коворкинги',
                    backgroundColor: 'rgb(253, 253, 22)',
                },
                {
                    id: "Библиотека",
                    imgPath: '/menuImages/biblioteki.svg',
                    description: 'Библиотеки',
                    backgroundColor: 'rgb(105, 250, 255)',
                },
                {
                    id: "Кафе",
                    imgPath: '/menuImages/kafe.svg',
                    description: 'Кафе',
                    backgroundColor: 'rgb(235, 125, 0)',
                },
                {
                    id: "Музей",
                    imgPath: '/menuImages/museum.svg',
                    description: 'Музеи',
                    backgroundColor: 'rgb(40, 220, 0)',
                }
            ],
            
        }
    },
    mounted() {
        this.loadUniversities();
    },
    computed: {
        ...mapGetters({
            coords: "getCoords"
        }),
        ...mapState({
            universities: "universities",
            marksConfigs: "marksConfigs",
        })
    },
    methods: {
      ...mapActions({
        addMarks: 'addMarksFromType',
        loadUniversities: 'loadUniversities',
        loadCoordsByAdress: "loadCoordsByAdress"
      }),
      async changeUniversity(universityName) {
        if (map.geoObjects.getLength()) {
            map.geoObjects.removeAll();
        }
        
        let university = this.universities.find(item => item.name === universityName);
        let addressArray = university.address.split(';');

        await this.loadCoordsByAdress(addressArray)

        for (let i = 0; i < this.coords.length; i++) {
            map.geoObjects.add(new ymaps.Placemark(this.coords[i], {
                balloonContentHeader: university.name,
                balloonContentBody: addressArray[i],
            }, this.marksConfigs.find(config => config.id === "ownUniversity").config));
        }
      },
      
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.menu, .filterBtns, .studyPlaceSelection {
    display: flex;
}

  .menu {
      flex-direction: column;
      padding: 10px;
  }

  .filterBtns {
      display: flex;
      flex-wrap: wrap;
      gap: 25px;
  }

  .studyPlaceSelection {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      margin: 5px;
      font-size: 0.7em;
      font-weight: 700;
  }
</style>
