import type { RouteRecordRaw, RouteLocationRaw } from 'vue-router'
import HomePage from '@/pages/home/ui'

const HOME_ROUTE_NAME = 'home'

export const HOME_LINK = {
  name: HOME_ROUTE_NAME,
} as const satisfies RouteLocationRaw

export const HOME_ROUTE = {
  path: '',
  name: HOME_LINK.name,
  meta: {
    title: 'Shop - Home',
  },
  component: () => HomePage,
} as const satisfies RouteRecordRaw
