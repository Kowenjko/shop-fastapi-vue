/**
 * Конфигурация Vue Router.
 * Определяет маршруты приложения и связывает их с компонентами.
 */

import { createRouter, createWebHistory } from 'vue-router'

import { HOME_ROUTE, HOME_LINK } from '@/pages/home/config'
import { PRODUCT_DETAILS_ROUTE, PRODUCT_DETAIL_LINK } from '@/pages/product-detail/config'
import { CART_ROUTE, CART_LINK } from '@/pages/cart/config'
import { ABOUT_ROUTE, ABOUT_LINK } from '@/pages/about/config'

export const links = { HOME_LINK, PRODUCT_DETAIL_LINK, CART_LINK, ABOUT_LINK }

export const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [HOME_ROUTE, PRODUCT_DETAILS_ROUTE, CART_ROUTE, ABOUT_ROUTE],
  //Прокрутка страницы вверх при переходе между роутами
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  },
})

// Обновление заголовка страницы при навигации
router.beforeEach((to, from, next) => {
  document.title = (to.meta.title as string) || 'FastAPI Shop'
  next()
})
