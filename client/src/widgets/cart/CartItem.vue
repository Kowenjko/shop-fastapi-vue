<script lang="ts" setup>
import { handleImageError } from '@/shared/lib'
import { useCartActions } from '@/features/cart'

import type { CartItemI } from '@/features/cart'

import { CartItemAction, CartItemTotal } from '@/features/cart'

const { item } = defineProps<{ item: CartItemI }>()

const { updating, increaseQuantity, decreaseQuantity, handleRemove } = useCartActions()
</script>

<template>
  <div
    class="bg-white border-2 border-gray-100 rounded-none p-6 shadow-sm hover:border-gray-300 transition-colors"
  >
    <div class="flex gap-6">
      <!-- Изображение товара -->
      <div class="w-24 h-24 shrink-0">
        <img
          :src="item.image_url"
          :alt="item.name"
          class="w-full h-full object-cover rounded-none"
          @error="handleImageError($event, '200x200')"
        />
      </div>

      <div class="grow">
        <h3 class="text-lg font-bold text-black mb-2">
          {{ item.name }}
        </h3>
        <p class="text-gray-600 text-sm mb-3">${{ item.price.toFixed(2) }} each</p>

        <CartItemAction
          :quantity="item.quantity"
          :updating
          @minus="decreaseQuantity(item)"
          @plus="increaseQuantity(item)"
          @remove="handleRemove(item)"
        />
      </div>

      <CartItemTotal :subtotal="item.subtotal" />
    </div>
  </div>
</template>
