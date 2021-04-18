<template>
  <div class="relative">
    <div class="container">
      <sidebar />
      <div class="content">
        <h1 class="title">Actualiza tus datos</h1>
        <form class="form" @submit.prevent="update_user">
          <div class="form-control">
            <label class="label" for="name">Nombre</label>
            <input
              id="name"
              class="input"
              type="text"
              v-model="name"
              :placeholder="placeholder"
            />
          </div>
          <div class="form-control">
            <label class="label" for="lastname">Apellido</label>
            <input
              id="lastname"
              class="input"
              type="text"
              v-model="lastname"
              :placeholder="placeholder"
            />
          </div>
          <div class="form-control">
            <label class="label" for="password">Contraseña</label>
            <input
              id="password"
              class="input"
              type="password"
              v-model="password"
              placeholder="Escribr tu nueva contraseña solo si deseas cambiarla"
            />
          </div>
          <div class="actions">
            <input
              class="button secondary"
              type="button"
              @click="() => $router.go(-1)"
              value="volver"
            />
            <input
              class="button primary"
              type="submit"
              value="Guardar cambios"
            />
          </div>
        </form>
      </div>
    </div>
    <bottombar />
    <alert
      v-show="error"
      type="error"
      content="Ha ocurrido un error, inténtalo de nuevo"
    />
    <alert
      v-show="loading"
      type="loading"
      content="Cargando, espere un momento"
    />
    <alert
      v-show="success"
      type="success"
      content="Datos actualizados satisfactoriamente"
    />
  </div>
</template>

<script>
import axios from "axios";
import Sidebar from "../../components/sidebar";
import Bottombar from "../../components/bottombar";
import Alert from "../../components/alert";

export default {
  components: {
    Alert,
    Sidebar,
    Bottombar,
  },
  data() {
    return {
      placeholder: "Escriba aquí...",
      token: null,
      name: "",
      lastname: "",
      password: "",
      error: false,
      success: false,
      loading: false,
    };
  },
  async mounted() {
    this.token = localStorage.getItem("token");
    this.headers = {
      headers: { Authorization: `JWT ${this.token}` },
    };

    await this.get_user();
  },
  methods: {
    async get_user() {
      this.loading = true;
      try {
        const { data } = await axios.get(
          "http://34.69.197.248/get/user",
          this.headers
        );

        this.name = data.name;
        this.lastname = data.lastname;

        // this.success = true;
      } catch (error) {
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 1000);
      }
      this.loading = false;
    },
    async update_user() {
      this.loading = true;
      try {
        const userData = {
          name: this.name,
          lastname: this.lastname,
        };

        if (this.password !== "") userData.password = this.password;

        const { data } = await axios.post(
          "http://34.69.197.248/update/user",
          userData,
          this.headers
        );
        console.log(data);

        this.success = true;
        setTimeout(() => {
          this.success = false;
        }, 1000);
      } catch (error) {
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 1000);
      }
      this.loading = false;
    },
  },
};
</script>

<style lang="postcss" scoped>
.container {
  @apply mb-16 md:mb-0 w-screen max-w-full flex;
}

.content {
  @apply overflow-y-scroll md:h-screen w-full p-8 md:px-2 md:px-10;
}

.title {
  @apply mt-8 mb-2 font-bold text-4xl;
}

.subtitle {
  @apply mb-8 font-semibold text-xl;
}

.form {
  @apply flex flex-col flex-wrap items-end;
}

.form-control {
  @apply w-full p-2;
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

.actions {
  @apply flex w-full;
}

.button {
  outline: 0;
  @apply block w-full mx-4 mb-2 p-2 rounded-full text-center font-semibold;
}

.primary {
  @apply bg-indigo-700 text-white;
}

.secondary {
  @apply bg-white border-2 border-indigo-700 text-indigo-700;
}
</style>
