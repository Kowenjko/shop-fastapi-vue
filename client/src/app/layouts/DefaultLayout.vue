<script lang="ts" setup>
import { AppFooter, AppHeader } from '@/widgets/app'
import { ModalProceedCart, ModalClearCart } from '@/features/cart'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />
    <RouterView />
    <AppFooter />
  </div>
  <ModalProceedCart />
  <ModalClearCart />
</template>
