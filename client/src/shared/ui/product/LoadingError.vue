<script lang="ts" setup>
const {
  error,
  isButtonBack = false,
  to = null,
} = defineProps<{
  error: string
  isButtonBack?: boolean
  to?: string | { name: string } | null
}>()
</script>

<template>
  <div class="text-center py-16" v-if="isButtonBack && to">
    <p class="text-red-600 text-lg font-medium pb-2">{{ error }}</p>
    <router-link
      v-if="isButtonBack && to"
      :to
      class="mt-6 bg-black text-white py-3 px-8 text-lg font-semibold rounded-none hover:bg-gray-900 transition-colors"
    >
      Return to catalog
    </router-link>
  </div>
  <div class="text-center py-12" v-else>
    <p class="text-red-600 font-medium">{{ error }}</p>
    {{ String(isButtonBack) }}
  </div>
</template>
