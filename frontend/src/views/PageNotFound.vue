<template>
  <div class="relative">
    <div class="container">
      <div class="content">
        <h1 class="title">Página no encontrada</h1>
        <h3 class="subtitle">
          Parece que no existe lo que estabas buscando
        </h3>
        <div class="image"></div>
      </div>
    </div>
  </div>
</template>

<style lang="postcss" scoped>
.container {
  @apply mb-16 md:mb-0 w-screen max-w-full flex;
}

.content {
  @apply overflow-y-scroll h-screen w-full p-8 md:px-2 md:px-10;
}
.title {
  @apply mt-8 mb-2 font-bold text-4xl;
}

.subtitle {
  @apply mb-8 font-semibold text-xl;
}


.image {
  background-image: url(../assets/404-Page.gif);
  background-position: center center;
  background-size: contain;
  background-repeat: no-repeat;
  
  @apply w-full h-4/6;
}

</style>
