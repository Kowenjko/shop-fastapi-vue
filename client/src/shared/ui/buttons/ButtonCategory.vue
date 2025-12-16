<script setup lang="ts">
const { isActive, name, count } = defineProps<{ isActive: boolean; name: string; count: number }>()

const emit = defineEmits<{ selectCategory: [] }>()
const selectCategory = () => emit('selectCategory')
</script>

<template>
  <button
    @click="selectCategory"
    :class="[
      'w-full text-left px-4 py-3 rounded-lg transition-all duration-200',
      isActive ? 'bg-black text-white font-semibold' : 'bg-gray-50 hover:bg-gray-100 text-gray-700',
    ]"
  >
    {{ name }}
    <span v-if="isActive" class="float-right"> ({{ count }}) </span>
  </button>
</template>
