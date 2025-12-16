<script lang="ts" setup>
import { onMounted } from 'vue'

import { useCartStore } from '@/features/cart'
import { CartEmpty } from '@/features/cart'

import { CartItem, CartActions, CartInfo } from '@/widgets/cart'
import { Title, Loading } from '@/shared/ui'
import { useModalStore } from '@/shared/stores'

const cartStore = useCartStore()
const modalStore = useModalStore()

const handleCheckout = () => {
  modalStore.modalProceedCart.show = true
}

const handleClearCart = () => {
  modalStore.modalClearCart.show = true
}

onMounted(async () => {
  await cartStore.fetchCartDetails()
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <Title title="Shopping Cart" description="Review your items before checkout" />

      <Loading v-if="cartStore.loading" text="Loading cart..." />
      <CartEmpty v-else-if="!cartStore.hasItems" />

      <!-- Содержимое корзины -->
      <div v-else class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <!-- Список товаров -->
        <div class="lg:col-span-2 space-y-6">
          <CartItem
            v-for="item in cartStore.cartDetails?.items"
            :key="item.product_id"
            :item="item"
          />
        </div>

        <!-- Итоговая информация -->
        <div class="lg:col-span-1">
          <div class="bg-white border-2 border-gray-100 rounded-none p-8 shadow-sm sticky top-24">
            <h2 class="text-2xl font-bold text-black mb-8">Order Summary</h2>
            <CartInfo />
            <CartActions @proceed="handleCheckout" @clear="handleClearCart" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
