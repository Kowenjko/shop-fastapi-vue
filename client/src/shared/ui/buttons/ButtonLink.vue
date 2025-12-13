<script setup lang="ts">
const {
  text = '',
  badge,
  to,
} = defineProps<{ to: string | { name: string }; text?: string; badge?: number }>()
</script>

<template>
  <router-link
    :to
    class="relative flex items-center space-x-2 text-gray-700 hover:text-black transition-colors font-medium"
  >
    <slot />

    <span v-if="text">{{ text }}</span>

    <!-- Счетчик товаров -->
    <span
      v-if="badge && badge > 0"
      class="absolute -top-2 -right-2 bg-black text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center"
    >
      {{ badge }}
    </span>
  </router-link>
</template>
