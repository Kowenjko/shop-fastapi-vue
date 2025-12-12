<script lang="ts" setup>
import { onMounted } from 'vue'
import { RouterView } from 'vue-router'

import { useCartStore } from '@/features/cart'

const cartStore = useCartStore()

onMounted(() => {
  cartStore.initCart()
})
</script>

<template>
  <RouterView />
</template>
