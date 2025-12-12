import { apiClient } from '@/shared/api'
import { CART, ADD, REMOVE, UPDATE } from '@/shared/config'

import type { CartI, AddToCartI, ResponseCartI } from '../model'

export const cartAPI = {
  async addItem(item: AddToCartI, cartData: CartI) {
    return await apiClient.post<{ cart: CartI }>(CART + ADD, {
      product_id: item.product_id,
      quantity: item.quantity,
      cart: cartData,
    })
  },

  async getCart(cartData: { cart: CartI }) {
    return await apiClient.post<ResponseCartI>(CART, cartData)
  },

  async updateItem(item: AddToCartI, cartData: CartI) {
    return await apiClient.put(CART + UPDATE, {
      product_id: item.product_id,
      quantity: item.quantity,
      cart: cartData,
    })
  },

  async removeItem(productId: number, cartData: CartI) {
    return await apiClient.delete(CART + REMOVE + productId + '/', {
      data: { cart: cartData },
    })
  },
}
