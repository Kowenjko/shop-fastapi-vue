<script lang="ts" setup>
import { computed } from 'vue'
import { useProductsStore } from '@/entities/product'
import { ButtonCategory } from '@/shared/ui'

const productsStore = useProductsStore()

const totalProductsCount = computed(() => {
  return productsStore.products.length
})

const selectCategory = (categoryId: number | null) => {
  if (categoryId === null) {
    productsStore.clearCategoryFilter()
  } else {
    productsStore.setCategory(categoryId)
  }
}
</script>

<template>
  <div class="bg-white border-2 border-gray-200 rounded-lg p-6">
    <h2 class="text-2xl font-bold text-black mb-6">Categories</h2>

    <ul class="space-y-2">
      <li>
        <ButtonCategory
          :is-active="!productsStore.selectedCategory"
          name="All Categories"
          :count="totalProductsCount"
          @select-category="selectCategory(null)"
        />
      </li>

      <li v-for="category in productsStore.categories" :key="category.id">
        <ButtonCategory
          :is-active="productsStore.selectedCategory === category.id"
          :name="category.name"
          :count="productsStore.productsCount"
          @select-category="selectCategory(category.id!)"
        />
      </li>
    </ul>
  </div>
</template>
