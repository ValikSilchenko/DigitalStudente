<template>
  <div class="menu">
      <div class="studyPlaceSelection">
          <p style="font-size: 0.8em">Выберите место учебы:</p>
          <CustomSelect />
      </div>
      <CustomInput />
      <div class="filterBtns">

      </div>
  </div>
</template>

<script>
import CustomInput from "@/components/ui/CustomInput.vue";
import CustomSelect from "@/components/ui/CustomSelect.vue";

export default {
  name: 'MenuLeft',
    components: {CustomSelect, CustomInput},
    data() {
      return {
          menuList: [ 
            {
              imgPath: 'dit/file',
              description: 'Коворкинги',  
            },

          ]
        }
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
      flex-direction: row;
  }

  .studyPlaceSelection {
      flex-direction: row;
      align-items: center;
      justify-content: space-between;
      margin: 5px;
  }
</style>
