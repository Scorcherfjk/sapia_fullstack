<template>
  <div class="container">
    <div class="sidebar"></div>
    <div class="content">
      <h1 class="title">Bienvenido!</h1>

      <!-- <h3 class="subtitle">Accede o regístrate</h3> -->
      <router-link class="button primary" to="login">Iniciar sesión</router-link>
      <router-link class="button secondary" to="register">Regístrate</router-link>
    </div>
  </div>
</template>

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

  @apply w-0 h-screen md:w-2/3 lg:w-2/3 xl:w-3/4;
}

.title {
  @apply mt-8 mb-8 font-bold text-4xl;
}

.subtitle {
  @apply mb-8 text-xl;
}

.button {
  @apply block w-full mb-2 p-2 rounded-full text-center font-semibold;
}

.primary {
  @apply  bg-indigo-700 text-white;
}

.secondary {
  @apply border-2 border-indigo-700 text-indigo-700;
}
</style>
