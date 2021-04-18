<template>
  <div class="relative">
    <div class="container">
      <sidebar />
      <div class="content">
        <h1 class="title">Cuéntanos sobre ti</h1>
        <h3 class="subtitle">
          esta información la podrán ver las demas personas
        </h3>
        <div class="card">
          <div class="card-detail">
            <img class="image" :src="image" :alt="name" />
            <div class="data">
              <h2 class="title">{{ name }} {{ lastname }}</h2>
              <p class="subtitle">
                {{ email }}
              </p>
            </div>
          </div>
          <div class="card-detail">
            <div class="data">
              <p class="subtitle">
                Modificar usuario?
              </p>
              <router-link class="button" to="/update/user"
                >Modificar</router-link
              >
            </div>
          </div>
        </div>
        <form class="form" @submit.prevent="update_profile">
          <div class="form-control">
            <label class="label" for="phone_number">Número de teléfono</label>
            <input
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
              id="date_of_birth"
              class="input"
              type="date"
              v-model="date_of_birth"
              :placeholder="placeholder"
            />
          </div>

          <div class="form-control">
            <label class="label" for="headquarter">sede</label>
            <input
              id="headquarter"
              class="input"
              type="text"
              v-model="headquarter"
              :placeholder="placeholder"
            />
          </div>

          <div class="form-control">
            <label class="label" for="program"
              >programa de especialización</label
            >
            <input
              id="program"
              class="input"
              type="text"
              v-model="program"
              :placeholder="placeholder"
            />
          </div>

          <div class="form-control-area">
            <label class="label" for="bio">Biografía</label>
            <textarea id="bio" v-model="bio" class="input" rows="3"></textarea>
          </div>
          <input class="button" type="submit" value="Guardar cambios" />
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
import Sidebar from "../components/sidebar";
import Bottombar from "../components/bottombar";
import gravatar from "../utils/gravatar";
import Alert from "../components/alert";

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
      phone_number: "",
      name: "",
      lastname: "",
      email: "",
      date_of_birth: "",
      headquarter: "",
      program: "",
      bio: "",
      image: "",
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
        this.email = data.email;
        this.phone_number = data.phone_number;
        this.date_of_birth = data.date_of_birth;
        this.headquarter = data.headquarter;
        this.program = data.program;
        this.bio = data.bio;
        this.image = gravatar(data.email);

      } catch (error) {
        console.log(error);
        this.error = true;
        setTimeout(() => {
          this.error = false;
        }, 1000);
      }
      this.loading = false;
    },
    async update_profile() {
      this.loading = true;
      try {
        const userData = {
          phone_number: this.phone_number,
          date_of_birth: this.date_of_birth,
          headquarter: this.headquarter,
          program: this.program,
          bio: this.bio,
        };

        const { data } = await axios.post(
          "http://34.69.197.248/update/profile",
          userData,
          this.headers
        );

        console.log(data);
        this.success = true;
        setTimeout(() => {
          this.success = false;
        }, 2000);
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
  @apply my-2 font-bold text-4xl;
}

.subtitle {
  @apply mb-8 font-semibold text-xl;
}

.card {
  @apply flex justify-between items-center p-4 w-full border-2 rounded-xl;
}

.card-detail {
  @apply flex items-center;
}

.image {
  @apply w-24 h-24 rounded-full;
}

.data {
  @apply ml-6;
}

.data .title {
  @apply capitalize;
}

.data .subtitle {
  @apply my-2;
}

.form {
  @apply flex flex-col flex-wrap justify-end md:flex-row;
}

.form-control {
  @apply w-full md:w-6/12 p-2;
}

.form-control-area {
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

.button {
  outline: 0;
  @apply block w-full md:max-w-md my-2 p-2 rounded-full bg-indigo-700 text-white text-center font-semibold;
}

.error {
  @apply text-red-500;
}

.success {
  @apply text-green-500;
}

.loading {
  @apply text-gray-500;
}
</style>
