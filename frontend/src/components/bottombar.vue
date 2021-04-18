<template>
  <div class="bottombar">
    <router-link class="link" to="users">
      <i class="icon material-icons">home</i>
      <p>Inicio</p></router-link
    >
    <router-link class="link" to="message"
      ><i class="icon material-icons">message</i>
      <p>Mensajes</p></router-link
    >
    <router-link class="link" to="profile"
      ><i class="icon material-icons">perm_identity</i>
      <p>Cuenta</p></router-link
    >
    <router-link class="link" to="login"
      ><i class="icon material-icons">logout</i>
      <p>Salir</p></router-link
    >
  </div>
</template>

<style lang="postcss" scoped>

.bottombar {
  @apply fixed bottom-0 w-full flex md:hidden bg-indigo-700 text-white justify-evenly;
}

.link {
  @apply w-full py-2 flex flex-col justify-center items-center text-xs;
}

</style>
