<script setup>
  import AssetForm from '@/components/AssetForm.vue';
  import AssetCard from '@/components/AssetCard.vue';
  import LoginForm from '@/components/LoginForm.vue';
  import {ref, onMounted} from 'vue'

  const assets = ref([])
  const assetToEdit = ref(null)

  const token = ref(localStorage.getItem('user-token') || null)
  //const token = ref(null)
  if(token.value) {
    console.log("token-found")
  } else {console.log("token-not-defined")}
    
  async function fetch_assets(){
      const response = await fetch('http://127.0.0.1:8000/core/assets/')
      const data = await response.json()
      assets.value = data
    }
  onMounted(() => {
    fetch_assets()
  })

  const enableEditAsset = (asset) => {
    assetToEdit.value = asset
  }

  const cancelEdit = () => {
    assetToEdit.value = null
  }

 

  const handleCreate = async (newAssetData) => {
     const headers = {
    'Content-type': 'application/json',
    'Authorization': `Token ${token.value}`
  }
    if(assetToEdit.value == null){
    try {
      const response = await fetch ('http://127.0.0.1:8000/core/assets/', {
        method: 'POST',
        headers: headers,
        body: JSON.stringify(newAssetData)
      })

      if(response.ok){
        console.log("OK-created")
        fetch_assets();
      }
    } catch(error){
      console.error("Error:", error)
    }
  } else {
      try {
        const assetId = assetToEdit.value.id
        const response = await fetch (`http://127.0.0.1:8000/core/assets/${assetId}/`, {
          method: 'PUT',
          headers: headers,
          body: JSON.stringify(newAssetData)
        })

        if(response.ok){
          console.log("OK-created")
          fetch_assets();
          assetToEdit.value = null
        }
      } catch(error){
        console.error("Error:", error)
      }
    }

  }


  const handleDelete = async (assetId) => {
    if (!confirm("Confirm delete")) return
    //console.log(assetId.id)
    //console.log('http://127.0.0.1:8000/core/assets/' + assetId.id +'/')
    try{
      
    const response = await fetch(`http://127.0.0.1:8000/core/assets/${assetId.id}/`, {
      method: "DELETE",
      headers : {'Authorization': `Token ${token.value}`}
    })

    if(response.ok){
      console.log("Ok-Deleted")
      fetch_assets();
    }
  } catch(error) {
    console.log("Error:", error)
  }

  }

  const handleLogin = async (credentials) => {
    try{
        console.log(credentials)
        const response = await fetch('http://127.0.0.1:8000/auth/token/login/', {
          method: "POST",
          headers: { 'Content-type': 'application/json'},
          body: JSON.stringify(credentials)
        })

        if(response.ok){
          const data = await response.json()
          const receivedToken = data.auth_token
          token.value = receivedToken
          localStorage.setItem('user-token', receivedToken)
        }

    } catch(error){
        console.log("Error:", error)
    }
  }

  const handleLogout = () => {
    token.value = null;
    localStorage.removeItem('user-token')
  }

</script>

<template>
  
  <div>
    <div class="container">
      <h1>Asset Factory</h1>
      <div v-if="!token">
        <LoginForm @user-login="handleLogin"/>
      </div>
      <div v-else>
        <div class="top-bar">
          <p>Welcome, User!</p>
          <button @click="handleLogout" class="logout-btn">Logout</button>
        </div>

        <AssetForm 
        :editingAsset="assetToEdit"
        @create-asset="handleCreate"
        @cancel-edit="cancelEdit"/>

        <hr>

        <div class="grid">
            <AssetCard v-for="item in assets" :key="item.id" :asset="item" @delete-asset="handleDelete" @edit-asset="enableEditAsset"/>
        </div>
      </div>
    </div>
  </div>
  
</template>

<style scoped>
  .top-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  background: #ddd;
  color: black;
  padding: 10px;
  border-radius: 4px;
}
.logout-btn {
  background: #d9534f; /* Rosso */
}
  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 20px;
    font-family: sans-serif;
  }
  .grid{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 20px;
    margin-top: 20px;
  }
  hr {
    border:0;
    border-top:1px solid #ddd;
    margin: 30px 0;
  }

</style>
