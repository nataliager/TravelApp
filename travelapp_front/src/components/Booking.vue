<template>
  <head>
    <title>Reservas</title>
  </head>
  <body>
    <div class="container_booking_flight">
      <h2>ID reserva</h2>

      <form class="formulario" v-on:submit.prevent="processBooking">
        <input type="text" v-model="this.bId" placeholder="id" />
        <br/>

        <button v-on:click="created()" type="submit">Buscar</button>
      </form>
    </div>

    <div id="info_cuenta">
      <table class="table stripped bordered2">
        <caption>
          RESERVAS
        </caption>
        <thead>
          <tr>
            <th>id</th>
            <th>Número de vuelo</th>
            <th>id del usuario</th>
            <th>Fecha de la reserva</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>{{ this.bId }}</td>
            <td>{{ booking.flight }}</td>
            <td>{{ booking.idUser }}</td>
            <td>{{ booking.date }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </body>
  <div class="botonReservar">
    <button v-on:click="deleteBooking()">Eliminar reserva</button>
  </div>
</template>


<script>
import axios from "axios";

export default {
  name: "Booking",

  data: () => ({
    loaded: false,
    bId: "",
    booking: {},
  }),

  methods: {
    getBooking: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }

      await this.verifyToken();

      let token = localStorage.getItem("token_access");
      let isadmin = localStorage.getItem("isAdmin");
      let idBooking = this.bId;

      axios
        .get(`https://be-travel-app.herokuapp.com/booking/${idBooking}/`, {
          headers: { Authorization: `Bearer ${token}` },
        })
        .then((result) => {
          this.booking = result.data;
          this.loaded = true;
        })
        .catch(() => {
          alert("Reserva no encontrada");
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

    deleteBooking: async function () {
      if (
        localStorage.getItem("token_access") === null ||
        localStorage.getItem("token_refresh") === null
      ) {
        this.$emit("logOut");
        return;
      }
      await this.verifyToken();
      let token = localStorage.getItem("token_access");

      axios
        .delete(
          `https://be-travel-app.herokuapp.com/booking/${this.booking.id}/`,
          { headers: { Authorization: `Bearer ${token}` } }
        )
        .then((result) => {
          alert("La reserva se ha eliminado exitosamente");
        })
        .catch(() => {
          alert("No se pudo eliminar la reserva...");
        });
    },

    created: async function () {
      /*se ejecuta cuando la vista se cargue*/
      this.getBooking();
    },
  },
};
</script>


<style>
table {
  width: 100%;
}
.container_booking_flight {
  border: 3px solid #283747;
  border-radius: 10px solid;
  width: 30%;
  height: 50%;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-left: 469px;
  margin-top: 30px;
  position: static;
  padding: 200%;
  padding: 0px 0px 0px 0px;
  background-repeat: no-repeat;
}
.eti h2 {
  color: #283747;
  font: 300% mostery;
  font-weight: bold;
}

.container_booking_flight caption {
  color: #283747;
  font: mostery bold;
  font-size: 60px;
  line-height: 70px;
  background-repeat: no-repeat;
}
.container_booking_flight table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 7px;
  border-spacing: 3px;
}
td {
  text-align: left;
}
tr:nth-child(even) {
  /*renglones pares*/
  background-color: #f1faee;
}
tr:nth-child(odd) {
  /*renglones impares*/
  background-color: #c2ceda;
}
th {
  color: white;
  background: #283747;
}
.botonReservar button {
  color: #e5e7e9;
  font: 100% mostery bold;
  background: #28517e;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 08px 09px;
  margin: 5px center;
  margin-top: 60px;
  margin-left: 600px;
  width: 150px;
}
.botonReservar button:hover {
  color: #e5e7e9;
  background: #99303e;
  border: 1px solid #283747;
}
</style>