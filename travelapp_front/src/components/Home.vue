<template>
  <center>
    <div class="Information">
      <div class="container_information">
        <img class="imagen"
          src="https://static.wixstatic.com/media/9c808c_54b69223547d4490b22dc588ea70804f~mv2.gif"
        />
        <h1>¿QUIÉNES SOMOS?</h1>
        <p class="box2">
          Somos una empresa líder en servicio de transporte cumpliendo los
          estándares de seguridad con los menores costos del mercado, desde
          1992, siendo líderes en las medidas de bioseguridad durante la
          pandemia y aún en la actualidad.
        </p>
      </div>
    </div>
  </center>
  <body></body>
</template>

<script>
export default {
  name: "Home",

  data: function () {
    return {
      username: localStorage.getItem("username") || "none" /*|| excepcion*/,
    };
  },
};
</script>

<style>
.container_information h1 {
  color: #283747;
  font: 255% mostery;
  font-weight: bold;
  margin-top: 5px;
}

p.box2 {
  border: 3px solid #28517e;
  border-radius: 10px;
  width: 30%;
  height: 50%;
  background: #cfe2f7;
  padding: 02%;
  font-weight: bold;

  display: flex;
  justify-content: center;
  align-items: center;
  font: 130% mostery;
  margin-top: 40px;
}
.imagen {
  border: 0;
  padding: -40px;
  width: 370px;
  text-decoration: underline;
  background: transparent;
}
</style>