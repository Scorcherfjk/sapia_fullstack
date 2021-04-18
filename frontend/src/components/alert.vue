<template>
  <div class="overlay">
    <p :class="'alert ' + type">
      {{ content }}
    </p>
  </div>
</template>

<script>
export default {
  props: {
    type: String,
    content: String,
  },
};
</script>

<style lang="postcss" scoped>
.overlay {
  @apply absolute top-4 right-4;
}

.alert {
  @apply px-4 py-2 rounded-lg text-white text-xl;
}

.error {
  @apply bg-red-400;
}

.success {
  @apply bg-green-500;
}

.loading {
  @apply bg-gray-500;
}
</style>
