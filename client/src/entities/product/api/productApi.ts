import { apiClient } from '@/shared/api'
import { PRODUCTS, CATEGORY } from '@/shared/config'

import type { ProductI, AllProductI } from '../model'

export const productsAPI = {
  async getAll() {
    return await apiClient.get<AllProductI>(PRODUCTS)
  },

  async getById(id: number) {
    return await apiClient.get<ProductI>(PRODUCTS + id)
  },

  async getByCategory(categoryId: number) {
    return await apiClient.get(PRODUCTS + CATEGORY + categoryId)
  },
}
