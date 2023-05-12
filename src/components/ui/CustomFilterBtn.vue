<template>
    <figure class="customFilterBtn">
        <img src="@/assets/universitiesImg.svg" alt="Universities">
        <figcaption>Библиотки</figcaption>
    </figure>
</template>

<script>
export default {

}
</script>

<style scoped>
.customFilterBtn {
    border: 1px solid black;
    border-radius: 5px;
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 3px;
    width: 75px;
    height: 75px;
    margin: 15px 5px;
    cursor: pointer;
}
.customFilterBtn:hover {
    background-color: aqua;
}

img {
    width: 50px;
    height: 50px;
}

figcaption {
    font-size: 0.6em;
}
</style>