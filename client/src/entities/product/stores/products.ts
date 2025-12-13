import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { productsAPI, categoriesAPI } from '@/entities/product'
import type { ProductI, CategoryI } from '@/entities/product'

export const useProductsStore = defineStore('products', () => {
  // State
  const products = ref<ProductI[]>([])
  const categories = ref<CategoryI[]>([])
  const selectedCategory = ref<number | null>(null)
  const loading = ref(false)
  const error = ref<string | null>(null)

  // Getters
  const filteredProducts = computed(() => {
    if (!selectedCategory.value) {
      return products.value
    }
    return products.value.filter((product) => product.category_id === selectedCategory.value)
  })

  const productsCount = computed(() => filteredProducts.value.length)

  // Actions
  /**
   * Загрузить все товары с сервера
   */
  const fetchProducts = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await productsAPI.getAll()
      products.value = response.data.products
    } catch (err) {
      error.value = 'Failed to load products'
      console.error('Error fetching products:', err)
    } finally {
      loading.value = false
    }
  }

  /**
   * Загрузить товар по ID
   */
  const fetchProductById = async (id: number) => {
    loading.value = true
    error.value = null
    try {
      const response = await productsAPI.getById(id)
      return response.data
    } catch (err) {
      error.value = 'Failed to load product'
      console.error('Error fetching product:', err)
      throw err
    } finally {
      loading.value = false
    }
  }

  /**
   * Загрузить все категории
   */
  const fetchCategories = async () => {
    try {
      const response = await categoriesAPI.getAll()
      categories.value = response.data
    } catch (err) {
      console.error('Error fetching categories:', err)
    }
  }

  /**
   * Установить фильтр по категории
   */
  const setCategory = (categoryId: number) => {
    selectedCategory.value = categoryId
  }

  /**
   * Сбросить фильтр категории
   */
  const clearCategoryFilter = () => {
    selectedCategory.value = null
  }

  return {
    // State
    products,
    categories,
    selectedCategory,
    loading,
    error,
    // Getters
    filteredProducts,
    productsCount,
    // Actions
    fetchProducts,
    fetchProductById,
    fetchCategories,
    setCategory,
    clearCategoryFilter,
  }
})
