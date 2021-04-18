<template>
  <div class="container">
    <div class="sidebar"></div>
    <div class="content">
      <h1 class="title">Iniciar Sesión</h1>
      <form class="form" @submit.prevent="send">
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
        <input class="button" type="submit" value="Ingresar" />
        <router-link class="link" to="register">Regístrate</router-link>
      </form>
    </div>
    <alert v-show="error" type="error" content="Correo o clave incorrectos" />
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
import { mapActions } from "vuex";
import axios from "axios";

import alert from "../components/alert";

export default {
  components: {
    alert,
  },
  data() {
    return {
      placeholder: "Escriba aquí...",
      email: "",
      password: "",
      error: false,
      success: false,
      loading: false,
    };
  },
  methods: {
    ...mapActions(["logInAction"]),
    async send() {
      this.loading = true;
      try {
        const { data } = await axios.post("http://127.0.0.1:5000/auth", {
          username: this.email,
          password: this.password,
        });
        this.logInAction(data.access_token);

        this.success = true;
        setTimeout(() => {
          this.success = false;
          this.$router.push("/users");
        }, 1500);
      } catch (error) {
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 2000);
      }
      this.loading = false;
    },
  },
};
</script>

<style lang="postcss" scoped>
.container {
  @apply w-screen h-screen max-w-full flex justify-center items-center md:justify-end;
}

.content {
  @apply w-full p-2 mb-10 mx-10 md:w-1/2 lg:w-1/3 xl:w-1/4;
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
