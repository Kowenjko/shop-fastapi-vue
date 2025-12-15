<script lang="ts" setup>
import { links } from '@/app/router'

const emit = defineEmits<{ proceed: []; clear: [] }>()

const proceed = () => emit('proceed')
const clear = () => emit('clear')
</script>

<template>
  <button
    class="w-full bg-black text-white py-4 px-6 text-lg font-semibold rounded-none hover:bg-gray-900 transition-colors mb-4"
    @click="proceed"
  >
    Proceed to Checkout
  </button>

  <router-link
    :to="links.HOME_LINK"
    class="block w-full bg-gray-100 text-black py-4 px-6 text-lg font-semibold rounded-none hover:bg-gray-200 transition-colors text-center"
  >
    Continue Shopping
  </router-link>

  <button
    @click="clear"
    class="w-full mt-6 text-base text-red-600 hover:text-red-700 transition-colors font-medium"
  >
    Clear Cart
  </button>
</template>
