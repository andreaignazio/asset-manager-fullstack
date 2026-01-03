<script setup>
    import {ref, watch} from 'vue'

    const props = defineProps({
        editingAsset: {
            type: Object,
            default: null   
        }
    })

    const emit = defineEmits(['create-asset', 'cancel-edit'])
    const name = ref("")
    const polys = ref(0)

    const handleSubmit = () =>{
        const payload = {
            name: name.value,
            poly_count: polys.value,
        }
        emit('create-asset', payload)
        name.value = ""
        polys.value = 0  
    }

    watch(
        () => props.editingAsset, (newAsset)=> {
            if(newAsset) {
                name.value = newAsset.name
                polys.value = newAsset.poly_count
            } else {
                name.value = ""
                polys.value = 0
            }
        }, {immediate: true}
    )

</script>
<template>
    <div class="form-container" :class="{'edit-mode' : editingAsset}">
        <h3>{{editingAsset ? 'Edit Asset' : 'New Asset'}}</h3>
        <div class ="input-group">
            <input v-model="name" type = "text" placeholder="Name of the asset"/>
            <input v-model="polys" type = "number" placeholder="Number of polys"/>
            <button @click="handleSubmit">{{editingAsset ? 'Save' : 'Add'}}</button>
            <button 
                v-if="editingAsset" 
                @click="emit('cancel-edit')" 
                class="cancel-btn">
            ❌</button>
        </div>
    </div>
</template>
<style scoped>
    .form-container {
        background: #f0f0f0;
        color: black;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 5px solid #42b883;
    }
    .edit-mode {
        border-left-color: #ffa500; /* orange */
        background: #fff8e1;
    }
    .input-group{
        display: flex;
        gap: 10px;
    }
    input {
        padding:8px;
        border: 1px solid #ccc;
        border-radius: 4px;
    }
    button {
        background: #42b883;
        color: white;
        border:none;
        padding: 8px 16px;
        border-radius: 4px;
        cursor: pointer;
        font-weight: bold;
    }

  
</style>