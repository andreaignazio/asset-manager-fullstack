<script setup>
    const props = defineProps({
        asset : Object
    })
    const emit = defineEmits(['delete-asset','edit-asset'])
    const handleDelete = () => {
        const payload = {
            id : props.asset.id
        }
        emit('delete-asset', payload)
    }
    
</script>
<template>
    <div class ="card">
        <div class="card-header">
            <h2>{{ asset.name }}</h2>
            <div class="actions">
                <button class = "icon-btn edit-btn"
                @click="handleDelete">🗑️</button>
                <button 
                class = "icon-btn edit-btn"
                @click="emit('edit-asset',  props.asset)">
                ✏️</button>
            </div>
        </div>
        <p>Poligons: <strong>{{ asset.poly_count }}</strong></p>
        <p class="author">Autore: {{ asset.author ? asset.author : "Anonymus" }}</p> 
    </div>

</template>
<style scoped>
   .card {
    background: #2a2a2a;
    color: white;
    padding: 15px;
    border-radius: 8px;
    border: 1px solid #444;
   } 

   .card:hover{
    transform: translate( -5px);
    border-color: #42b883;
   }
   .card-header {
    display: flex;
    justify-content: space-between;
    align-items: start;
   }
   .actions {
    display: flex;
    gap: 5px;
   }

   .author {
    font-size: 0.8em;
    color: #888;
    margin-top: 10px;
   }
   .icon-btn {
    background: transparent;
    border: none;
    cursor: pointer;
    font-size: 1.2em;
    padding: 0;
    transition: transform 0.2s;
   }
   .edit-btn:hover { transform: scale(1.2);}
   .delete-btn:hover { transform: scale(1.2);}

</style>