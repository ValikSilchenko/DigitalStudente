<template>
  <div class="menu">
      <div class="studyPlaceSelection">
          <p>Выберите место учебы:</p>
          <CustomSelect />
      </div>
      <CustomInput />
      <div class="filterBtns">
          <CustomFilterBtn v-for="item in menuList"
            :imgPath="item.imgPath"
            :description="item.description"
            :backgroundColor="item.backgroundColor"
          >
          </CustomFilterBtn>
      </div>
  </div>
</template>

<script>
import CustomInput from "@/components/ui/CustomInput.vue";
import CustomSelect from "@/components/ui/CustomSelect.vue";
import CustomFilterBtn from "@/components/ui/CustomFilterBtn.vue";

export default {
  name: 'MenuLeft',
    data() {
      return {
          menuList: [ 
            {
              imgPath: '/menuImages/universImg.svg',
              description: 'ВУЗы',
              backgroundColor: 'rgb(183, 116, 245)',
            },
            {
              imgPath: '/menuImages/kovorkingImg.svg',
              description: 'Коворкинги',
              backgroundColor: 'rgb(253, 253, 22)',
            },
            {
              imgPath: '/menuImages/biblioteki.svg',
              description: 'Библиотеки',
              backgroundColor: 'rgb(105, 250, 255)',
            },
            {
              imgPath: '/menuImages/kafe.svg',
              description: 'Кафе',
              backgroundColor: 'rgb(235, 125, 0)',
            },
          ]
        }
    },
    components: {CustomFilterBtn, CustomSelect, CustomInput},

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
