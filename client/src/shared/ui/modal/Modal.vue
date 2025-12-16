<script setup lang="ts">
import { IconClose } from '@/shared/ui'

const { isCloseOutside = true } = defineProps<{ isCloseOutside?: boolean }>()

const open = defineModel('open')

const clickOutside = () => {
  if (!isCloseOutside) return

  open.value = false
}
</script>

<template>
  <div
    class="fixed top-0 left-0 bg-black/90 transition-all duration-300 z-50 w-full h-screen opacity-0 scale-0 flex justify-center items-center"
    :class="{ 'opacity-100 scale-100': open }"
    @click.self="clickOutside"
  >
    <button class="absolute top-4 right-4 text-black" @click="open = false">
      <IconClose class="size-8 text-white" />
    </button>
    <slot />
  </div>
</template>
