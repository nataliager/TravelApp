<template>
  <div class="logIn_user">
    <div class="container_logIn_user">
      <h2>Iniciar sesión</h2>

      <form v-on:submit.prevent="processLogInUser">
        <input type="text" v-model="user.username" placeholder="Username" />
        <br />
        <input type="password" v-model="user.password" placeholder="Password" />
        <br />
        <button type="submit">Iniciar Sesion</button>
      </form>
    </div>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "LogIn" /*nombre de la vista*/,

  data: function () {
    /*devuelve un dict con las variables */
    return {
      user: {
        username: "",
        password: "",
      },
    };
  },

  methods: {
    processLogInUser: function () {
      /*comunicacion con el back con axios*/
      axios
        .post(
          "https://be-travel-app.herokuapp.com/login/",
          this.user /*dentro de user esta username and password*/,
          { headers: {} } /*otra forma de enviar info*/
        )
        .then((result) => {
          /*se ejecuta cuando los codigos http sean 200*/
          let dataLogIn = {
            /*obj */ username: this.user.username,
            token_access: result.data.access /*es eñ json de respuest*/,
            token_refresh: result.data.refresh /*datos de autenticación*/,
            password: this.user.password,
          };

          this.$emit("completedLogIn", dataLogIn); /*emitir al padre*/
        })
        .catch((error) => {
          if (error.response.status == "401")
            alert("ERROR 401: Credenciales Incorrectas.");
        });
    },
  },
};
</script>

<style>
.logIn_user {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container_logIn_user {
  border: 3px solid #28517e;
  border-radius: 10px;
  width: 30%;
  height: 100%;
  background: #cfe2f7;
  padding: 15px 30px 35px 30px;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 110px;
  position: static;
}

.logIn_user h2 {
  color: #283747;
  font: 250% mostery;
  font-weight: bold;
}

.logIn_user form {
  width: 70%;
}

.logIn_user input {
  height: 40px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.logIn_user button {
  width: 100%;
  height: 40px;

  color: #e5e7e9;
  font: mostery;
  background: #28517e;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0;
}

.logIn_user button:hover {
  color: #e5e7e9;
  background: #99303e;
  border: 1px solid #283747;
}
</style>