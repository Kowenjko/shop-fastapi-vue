<script lang="ts" setup>
const { text = 'Loading products...' } = defineProps<{ text?: string }>()
</script>

<template>
  <div class="text-center py-12">
    <div class="inline-block animate-spin rounded-none h-12 w-12 border-b-2 border-black"></div>
    <p class="mt-4 text-gray-500">{{ text }}</p>
  </div>
</template>
