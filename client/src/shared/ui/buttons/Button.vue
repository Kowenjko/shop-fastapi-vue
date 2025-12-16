<script lang="ts" setup>
import { computed } from 'vue'

const {
  disabled = false,
  text,
  isShowTransition = false,
  textNotification = '',
  variant = 'default',
} = defineProps<{
  disabled?: boolean
  text: string
  isShowTransition?: boolean
  textNotification?: string
  variant?: 'default' | 'destructive'
}>()

const emit = defineEmits<{ onClick: [] }>()

const onClick = () => emit('onClick')

const classes = computed(() => {
  if (variant === 'destructive')
    return 'bg-white border border-red-500 text-red-500 hover:bg-red-200'
  return 'bg-black text-white hover:bg-gray-800'
})
</script>

<template>
  <button
    @click="onClick"
    :disabled
    class="w-full py-3 px-4 rounded-lg transition-colors disabled:opacity-50 disabled:cursor-not-allowed font-medium"
    :class="classes"
  >
    {{ text }}
  </button>
  <transition name="fade">
    <div v-if="isShowTransition" class="mt-2 text-sm text-green-600 text-center font-medium">
      {{ textNotification }}
    </div>
  </transition>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
