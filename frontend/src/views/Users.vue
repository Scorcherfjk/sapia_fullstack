<template>
  <div class="relative">
    <div class="container">
      <Sidebar />
      <div class="content">
        <h1 class="title">Usuarios online</h1>
        <h3 class="subtitle">
          conoce a las demas personas que comparten tu pasión
        </h3>
        <div class="users">
          <user-card v-for="user in users" :key="user.id" :user="user" />
        </div>
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
  </div>
</template>

<script>
import axios from "axios";
import userCard from "../components/userCard.vue";
import Sidebar from "../components/sidebar";
import Bottombar from "../components/bottombar";
import Alert from "../components/alert";

export default {
  components: {
    Alert,
    userCard,
    Sidebar,
    Bottombar,
  },
  data() {
    return {
      token: null,
      users: [],
      error: false,
      loading: false,
    };
  },
  async mounted() {
    this.token = localStorage.getItem("token");
    this.headers = {
      headers: { Authorization: `JWT ${this.token}` },
    };

    await this.get_all_users();
  },
  methods: {
    async get_all_users() {
      this.loading = true;
      try {
        const { data } = await axios.get(
          "http://127.0.0.1:5000/get/all",
          this.headers
        );
        console.log(data);

        this.users = data;
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

.users {
  @apply flex flex-col sm:flex-row flex-wrap;
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
