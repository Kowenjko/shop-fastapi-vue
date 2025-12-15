<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { ProductDetailCart } from '@/widgets/product'
import { useProductsStore } from '@/entities/product'
import { useCartStore } from '@/features/cart'

import { ButtonBack } from '@/shared/ui'
import { LoadingProduct, LoadingError } from '@/shared/ui'
import { links } from '@/app/router'

import type { ProductI } from '@/entities/product'

const route = useRoute()
const router = useRouter()
const productsStore = useProductsStore()
const cartStore = useCartStore()

// State
const product = ref<ProductI | null>(null)
const loading = ref(false)
const error = ref<string | null>(null)
const adding = ref(false)
const showNotification = ref(false)

async function loadProduct() {
  loading.value = true
  error.value = null

  try {
    const productId = +route.params.id!
    product.value = await productsStore.fetchProductById(productId)
  } catch (err) {
    error.value = 'Product not found'
    console.error('Error loading product:', err)
  } finally {
    loading.value = false
  }
}

const handleAddToCart = async () => {
  if (!product.value) return
  adding.value = true
  const success = await cartStore.addToCart(product.value.id, 1)

  if (success) {
    showNotification.value = true
    setTimeout(() => {
      showNotification.value = false
    }, 3000)
  }

  adding.value = false
}

onMounted(async () => {
  await loadProduct()
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <ButtonBack @click="router.push(links.HOME_LINK)" />

      <!-- Состояние загрузки -->
      <LoadingProduct v-if="loading" />
      <LoadingError v-else-if="error" :is-button-back="true" :error :to="links.HOME_LINK" />

      <!-- Детальная информация о товаре -->
      <ProductDetailCart
        v-else-if="product"
        :product
        :adding
        :showNotification
        @add-to-cart="handleAddToCart"
      />
    </div>
  </div>
</template>
