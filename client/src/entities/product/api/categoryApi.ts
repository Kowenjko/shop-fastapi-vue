import { apiClient } from '@/shared/api'
import { CATEGORIES } from '@/shared/config'

import type { CategoryI } from '../model'

export const categoriesAPI = {
  getAll() {
    return apiClient.get<CategoryI[]>(CATEGORIES)
  },

  getById(id: number) {
    return apiClient.get<CategoryI>(CATEGORIES + id + '/')
  },
}
