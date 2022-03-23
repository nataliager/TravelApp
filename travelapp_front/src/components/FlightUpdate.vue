<template>
  <div class="update_flight">
    <div class="container_update_flight">
      <h2>Actualizar vuelo</h2>

      <form v-on:submit.prevent="processUpdateFlight()">
        <input
          type="text"
          v-model="flight.flightNumber"
          placeholder="Número de vuelo"
        />
        <br />

        <input
          type="datetime-local"
          v-model="flight.departureDate"
          placeholder="Fecha de ida"
        />
        <br />

        <input
          type="datetime-local"
          v-model="flight.returnDate"
          placeholder="Fecha de regreso"
        />
        <br />

        <select v-model="flight.origin">
          <option disabled value="">Seleccione ciudad de origen</option>
          <option>Bogotá</option>
          <option>Cali</option>
          <option>Medellín</option>
          <option>Armenia</option>
          <option>Pereira</option>
          <option>Barranquilla</option>
          <option>Neiva</option>
          <option>San Andrés</option>
          <option>Santa Marta</option>
          <option>Cartagena</option>
          <option>Leticia</option>
          <option>Popayán</option>
          <option>Montería</option>
          <option>Manizales</option>
          <option>Cúcuta</option>
        </select>
        <br />

        <select v-model="flight.destination">
          <option disabled value="">Seleccione ciudad de destino</option>
          <option>Bogotá</option>
          <option>Cali</option>
          <option>Medellín</option>
          <option>Armenia</option>
          <option>Pereira</option>
          <option>Barranquilla</option>
          <option>Neiva</option>
          <option>San Andrés</option>
          <option>Santa Marta</option>
          <option>Cartagena</option>
          <option>Leticia</option>
          <option>Popayán</option>
          <option>Montería</option>
          <option>Manizales</option>
          <option>Cúcuta</option>
        </select>
        <br />

        <select v-model="flight.airline">
          <option disabled value="">Seleccione un elemento</option>
          <option>Avianca</option>
          <option>LATAM</option>
          <option>EasyFly</option>
          <option>Viva CO</option>
          <option>Airlines</option>
          <option>Wingo</option>
          <option>SATENA</option>
          <option>Spirit</option>
        </select>
        <br />

        <input
          type="number"
          v-model="flight.weight"
          placeholder="Peso equipaje"
        />
        <br />

        <input
          type="number"
          v-model="flight.price"
          placeholder="Precio ticket"
        />
        <br />

        <button type="submit">Actualizar vuelo</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "FlightUpdate",

  data: function () {
    return {
      /*devuelve dict con las var*/
      flight: {
        flightNumber: "",
        departureDate: "",
        returnDate: "",
        origin: "",
        destination: "",
        airline: "",
        weight: "",
        price: "",
      },
    };
  },

  methods: {
    processUpdateFlight: function () {
      let idFlight = this.flight.flightNumber;
      axios
        .put(
          /*manera asincronica*/
          `https://be-travel-app.herokuapp.com/flight/${idFlight}/`,
          this.flight,
          { headers: {} }
        )
        .then((result) => {
          (this.flight = result.data),
            alert("Se actualizó el vuelo exitosamente!!");
        })
        .catch((error) => {
          console.log(error);
          alert("ERROR: Fallo en la actualización del vuelo.");
        });
    },
  },
};
</script>

<style>
.update_flight {
  margin: 0;
  padding: 0%;
  height: 100%;
  width: 100%;

  display: flex;
  justify-content: center;
  align-items: center;
}

.container_update_flight {
  border: 3px solid #283747;
  border-radius: 10px solid;
  width: 50%;
  height: 60%;
  background: #cfe2f7;

  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 10px;
  position: static;
  padding: 0px 0px 0px 0px;
}

.update_flight h2 {
  color: #283747;
  font: 220% mostery;
  font-weight: bold;
  margin-bottom: 10px;
}

.update_flight form {
  width: 70%;
}

.update_flight input,
select {
  height: 35px;
  width: 100%;

  box-sizing: border-box;
  padding: 10px 20px;
  margin: 5px 0;

  border: 1px solid #283747;
}

.update_flight button {
  width: 100%;
  height: 40px;

  color: #e5e7e9;
  font: mostery;
  background: #28517e;
  border: 1px solid #e5e7e9;

  border-radius: 5px;
  padding: 10px 25px;
  margin: 5px 0 25px 0;
}

.update_flight button:hover {
  color: #e5e7e9;
  background: #99303e;
  border: 1px solid #283747;
}
</style>