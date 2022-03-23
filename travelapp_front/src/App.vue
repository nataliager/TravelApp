<template>
  <div id="app" class="app">
    <div class="header">
      <h1><img src="./assets/mosteryAPP.png" /></h1>
      <nav>
        <button v-if="is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="!is_auth" v-on:click="loadHome">Inicio</button>
        <button v-if="is_auth" v-on:click="loadAccount">Cuenta</button>
        <button v-on:click="loadFlight">Vuelos</button>
        <button v-if="is_auth" v-on:click="logOut">Cerrar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadLogIn">Iniciar Sesión</button>
        <button v-if="!is_auth" v-on:click="loadSignUp">Registrarse</button>
      </nav>
    </div>

    <body></body>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
        v-on:logOut="logOut"
      >
      </router-view>
    </div>

    <div class="footer">
      <ul>
        <li><img src="./assets/1.png" alt="#" /> Calle 7 # 24 A - 27 Bogotá</li>
        <li><img src="./assets/2.png" alt="#" /> +57 3164699599</li>
        <li><img src="./assets/3.png" alt="#" /> travelapp@gmail.com</li>
      </ul>
    </div>
  </div>
</template>


<script>
export default {
  name: "App",

  data: function () {
    return {
      is_auth: false,
    };
  },

  components: {},

  methods: {
    verifyAuth: function () {

      /*Permite verificar si esta autenticado*/
      this.is_auth =
        localStorage.getItem("isAuth") ||
        false; /*verifica si estoy autenticado*/

      if (this.is_auth == false)
        this.$router.push({ name: "home" });/*si no estoy autenticado me voy a home*/
      else
        this.$router.push({ name: "account" });/*si estoy autenticado me voy a account*/ 
    },

    loadLogIn: function () {
      this.$router.push({ name: "logIn" });/*redirige al componente de login con router push*/
    },

    loadSignUp: function () {
      this.$router.push({ name: "signUp" });
    },

    completedLogIn: function (data) {

      /*datos a guardar en el localstorage*/
      localStorage.setItem("isAuth", true); /*esta autenticado*/
      localStorage.setItem(
        "username",
        data.username /*guardar username, data que envia el hijo*/
      ); 
      localStorage.setItem("token_access", data.token_access);
      localStorage.setItem("token_refresh", data.token_refresh);
      localStorage.setItem("pass", data.password);
      alert("¡Sesión iniciada con éxito!:");
      this.verifyAuth();
    },

    completedSignUp: function (data) {
      alert("Te has registrado exitosamente.");
      this.completedLogIn(data);
    },

    loadHome: function () {
      this.$router.push({ name: "home" });/*me redirijo a home*/
    },

    logOut: function () {
      localStorage.clear(); /*quitar todo lo del local storage*/
      alert("Sesión Cerrada");
      this.verifyAuth(); /*llamo a la func, y lo busca y como no esta toma valor false*/
    },

    loadAccount: function () {
      this.$router.push({ name: "account" });
    },

    loadFlight: function () {
      this.$router.push({ name: "flight" });
    },
  },

  created: function () {/*se ejecuta cuando se carga la pagina*/
    this.verifyAuth();
  },
};
</script>

<style>

.header {
  background: url(../src/assets/header-bg.jpg);
  background-color: rgba(0, 0, 0, 0);
  background-repeat: repeat;
  background-size: auto;
  background-color: #00000052;
  box-shadow: #060606 0px 0px 3px 0px;
  z-index: 999;
  width: 100%;
  left: 0;
  top: 0;
  background-color: #00000052;
  padding: 0;
  padding-top: 0px;
  background-size: 100% 100%;
  background-repeat: no-repeat;
  color: #f8fcff;

  margin: 0;
  padding: 0;
  height: 10vh;
  min-height: 100px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

body {
  background-image: url("./assets/fondo.jpg");
  background-size: cover;
  background-repeat: no-repeat;
  width: 100%;
  margin: 0 0 0 0;
}

.header h1 {
  width: 50%;
  text-align: center;
  font: 300% mostery;
  justify-content: center;
  align-items: center;
  background-repeat: no-repeat;
}

.header nav {
  height: 100%;
  width: auto;

  display: flex;
  justify-content: space-around;
  align-items: center;

  font-size: 20px;
}
.header nav button {
  color: #e5e7e9;
  background: url(../src/assets/header-bg.jpg);
  background-color: rgba(0, 0, 0, 0);
  border: 1px solid #e5e7e9;
  background-color: #00000052;
  box-shadow: #060606 0px 0px 3px 0px;
  background-color: #00000052;

  border-radius: 5px;
  padding: 10px 15px;
  margin: 1.5%;
  margin-right: 5px;
}

.header nav button:hover {
  /*Cuando paso mouse por encima*/
  color: #283747;
  background: #e5e7e9;
  border: 1px solid #e5e7e9;
}

.main-component {
  height: fit-content;
  min-height: 80vh;
  margin: 0%;
  padding: 0%;
}

.footer {
  background: url(../src/assets/header-bg.jpg);
  background-color: rgba(0, 0, 0, 0);
  background-size: auto;
  background-color: #00000052;
  box-shadow: #060606 0px 0px 3px 0px;
  z-index: auto;
  background-color: #00000052;
  padding: 0;
  padding-top: 0px;
  background-size: 100% 100%;
  background-repeat: no-repeat;
  color: #f8fcff;
  margin: 0;
  padding: 0;
  min-height: 100px;

  width: 100%;
  height: 81px;
  position: absolute;
  bottom: 0;
}

.footer li {
  width: 100%;
  height: 80%;
  font: 140% mostery center;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
