<script lang="ts" setup>
import { onMounted } from 'vue'

import { ProductCard, CategoryFilter, InfoFilter } from '@/widgets/product'
import { useProductsStore } from '@/entities/product'
import { LoadingProduct, LoadingError, ProductNoFound } from '@/entities/product'
import { Title } from '@/shared/ui'

const productsStore = useProductsStore()

onMounted(async () => {
  await Promise.allSettled([productsStore.fetchProducts(), productsStore.fetchCategories()])
})
</script>

<template>
  <div class="min-h-screen bg-white">
    <div class="max-w-7xl mx-auto px-4 py-8">
      <Title title="Product Catalog" description="Discover our amazing products" />

      <div class="flex gap-8">
        <aside class="w-64 shrink-0">
          <CategoryFilter />
        </aside>

        <main class="grow">
          <InfoFilter
            :products-count="productsStore.productsCount"
            :selected-category="productsStore.selectedCategory"
            @clear-filter="productsStore.clearCategoryFilter"
          />

          <LoadingProduct v-if="productsStore.loading" />
          <LoadingError v-else-if="productsStore.error" :error="productsStore.error" />

          <div
            v-else-if="productsStore.filteredProducts.length > 0"
            class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6"
          >
            <ProductCard
              v-for="product in productsStore.filteredProducts"
              :key="product.id"
              :product="product"
            />
          </div>

          <ProductNoFound v-else @clear-filter="productsStore.clearCategoryFilter" />
        </main>
      </div>
    </div>
  </div>
</template>
