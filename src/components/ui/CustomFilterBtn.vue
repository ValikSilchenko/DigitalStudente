<template>
    <figure :class="['customFilterBtn']" :style="colorImg">
        <img :src="imgPath" :alt="description">
        <figcaption>{{ description }}</figcaption>
    </figure>
</template>

<script>
    export default {
        name: 'CustomFilterBtn',
        props: {
            imgPath: {
                type: String,
                required: true,
            },
            description: {
                type: String,
                required: true,
            },
            backgroundColor:  {
                type: String,
                required: true
            }
        },
        computed: {
            colorImg() {
                return {
                    'background-color': this.backgroundColor,
                }
            }
        },
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
    background-color: transparent;
}
.customFilterBtn:hover {
    background-color: rgb(227, 227, 228) !important;
}

img {
    width: 50px;
    height: 50px;
}

figcaption {
    font-size: 0.7em;
    font-weight: 400;
}
</style>