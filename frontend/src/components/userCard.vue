<template>

  <div class="card">
    <img :src="image" :alt="user.name" class="image">
    <div class="content">
      <p class="name">{{ completeName }}</p>
      <p class="program">{{ user.program }}</p>
      <button class="button" @click="openCloseModal">
        <i class="material-icons">add_circle_outline</i><span>Ver más</span>
      </button>
    </div>
    <modal :user="user" :open="open" :close="openCloseModal"/>
  </div>

</template>

<script>
import gravatar from "../utils/gravatar.js"
import modal from './modal.vue';

export default {
  components: { modal },
  name: "UserCard",
  props: {
    user: Object
  },
  data() {
    return {
      image: '/no-user.jpeg',
      open: false
    }
  },
  computed: {
    completeName() {
      const complete = `${this.user.name} ${this.user.lastname}`
      return complete.length > 20 ? complete.slice(0, 20) + '...' : complete
    }
  },
  mounted() {
    this.image = gravatar(this.user.email)
  },
  methods: {
    openCloseModal() {
      this.open = !this.open
    }
  }
};
</script>

<style lang="postcss" scoped>

.card {
  @apply flex flex-col justify-center items-center w-56 my-16 mx-auto sm:mx-10 rounded-3xl bg-gray-100 border-2 border-gray-200 shadow-lg;
}

.image {
  @apply w-24 -mt-12 rounded-full;
}

.content {
  @apply p-4 text-center ;
}

.name {
  @apply my-4 font-semibold text-lg capitalize;
}

.program {
  @apply my-4 font-medium text-base;
}

.button {
  @apply w-full flex items-center justify-center text-center font-semibold text-lg text-indigo-600;
}

.button span {
  @apply ml-4;
}

</style>
