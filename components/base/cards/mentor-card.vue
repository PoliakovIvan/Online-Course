<script setup>
defineProps({
    itemData: {
        type: Object,
        required: true
    }
})
</script>

<template>
    <div class="mentor">
        <div class="mentor__image">
            <img :src="itemData.image" :alt="itemData.name">
            <div class="mentor__gradient"></div>
        </div>
        <div class="mentor__info">
            <h3 class="mentor__name">{{ itemData.name }}</h3>
            <div class="mentor__position">{{ itemData.position }}</div>
        </div>
    </div>
</template>