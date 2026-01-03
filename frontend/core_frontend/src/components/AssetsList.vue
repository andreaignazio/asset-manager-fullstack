<script setup>
    import {ref, onMounted} from 'vue'
    import AssetCard from '@/components/AssetCard.vue'

    const assets = ref([])
    
    async function fetch_assets(){
        const response = await fetch('http://127.0.0.1:8000/core/assets/')
        const data = await response.json()
        assets.value = data
    }
    onMounted(() => {
  fetch_assets()
})

    console.log(assets.value)

</script>

<template>
    
    
    <div class="grid">
        <AssetCard v-for="item in assets" :key="item.id" :asset="item"/>
    </div>

</template>

<style scoped>

</style>