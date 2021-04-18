<template>
  <div class="sidebar">
    <div class="content">
      <h2 class="title">
        The <br />
        University
      </h2>
      <router-link class="link" to="/users">
        <i class="icon material-icons">home</i>
        <p>Inicio</p>
      </router-link>
      <router-link class="link" to="/message">
        <i class="icon material-icons">message</i>
        <p>Mensajes</p>
      </router-link>
      <router-link class="link" to="/profile">
        <i class="icon material-icons">perm_identity</i>
        <p>Mi cuenta</p>
      </router-link>
    </div>
    <div class="footer">
      <button class="link" @click="logout">
        <i class="icon material-icons">logout</i>
        <p>Salir</p>
      </button>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  methods: {
    ...mapActions(["logOutAction"]),
    logout(){
      this.logOutAction()
      this.$router.push('/login')
    }
  }
}
</script>

<style lang="postcss" scoped>
.sidebar {
  @apply hidden md:flex flex-col py-4 justify-between sm:w-1/3 lg:w-1/4 xl:w-1/5 h-screen bg-indigo-700;
}

.content,
.footer {
  @apply flex flex-col;
}

.title {
  @apply p-4 uppercase text-white font-bold text-3xl font-serif mb-10;
}

.icon {
  @apply w-10 h-10 flex justify-center items-center text-white text-2xl;
}

.link {
  @apply flex items-center w-full p-4 uppercase text-white font-semibold;
}

.link:hover {
  @apply bg-indigo-500;
}

.router-link-active {
  @apply bg-indigo-500;
}
</style>
