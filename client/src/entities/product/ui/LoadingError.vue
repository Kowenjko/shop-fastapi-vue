<script lang="ts" setup>
const { error } = defineProps<{ error: string }>()
</script>

<template>
  <div class="text-center py-12">
    <p class="text-red-600 font-medium">{{ error }}</p>
  </div>
</template>
