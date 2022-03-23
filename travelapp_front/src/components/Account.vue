<template>
  <head>
    <title>Vuelos disponibles</title>
  </head>
  <body>
    <div id="info_cuenta">
      <table class="table2">
        <caption>
          INFORMACIÓN DE SU CUENTA
        </caption>
        <thead>
          <tr>
            <th>id</th>
            <th>Usuario</th>
            <th>Nombre</th>
            <th>Email</th>
            <th>Ultima conexión</th>
            <th>Activo</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ usuario.id }}</td>
            <td>{{ usuario.username }}</td>
            <td><input v-model="usuario.name" /></td>
            <td><input v-model="usuario.email" /></td>
            <td>{{ usuario.account.lastChangeDate }}</td>
            <td>{{ usuario.account.isActive }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>

  <div class="botons">
    <button v-on:click="processUpdateUser">Actualizar datos</button>
    <button v-on:click="loadBooking"> Ver reservas</button>
    <button v-on:click="deleteUser"> Eliminar cuenta</button>
  </div>
</template>


<script>
import jwt_decode from "jwt-decode";
import axios from "axios";

export default {
  name: "Account",

   data: () => ({
    usuarios: [],
    loaded: false,
    usuario: {},
  }),

  methods: {
    getData: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();

      axios
        .get(`https://be-travel-app.herokuapp.com/user-view/`, {headers: { Authorization: `Bearer ${token}` },
        })
        .then((result) => {
          this.usuario = result.data;
          localStorage.setItem("isAdmin",result.data.isAdmin);
          this.loaded = true;
        })
        .catch(() => {
          alert("Error");
        });
    },

    verifyToken: function () {
      /*devuelve una promesa*/
      return axios
        .post(
          `https://be-travel-app.herokuapp.com/refresh/`,
          { refresh: localStorage.getItem("token_refresh") },
          { headers: {} }
        )
        .then((result) => {
          localStorage.setItem("token_access", result.data.access);
        })
        .catch(() => {
          this.$emit("logOut");
        });
    },

    processUpdateUser: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }
      await this.verifyToken();

      let token = localStorage.getItem("token_access");

      let password = localStorage.getItem("pass");

      this.usuario.password = password;

      const user = this.usuario;
      const config = {
        headers: {
          "Content-Type": "application/json; charset=UTF-8",
          Authorization: `Bearer ${token}`,
        },
      };

      axios
        .put("https://be-travel-app.herokuapp.com/user-view/ ", user, config)
        .then((result) => {
          this.usuario = result.data;

          alert("Se actualizó correctamente");
        })
        .catch((error) => {
          console.log(error);
          alert("ERROR: Fallo en el registro." + error);
        });
    },
    deleteUser: async function () {
      
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let userId = jwt_decode(token).user_id.toString();
      let dato = {"id": userId};/*json que se pasa*/

      axios.delete(`https://be-travel-app.herokuapp.com/user-view/`,{headers: { Authorization: `Bearer ${token}` },
        })
        .then((result) => {
          usuarios.id = result.data.id;
          }).catch(() => {
            this.$emit("logOut");
            });       
    },

    loadBooking: function() {/*me redirijo a home*/
      this.$router.push({ name: "booking" });
    },

  },

  created: async function () {
    /*se ejecuta cuando la vista se cargue*/
    this.getData();
  },
 
};
</script>


<style>

.table2 table, th, td{
  border: 1px solid black;
  border-collapse: collapse;
  padding: 100%;
  border-spacing: 3px;
  position: static;
  height: 20px;
}
.table2 table{
  
  margin: 100%;
  position: static;

}
.table2 th{
  height: 25px;
  font: mostery bold;
  font-size: 113%;
}
.table2 caption{
  color: #283747;
  font: mostery bold;
  font-size: 50px;
  line-height: 70px;
  margin-top: 50px;
  margin-bottom: 50px;
}
.botons button{
        width: 32%;
        height: 40px;

        color: #E5E7E9;
        font:  mostery bold;
        background: #28517e;
        font-size: 16px;
        border: 1px solid #E5E7E9;

        border-radius: 5px;
        padding: 10px 25px;
        margin: 5px 0;
        align-items: center;
        justify-content: center;
        margin-top:50px;
        margin-left: 15px;
    }
</style>