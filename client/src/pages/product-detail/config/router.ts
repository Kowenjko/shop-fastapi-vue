import type { RouteRecordRaw, RouteLocationRaw } from 'vue-router'

const PRODUCT_DETAIL_ROUTE_NAME = 'product-detail'

export const PRODUCT_DETAIL_LINK = {
  name: PRODUCT_DETAIL_ROUTE_NAME,
} as const satisfies RouteLocationRaw

export const PRODUCT_DETAILS_ROUTE = {
  path: 'product/:id',
  name: PRODUCT_DETAIL_LINK.name,
  meta: {
    title: 'Product Details',
  },
  component: () => import('@/pages/product-detail/ui'),
} as const satisfies RouteRecordRaw
