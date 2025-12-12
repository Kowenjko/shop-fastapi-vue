import type { RouteRecordRaw, RouteLocationRaw } from 'vue-router'

const CART_ROUTE_NAME = 'cart'

export const CART_LINK = {
  name: CART_ROUTE_NAME,
} as const satisfies RouteLocationRaw

export const CART_ROUTE = {
  path: 'cart',
  name: CART_LINK.name,
  meta: {
    title: 'Shopping Cart',
  },
  component: () => import('@/pages/cart/ui'),
} as const satisfies RouteRecordRaw
