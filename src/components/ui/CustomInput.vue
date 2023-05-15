<template>
    <input 
        type="text" 
        placeholder="Поиск..."
        class="customInput"
        :value="searchString"
        @change="$emit('find', $event.target.value)"
    >
</template>

<script>
export default {
    name: "CustomInput",
    props: {
        searchString: {
            type: String,
        }
    },
    emits: ['find'],
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