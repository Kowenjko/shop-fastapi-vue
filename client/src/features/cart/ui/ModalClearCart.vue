<script lang="ts" setup>
import { Modal, Button, IconClose } from '@/shared/ui'
import { useModalStore } from '@/shared/stores'
import { useCartStore } from '@/features/cart/stores'

const modalStore = useModalStore()
const cartStore = useCartStore()

const hideModal = () => (modalStore.modalClearCart.show = false)
const clearCart = () => {
  cartStore.clearCart()
  hideModal()
}
</script>

<template>
  <Modal v-model:open="modalStore.modalClearCart.show">
    <div class="min-w-lg bg-white text-black p-5 rounded-lg relative">
      <button class="absolute top-2 right-2 hover:scale-110 transition-all" @click="hideModal">
        <IconClose class="size-6 text-black" />
      </button>
      <div class="py-4 text-2xl text-center font-bold">Clear Cart</div>
      <p class="pb-4 text-center">Are you sure you want to clear your cart?</p>
      <div class="flex gap-2">
        <Button text="Clear Cart" @on-click="clearCart" variant="destructive" />
        <Button text="Cancel" @on-click="hideModal" />
      </div>
    </div>
  </Modal>
</template>
