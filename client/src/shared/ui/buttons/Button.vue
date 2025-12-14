<script lang="ts" setup>
const {
  disabled = false,
  text,
  isShowTransition = false,
  textNotification = '',
} = defineProps<{
  disabled?: boolean
  text: string
  isShowTransition: boolean
  textNotification?: string
}>()

const emit = defineEmits<{ onClick: [] }>()

const onClick = () => emit('onClick')
</script>

<template>
  <button
    @click="onClick"
    :disabled
    class="w-full bg-black text-white py-3 px-4 rounded-lg hover:bg-gray-800 transition-colors disabled:opacity-50 disabled:cursor-not-allowed font-medium"
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
