<script lang="ts" setup>
import { ref } from 'vue'
import { Button } from '@/shared/ui'
import { useCartStore } from '@/features/cart'
import type { ProductI } from '@/entities/product'

import { links } from '@/app/router'

const { product } = defineProps<{ product: ProductI }>()

const cartStore = useCartStore()
const adding = ref(false)
const showNotification = ref(false)

const handleAddToCart = async () => {
  adding.value = true
  const success = await cartStore.addToCart(product.id, 1)

  if (success) {
    showNotification.value = true
    setTimeout(() => {
      showNotification.value = false
    }, 2000)
  }

  adding.value = false
}

const handleImageError = (event: Event) => {
  const img = event.target as HTMLImageElement
  img.src = 'https://via.placeholder.com/400x400?text=No+Image'
}
</script>

<template>
  <div
    class="bg-white border-2 border-gray-200 rounded-lg overflow-hidden hover:border-black transition-all duration-300 hover:shadow-lg"
  >
    <!-- Изображение товара -->
    <router-link :to="{ ...links.PRODUCT_DETAIL_LINK, params: { id: product.id } }">
      <div class="aspect-square overflow-hidden bg-gray-100">
        <img
          :src="product.image_url"
          :alt="product.name"
          class="w-full h-full object-cover hover:scale-105 transition-transform duration-300"
          @error="handleImageError"
        />
      </div>
    </router-link>

    <!-- Информация о товаре -->
    <div class="p-4">
      <!-- Категория -->
      <div class="text-xs text-gray-500 uppercase tracking-wide mb-2">
        {{ product.category.name }}
      </div>

      <!-- Название товара -->
      <router-link :to="{ ...links.PRODUCT_DETAIL_LINK, params: { id: product.id } }">
        <h3 class="text-lg font-semibold text-black mb-2 hover:text-gray-700 transition-colors">
          {{ product.name }}
        </h3>
      </router-link>

      <!-- Цена -->
      <p class="text-2xl font-bold text-black mb-4">${{ product.price.toFixed(2) }}</p>

      <Button
        @on-click="handleAddToCart"
        :disabled="adding"
        :text="adding ? 'Adding...' : 'Add to Cart'"
        :is-show-transition="showNotification"
        text-notification="✓ Added to cart!"
      />
    </div>
  </div>
</template>
