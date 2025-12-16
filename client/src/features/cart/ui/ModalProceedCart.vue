<script lang="ts" setup>
import { Modal, Button, IconClose } from '@/shared/ui'
import { useModalStore } from '@/shared/stores'

const modalStore = useModalStore()

const hideModal = () => (modalStore.modalProceedCart.show = false)
</script>

<template>
  <Modal v-model:open="modalStore.modalProceedCart.show">
    <div class="min-w-lg bg-white text-black p-5 rounded-lg relative">
      <button class="absolute top-2 right-2 hover:scale-110 transition-all" @click="hideModal">
        <IconClose class="size-6 text-black" />
      </button>
      <div class="py-4 text-2xl text-center font-bold">Modal Proceed</div>
      <p class="pb-4 text-center">Checkout functionality will be implemented soon!</p>
      <Button text="Proceed to Checkout" @on-click="hideModal" />
    </div>
  </Modal>
</template>
