<script lang="ts" setup>
import { IconCart } from '@/shared/ui'
import { links } from '@/app/router'
</script>

<template>
  <div class="text-center py-16">
    <IconCart class="h-28 w-28 mx-auto text-gray-300 mb-6" />

    <h2 class="text-2xl font-bold text-black mb-3">Your cart is empty</h2>
    <p class="text-lg text-gray-500 mb-8">Add some products to get started!</p>
    <router-link
      :to="links.HOME_LINK"
      class="inline-block bg-black text-white py-3 px-8 text-lg font-semibold rounded-none hover:bg-gray-900 transition-colors"
    >
      Continue Shopping
    </router-link>
  </div>
</template>
