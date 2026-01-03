<script setup>
    import {ref} from 'vue'

    const username = ref("")
    const password = ref("")

    const emit = defineEmits(['user-login'])

    const handleLogin = () => {
        console.log("ciao")
        const payload = {
            username: username.value,
            password: password.value
        }
        emit('user-login', payload)
    }

</script>

<template>
    <div class="login-container">
        <h2> Access Reserved</h2>
        <!--<form @sumbit.prevent = "handleLogin">
            <input v-model="username" type="text" placeholder="username" >
            <input v-model="password" type="password" placeholder="password">
            <button type = "submit" >Login</button>
        </form>-->
         <input v-model="username" type="text" placeholder="username" >
            <input v-model="password" type="password" placeholder="password">
            <button @click="handleLogin" >Login</button>
        
    </div>

</template>

<style scoped>
    .login-container {
  max-width: 300px;
  margin: 50px auto;
  padding: 30px;
  background: #2a2a2a;
  color: white;
  border-radius: 8px;
  text-align: center;
  box-shadow: 0 4px 15px rgba(0,0,0,0.5);
}
input {
  display: block;
  width: 100%;
  padding: 10px;
  margin: 10px 0;
  box-sizing: border-box;
}
button {
  width: 100%;
  padding: 10px;
  background: #42b883;
  border: none;
  color: white;
  font-weight: bold;
  cursor: pointer;
  margin-top: 10px;
}

</style>