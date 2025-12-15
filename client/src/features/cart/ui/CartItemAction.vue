<script lang="ts" setup>
import { IconMinus, IconPlus, IconTrash } from '@/shared/ui'

const { quantity, updating } = defineProps<{ quantity: number; updating: boolean }>()

const emit = defineEmits<{ minus: []; plus: []; remove: [] }>()

const minus = () => emit('minus')
const plus = () => emit('plus')
const remove = () => emit('remove')
</script>

<template>
  <div class="flex items-center gap-4">
    <div class="flex items-center border-2 border-gray-100 rounded-none text-black">
      <button
        @click="minus"
        :disabled="updating"
        class="px-3 py-2 hover:bg-gray-100 transition-colors disabled:opacity-50"
      >
        <IconMinus class="h-5 w-5" />
      </button>

      <span class="px-4 py-2 font-medium min-w-[40px] text-center">
        {{ quantity }}
      </span>

      <button
        @click="plus"
        :disabled="updating"
        class="px-3 py-2 hover:bg-gray-100 transition-colors disabled:opacity-50"
      >
        <IconPlus class="h-5 w-5" />
      </button>
    </div>

    <!-- Кнопка удаления -->
    <button
      @click="remove"
      :disabled="updating"
      class="text-red-600 hover:text-red-700 transition-colors disabled:opacity-50"
    >
      <IconTrash class="h-6 w-6" />
    </button>
  </div>
</template>
