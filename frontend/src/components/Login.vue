<template>
    <div>
        <h2>Login</h2>
        <form v-on:submit="login">
            <input type="text" name="email" /><br>
            <input type="password" name="password" /><br>
            <input type="submit" value="Login" />
        </form>
    </div>
</template>

<script>
// import router from '../router'
import axios from 'axios'
export default {
  name: 'Login',
  methods: {
    login: (e) => {
      e.preventDefault()
      let username = 'usera'
      let password = 'password'
      let login = () => {
        axios
          .get('http://127.0.0.1:8000/api/login', {
            params: {
              username: username,
              password: password
            },
            withCredentials: true
          })
          .then((response) => {
            console.log('Logged in')
            console.log(response)
          })
          .catch(err => { console.log(err) })

        // axios.get('http://127.0.0.1:8000/api/login', {
        //   params: {
        //     username: username,
        //     password: password
        //   }
        // })
        //   .then((response) => {
        //     console.log('Logged in')
        //     console.log(response)
        //   })
        //   .catch((errors) => {
        //     console.log('Cannot log in')
        //   })

        // axios.post('http://127.0.0.1:8000/api/login', data)
        //   .then((response) => {
        //     console.log('Logged in')
        //     router.push('/dashboard')
        //   })
        //   .catch((errors) => {
        //     console.log('Cannot log in')
        //   })
      }

      login()
    }
  }
}
</script>
