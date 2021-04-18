<template>
  <div class="container">
    <div class="sidebar"></div>
    <div class="content">
      <h1 class="title">Regístrate</h1>
      <form class="form" @submit.prevent="send">
        <div class="form-control">
          <label class="label" for="name">Nombre</label>
          <input
            required
            id="name"
            class="input"
            type="text"
            v-model="name"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="lastname">apellido</label>
          <input
            required
            id="lastname"
            class="input"
            type="text"
            v-model="lastname"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="phone_number">número de teléfono</label>
          <input
            required
            id="phone_number"
            class="input"
            type="text"
            maxlength="9"
            pattern="^9\d{0,8}"
            v-model="phone_number"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="date_of_birth">Fecha de nacimiento</label>
          <input
            required
            id="date_of_birth"
            class="input"
            type="date"
            v-model="date_of_birth"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="email">Correo Electrónico</label>
          <input
            required
            id="email"
            class="input"
            type="email"
            v-model="email"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="password">Contraseña</label>
          <input
            required
            id="password"
            class="input"
            type="password"
            v-model="password"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="headquarter">Sede</label>
          <input
            required
            id="headquarter"
            class="input"
            type="text"
            v-model="headquarter"
            :placeholder="placeholder"
          />
        </div>
        <div class="form-control">
          <label class="label" for="program">Programa de Especialización</label>
          <input
            required
            id="program"
            class="input"
            type="text"
            v-model="program"
            :placeholder="placeholder"
          />
        </div>
        <input class="button" type="submit" value="Enviar" />
        <router-link class="link" to="login">Iniciar Sesión</router-link>
      </form>
    </div>
    <alert
      v-show="error"
      type="error"
      content="Verifique sus datos e intente nuevamente"
    />
    <alert
      v-show="loading"
      type="loading"
      content="Cargando, espere un momento"
    />
    <alert
      v-show="success"
      type="success"
      content="Bienvenido, redirigiendo..."
    />
  </div>
</template>

<script>
import axios from "axios";
import alert from "../components/alert";

export default {
  components: {
    alert,
  },
  data() {
    return {
      placeholder: "Escriba aquí...",
      name: "",
      lastname: "",
      phone_number: null,
      date_of_birth: "",
      email: "",
      password: "",
      headquarter: "",
      program: "",
      error: false,
      success: false,
      loading: false,
    };
  },
  methods: {
    async send() {
      this.loading = true;
      try {
        const { data } = await axios.post("http://34.69.197.248/create", {
          name: this.name,
          lastname: this.lastname,
          phone_number: this.phone_number,
          date_of_birth: this.date_of_birth,
          email: this.email,
          password: this.password,
          headquarter: this.headquarter,
          program: this.program,
        });
        console.log(data);
        this.success = true;
        setTimeout(() => {
          this.success = false;
          this.$router.push("/login");
        }, 1000);
      } catch (error) {
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 5000);
      }
      this.loading = false;
    },
  },
};
</script>

<style lang="postcss" scoped>
.container {
  @apply w-screen h-screen max-w-full flex justify-center md:justify-end;
}

.content {
  @apply w-full p-2 mx-10 md:w-1/2 lg:w-1/3 xl:w-1/4;
}

.sidebar {
  background-image: url(../assets/bg.jpg);
  background-position: center center;
  background-size: contain;
  background-repeat: no-repeat;

  @apply w-0 h-screen md:w-2/3;
}

.title {
  @apply my-8 font-bold text-4xl;
}

.form {
  @apply pb-10;
}

.label {
  @apply mt-2 p-1 uppercase text-sm font-semibold text-gray-400;
}

.input {
  outline: 0;
  @apply w-full mb-2 p-2 border-2 rounded-lg border-gray-200;
}

.input:focus {
  @apply border-indigo-300;
}

.button {
  outline: 0;
  @apply w-full my-2 p-2 rounded-full bg-indigo-700 text-white font-semibold;
}

.link {
  @apply block w-full text-right text-indigo-400;
}
</style>
