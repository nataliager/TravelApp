<template>
  <body>
    <div class="scroll-table-container">
      <div id="vuelos">
        <table class="table stripped bordered">
          <caption>
            VUELOS DISPONIBLES
          </caption>
          <thead>
            <tr>
              <th>Número de vuelo</th>
              <th>Fecha de ida</th>
              <th>Fecha de regreso</th>
              <th>Origen</th>
              <th>Destino</th>
              <th>Aerolínea</th>
              <th>Peso</th>
              <th>Precio</th>
              <th>Acción</th>
              <th v-if="isAdmin">Actualizar</th>
              <th v-if="isAdmin">Eliminar</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="flight in flights" v-bind:key="flight.flightNumber">
              <td>
                <center>{{ flight.flightNumber }}</center>
              </td>
              <td>
                <center>{{ flight.departureDate }}</center>
              </td>
              <td>
                <center>{{ flight.returnDate }}</center>
              </td>
              <td>
                <center>{{ flight.origin }}</center>
              </td>
              <td>
                <center>{{ flight.destination }}</center>
              </td>
              <td>
                <center>{{ flight.airline }}</center>
              </td>
              <td>
                <center>{{ flight.weight }}</center>
              </td>
              <td>
                <center>{{ flight.price }}</center>
              </td>
              <td>
                <center>
                  <button v-on:click="reservar(flight.flightNumber)">
                    Reservar
                  </button>
                </center>
              </td>
              <td v-if="isAdmin">
                <center>
                  <button v-on:click="update_flight()">Actualizar</button>
                </center>
              </td>
              <td v-if="isAdmin">
                <center>
                  <button v-on:click="deleteFlight(flight.flightNumber)">
                    Eliminar
                  </button>
                </center>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </body>

  <div v-if="isAdmin" class="boton">
    <center>
      <button v-on:click="createFlight">Crear un vuelo</button>
    </center>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from "jwt-decode";

export default {
  name: "Flight",

  data() {
    return {
      flights: [],
      isAdmin: localStorage.getItem("isAdmin") == "true",
    };
  },

  methods: {
    getData: async function () {
      axios
        .get(`https://be-travel-app.herokuapp.com/flightDetail`)
        .then((result) => {
          this.flights = result.data;
        })
        .catch(() => {
          this.$emit("logOut");
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

    reservar: async function (flightNumber) {
      this.is_auth =
        localStorage.getItem("isAuth") ||
        false; /*verifica si estoy autenticado*/

      if (this.is_auth == false)
        /*si no estoy autenticado me voy a logIn*/
        this.$router.push({ name: "logIn" });
      /*si estoy autenticado me voy a home*/ else {
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
        let reserva = {
          flight: flightNumber,
          idUser: userId,
        }; /*json que se pasa*/

        axios
          .post(`https://be-travel-app.herokuapp.com/booking`, reserva, {
            headers: { Authorization: `Bearer ${token}` },
          })
          .then((result) => {
            alert(
              "Reserva exitosa. Su numero de reserva es: " +
                result.data.NoReserva +
                " .Guardelo para futuras consultas."
            );
          })
          .catch(() => {
            alert("No se pudo hacer la reserva...");
          });
      }
    },

    deleteFlight: async function (flightNumber) {
      this.flights.flightNumber = flightNumber;
      axios
        .delete(`https://be-travel-app.herokuapp.com/flight/${flightNumber}/`)
        .then((result) => {
          alert("El vuelo se ha eliminado exitosamente");
        })
        .catch(() => {
          alert("No se pudo eliminar el vuelo...");
        });
    },

    createFlight: function () {
      /*me redirijo a createflight*/
      this.$router.push({ name: "createflight" });
    },

    update_flight: function () {
      /*me redirijo a updateFlight*/
      this.$router.push({ name: "updateflight" });
    },
  },

  created: async function () {
    /*se ejecuta cuando la vista se cargue*/
    this.getData();
  },
};
</script>

<style>
caption {
  color: #283747;
  font: mostery bold;
  font-size: 45px;
  line-height: 70px;
}
table,
th,
td {
  border: 1px solid black;
  border-collapse: collapse;
  padding: 7px;
  border-spacing: 3px;
  position: static;
  position: static;
}
td {
  text-align: center;
  font: mostery bold center;
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
  position: static;
}
tbody {
  overflow-y: scroll;
}
button {
  color: #e5e7e9;
  font: mostery bold;
  background: #28517e;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 05px 5px;
  margin: 5px center;
  position: static;
}
.scroll-table-container {
  border: 2px solid green;
  height: 500px;
  overflow: scroll;
  position: static;
}
button:hover {
  color: #e5e7e9;
  background: #99303e;
  border: 1px solid #283747;
}
.boton button {
  color: #e5e7e9;
  font: 100% mostery bold;
  background: #28517e;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 08px 09px;
  margin: 5px center;
  margin-top: 09px;
  width: 150px;
  position: static;
}
.boton button:hover {
  color: #e5e7e9;
  background: #99303e;
  border: 1px solid #283747;
}
</style>