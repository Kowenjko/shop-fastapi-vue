import { apiClient } from '@/shared/api'
import { CATEGORIES } from '@/shared/config'

import type { CategoryI } from '../model'

export const categoriesAPI = {
  async getAll() {
    return await apiClient.get<CategoryI[]>(CATEGORIES)
  },

  async getById(id: number) {
    return await apiClient.get<CategoryI>(CATEGORIES + id)
  },
}
