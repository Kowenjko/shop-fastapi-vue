<script lang="ts" setup>
const { subtotal } = defineProps<{ subtotal: number }>()
</script>

<template>
  <div class="text-right">
    <p class="text-xl font-bold text-black">${{ subtotal.toFixed(2) }}</p>
  </div>
</template>
