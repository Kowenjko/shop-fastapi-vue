import { apiClient } from '@/shared/api'
import { PRODUCTS, CATEGORY } from '@/shared/config'

import type { ProductI, AllProductI } from '../model'

export const productsAPI = {
  getAll() {
    return apiClient.get<AllProductI>(PRODUCTS)
  },

  getById(id: number) {
    return apiClient.get<ProductI>(PRODUCTS + id + '/')
  },

  getByCategory(categoryId: number) {
    return apiClient.get(PRODUCTS + CATEGORY + categoryId + '/')
  },
}
