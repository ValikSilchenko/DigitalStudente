<template>
    <select class="customSelect" @change="$emit('changeSelect', $event.target.value)">
        <option 
            v-for="university in universities"
            :value="university.name"
        >
            {{ university.name }}
        </option>
    </select>
</template>

<script>
export default {
    name: "CustomSelect",
    props: {
        universities: {
            type: Array,
            required: true,
        }
    }
}
</script>

<style scoped>
.customSelect {
    display: block;
    width: 50%;
    padding: 5px;
    border: 2px solid black;
    border-radius: 5px;
}
</style>