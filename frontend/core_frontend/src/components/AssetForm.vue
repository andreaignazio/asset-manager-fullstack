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


    const selectedImage = ref(null)
    const imageFileId = 'image-input'
    const selectedFile = ref(null)
    const modelFileId = 'file-input'

    const handleSubmit = () =>{
        const payload = {
            name: name.value,
            poly_count: polys.value,
            image: selectedImage.value,
            asset_file: selectedFile.value
        }
        emit('create-asset', payload)
        if(!props.editingAsset){
            name.value = ""
            polys.value = 0 
            selectedImage.value = null
            selectedFile.value = null
            document.getElementById(imageFileId).value = ''
            document.getElementById(modelFileId).value = ''

        }
         
    }

    watch(
        () => props.editingAsset, (newAsset)=> {
            if(newAsset) {
                name.value = newAsset.name
                polys.value = newAsset.poly_count
                selectedImage.value = null
                selectedFile.value = null
            } else {
                name.value = ""
                polys.value = 0
                selectedImage.value = null
                selectedFile.value = null
            }
        }
        , {immediate: true}
    )

    const handleImageSelect = (event) => {
        selectedImage.value = event.target.files[0]
    }
    const handleFileSelect = (event) => {
        selectedFile.value = event.target.files[0]
    }

</script>

<template>
    <div class="form-container" :class="{'edit-mode' : editingAsset}">
        <h3>{{editingAsset ? 'Edit Asset' : 'New Asset'}}</h3>
        <div class ="input-group">
            <input v-model="name" type = "text" placeholder="Name of the asset"/>
            <input v-model="polys" type = "number" placeholder="Number of polys"/>
            <label>📸 Preview:</label>
            <input
                :id="imageFileId"
                type="file"
                accept="image/*"
                @change="handleImageSelect"/>
            <label>📦 File 3D (.obj, .zip, .blend):</label>    
            <input
                :id="modelFileId"
                type = "file"
                accept=".obj,.fbx,.gltf,.glb,.stl,.dae,.blend"
                @change="handleFileSelect"/>


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
/*
    .form-container {
        background: #f0f0f0;
        color: black;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        border-left: 5px solid #42b883;
    }
    .edit-mode {
        border-left-color: #ffa500; 
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
    input[type="file"] {
        background: white;
        padding: 5px;
    }
    label {
  display: block;
  margin-top: 10px;
  font-size: 0.8em;
  color: #ccc;
  text-align: left;
}
*/
.form-container {
  background: #f8f9fa; 
  padding: 25px;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  max-width: 450px; 
  margin: 0 auto 30px 0; 
  border-top: 4px solid #42b883; 
}

/* Cambia stile quando sei in modalità modifica */
.form-container.edit-mode {
  border-top-color: #ffc107; /* Giallo per modifica */
  background: #fffbea;
}

h3 {
  margin-top: 0;
  margin-bottom: 20px;
  color: #2c3e50;
  text-align: center;
}

/* --- Layout a Colonna --- */
.input-group {
  display: flex;
  flex-direction: column; /* Impila tutto verticalmente */
  gap: 15px; /* Spazio verticale tra i campi */
}

/* --- Stile Input e Label --- */

/* Etichette per i file */
label {
  font-weight: 600;
  color: #555;
  margin-bottom: -5px; /* Avvicina un po' la label al suo input */
  display: block;
  font-size: 0.9em;
}

/* Campi di testo, numeri e file */
input[type="text"],
input[type="number"],
input[type="file"] {
  padding: 12px;
  border: 1px solid #dde2e7;
  border-radius: 6px;
  font-size: 14px;
  width: 100%; /* Occupa tutta la larghezza del contenitore */
  box-sizing: border-box; /* Include padding e bordo nella larghezza totale */
  background: white;
  transition: border-color 0.2s;
}

/* Effetto focus sugli input */
input:focus {
  outline: none;
  border-color: #42b883;
}

input[type="file"] {
  padding: 8px; /* Un po' meno padding per i file input */
  cursor: pointer;
}

/* --- Bottoni --- */
button {
  padding: 14px;
  background: #42b883; /* Verde Vue */
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s, transform 0.1s;
  width: 100%; /* Bottone largo quanto il form */
  margin-top: 10px; /* Un po' di spazio extra prima del bottone */
}

button:hover {
  background: #3aa876;
}

button:active {
  transform: scale(0.98); /* Piccolo effetto click */
}

/* Bottone "Annulla" (X) */
.cancel-btn {
  background: transparent;
  color: #d9534f;
  border: 2px solid #d9534f;
  margin-top: 0; /* Rimuovi margine extra */
}
.cancel-btn:hover {
  background: #d9534f;
  color: white;
}

  
</style>