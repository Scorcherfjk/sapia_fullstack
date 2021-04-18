<template>
  <div v-show="open" class="overlay">
    <div class="card">
      <div class="header">
        <p>Perfil</p>
        <button @click="close">&times;</button>
      </div>
      <div class="content">
        <h2 class="name">{{ user.name }} {{ user.lastname }}</h2>
        <p class="description">
          {{ user.bio }}
        </p>

        <div class="table">
          <div class="cell">
            <i class="icon material-icons">school</i>
            <p class="detail">{{ user.program }}</p>
          </div>
          <div class="cell">
            <i class="icon material-icons">room</i>
            <p class="detail">{{ user.headquarter }}</p>
          </div>
          <div class="cell">
            <i class="icon material-icons">call</i>
            <p class="detail">+51 {{ user.phone_number }}</p>
          </div>
          <div class="cell">
            <i class="icon material-icons">email</i>
            <p class="detail">{{ user.email }}</p>
          </div>
        </div>
      </div>
      <div class="footer">
        <router-link class="button" to="message">Enviar Mensaje</router-link>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      default: () => ({
        name: "nombre",
        lastname: "apellido",
        bio: "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Deleniti, corporis eligendi voluptate facere ducimus, dolores amet, laboriosam nulla reprehenderit officia expedita vero provident impedit quis vel repellendus! Consequatur, vel exercitationem.",
        program: "Programa de especializacion",
        hearquarter: "Sede",
        phone_number: "999 999 999",
        email: "email@test.com",
      }),
    },
    open: {
      type: Boolean,
      default: true
    },
    close: {
      type: Function,
      default: () => {}
    }
  },
};
</script>

<style lang="postcss" scoped>
.overlay {
  @apply w-screen h-screen;
  @apply fixed top-0 left-0 flex justify-center items-center;
  @apply bg-gray-900;
  --tw-bg-opacity: 0.7;
}

.card {
  @apply flex flex-col justify-between rounded-lg h-3/4 w-5/6 md:w-2/4 lg:w-1/3 xl:w-1/4 bg-white;
}

.header {
  @apply h-16 pl-6 pr-2;
  @apply flex justify-between items-center;
  @apply bg-gray-200 rounded-t-lg border-b-2 border-gray-500;
}

.header p {
  @apply text-black font-semibold uppercase;
}

.header button {
  outline: 0;
  @apply w-10 h-10 text-black text-2xl;
}

.content {
  @apply w-full overflow-y-scroll p-6;
}

.name {
  @apply mb-6 text-lg text-black font-semibold uppercase;
}

.table {
  @apply flex flex-col my-6;
}

.cell {
  @apply flex justify-start items-center;
}

.icon {
  @apply w-10 h-10 flex justify-center items-center text-indigo-700 text-2xl;
}

.footer {
  @apply p-6;
}

.button {
  outline: 0;
  @apply block text-center w-full my-2 p-2 rounded-full bg-indigo-700 text-white font-semibold;
}
</style>
