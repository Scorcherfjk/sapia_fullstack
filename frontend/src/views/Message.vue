<template>
  <div class="relative">
    <div class="container">
      <Sidebar />
      <div class="content">
        <h1 class="title">Mensajes</h1>
        <h3 class="subtitle">
          Estamos trabajando para brindarte este beneficio lo más pronto posible
        </h3>
        <div class="image"></div>
      </div>
    </div>
    <bottombar />
  </div>
</template>

<script>
import Sidebar from "../components/sidebar";
import Bottombar from "../components/bottombar";

export default {
  components: {
    Sidebar,
    Bottombar,
  },
};
</script>

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
  background-image: url(../assets/working.gif);
  background-position: center center;
  background-size: contain;
  background-repeat: no-repeat;
  
  @apply w-full h-4/6;
}

</style>
