<template>
    <input type="text" placeholder="Поиск..." class="customInput">
</template>

<script>
export default {

}
</script>

<style scoped>
.customInput {
    padding: 5px;
    margin: 5px;
    border: 2px solid black;
    border-radius: 5px;
}

.customInput::placeholder {
    font-style: italic;
    color: black;
}
</style>