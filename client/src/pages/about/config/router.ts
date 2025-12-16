import type { RouteRecordRaw, RouteLocationRaw } from 'vue-router'

const ABOUT_ROUTE_NAME = 'about'

export const ABOUT_LINK = {
  name: ABOUT_ROUTE_NAME,
} as const satisfies RouteLocationRaw

export const ABOUT_ROUTE = {
  path: 'about',
  name: ABOUT_LINK.name,
  meta: {
    title: 'About - page',
  },
  component: () => import('@/pages/about/ui'),
} as const satisfies RouteRecordRaw
