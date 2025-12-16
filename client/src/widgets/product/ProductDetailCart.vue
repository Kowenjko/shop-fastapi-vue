<script lang="ts" setup>
import type { ProductI } from '@/entities/product'

import { formatDate, handleImageError } from '@/shared/lib'

const {
  product,
  adding = false,
  showNotification = false,
} = defineProps<{ product: ProductI; adding?: boolean; showNotification?: boolean }>()

const emit = defineEmits<{ addToCart: [] }>()

const addToCart = () => emit('addToCart')
</script>

<template>
  <div class="bg-white border-2 border-gray-100 rounded-none shadow-sm overflow-hidden">
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 p-8">
      <!-- Изображение -->
      <div class="aspect-square overflow-hidden rounded-none bg-gray-50">
        <img
          :src="product.image_url"
          :alt="product.name"
          class="w-full h-full object-cover"
          @error="handleImageError"
        />
      </div>

      <!-- Информация -->
      <div class="flex flex-col">
        <!-- Категория -->
        <div class="text-sm text-gray-500 uppercase tracking-wider mb-3 font-medium">
          {{ product.category.name }}
        </div>

        <!-- Название -->
        <h1 class="text-3xl sm:text-4xl font-extrabold text-black mb-4">
          {{ product.name }}
        </h1>

        <!-- Цена -->
        <div class="text-2xl sm:text-3xl font-bold text-black mb-6">
          ${{ product.price.toFixed(2) }}
        </div>

        <!-- Описание -->
        <div class="mb-8">
          <h2 class="text-xl font-bold text-black mb-3">Description</h2>
          <p class="text-gray-600 leading-relaxed">
            {{ product.description || 'No description available.' }}
          </p>
        </div>

        <!-- Кнопка добавления в корзину -->
        <div class="mt-auto">
          <button
            @click="addToCart"
            :disabled="adding"
            class="w-full bg-black text-white py-4 px-6 text-lg font-semibold rounded-none hover:bg-gray-900 transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ adding ? 'Adding to cart...' : 'Add to Cart' }}
          </button>

          <!-- Уведомление об успешном добавлении -->
          <transition name="fade">
            <div
              v-if="showNotification"
              class="mt-4 bg-black text-white px-4 py-3 rounded-none text-center font-medium"
            >
              ✓ Product added to cart!
            </div>
          </transition>
        </div>

        <!-- Дополнительная информация -->
        <div class="mt-8 pt-6 border-t-2 border-gray-100">
          <p class="text-sm text-gray-500">Product ID: {{ product.id }}</p>
          <p class="text-sm text-gray-500">Added: {{ formatDate(product.created_at) }}</p>
        </div>
      </div>
    </div>
  </div>
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
