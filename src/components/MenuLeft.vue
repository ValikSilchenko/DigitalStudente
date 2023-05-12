<template>
  <div class="menu_left">
      <div class="studyPlaceSelection">
          <p style="font-size: 0.8em">Выберите место учебы:</p>
          <CustomSelect />
      </div>
      <CustomInput />
      <div class="filterBtns">
          <CustomFilterBtn />
      </div>
  </div>
</template>

<script>
import CustomInput from "@/components/ui/CustomInput.vue";
import CustomSelect from "@/components/ui/CustomSelect.vue";
import CustomFilterBtn from "@/components/ui/CustomFilterBtn.vue";

export default {
  name: 'MenuLeft',
    components: {CustomFilterBtn, CustomSelect, CustomInput},

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.menu_left, .filterBtns, .studyPlaceSelection {
    display: flex;
}

  .menu_left {
      flex-direction: column;
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
