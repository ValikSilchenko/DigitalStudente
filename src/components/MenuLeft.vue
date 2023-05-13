<template>
  <div class="menu">
      <div class="studyPlaceSelection">
          <p>Выберите место учебы:</p>
          <CustomSelect />
      </div>
      <CustomInput />
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
import { mapActions } from "vuex";

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
                    id: "Музеи",
                    imgPath: '/menuImages/museum.svg',
                    description: 'Музеи',
                    backgroundColor: 'rgb(40, 220, 0)',
                }
            ],
            
        }
    },
    mounted() {},
    computed: {
    },
    methods: {
      ...mapActions({
        addMarks: 'addMarksFromType',
        createMap: 'createMap',
      }),
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
  }
</style>
