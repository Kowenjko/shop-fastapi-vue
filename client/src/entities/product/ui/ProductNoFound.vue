<script lang="ts" setup>
import { IconNoProductFound } from '@/shared/ui'

const emit = defineEmits<{ clearFilter: [] }>()

const clearFilter = () => emit('clearFilter')
</script>

<template>
  <div class="text-center py-12">
    <IconNoProductFound />
    <p class="text-gray-500 text-lg font-medium">No products found</p>
    <button @click="clearFilter" class="mt-4 text-black hover:underline font-medium">
      View all products
    </button>
  </div>
</template>
