<script lang="ts" setup>
import { useCartStore } from '@/features/cart'
const cartStore = useCartStore()
</script>

<template>
  <div class="space-y-6 mb-8">
    <div class="flex justify-between text-lg text-gray-600">
      <span>Items ({{ cartStore.cartDetails?.items_count }})</span>
      <span>${{ cartStore.totalPrice.toFixed(2) }}</span>
    </div>

    <div class="flex justify-between text-lg text-gray-600">
      <span>Shipping</span>
      <span class="text-green-600 font-medium">Free</span>
    </div>

    <div class="border-t-2 border-gray-100 pt-6">
      <div class="flex justify-between text-xl font-bold text-black">
        <span>Total</span>
        <span>${{ cartStore.totalPrice.toFixed(2) }}</span>
      </div>
    </div>
  </div>
</template>
