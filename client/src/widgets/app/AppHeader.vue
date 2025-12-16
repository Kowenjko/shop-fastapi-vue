<script lang="ts" setup>
import { useCartStore } from '@/features/cart'
import { IconCart, ButtonLink } from '@/shared/ui'
import { links } from '@/app/router'

const cartStore = useCartStore()
</script>

<template>
  <header class="bg-white border-b-2 border-black sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4">
      <div class="flex items-center justify-between h-20">
        <!-- Логотип -->
        <button-link :to="links.HOME_LINK" class="flex items-center space-x-2 group">
          <IconCart class="h-8 w-8 group-hover:scale-110 transition-transform" />
          <span class="text-2xl font-bold text-black">FastAPI Shop</span>
        </button-link>

        <!-- Навигация -->
        <nav class="flex items-center space-x-8">
          <button-link
            text="About"
            :to="links.ABOUT_LINK"
            class="text-gray-700 hover:text-black transition-colors font-medium"
          />

          <!-- Корзина -->
          <button-link
            text="Cart"
            :to="links.CART_LINK"
            class="relative flex items-center space-x-2 text-gray-700 hover:text-black transition-colors font-medium"
            :badge="cartStore.itemsCount"
          >
            <IconCart class="h-6 w-6" />
          </button-link>
        </nav>
      </div>
    </div>
  </header>
</template>
