import { reactive } from 'vue'
import { defineStore } from 'pinia'

export const useModalStore = defineStore('modals', () => {
  const modalProceedCart = reactive({ show: false, content: null })
  const modalClearCart = reactive({ show: false, content: null })

  return {
    modalProceedCart,
    modalClearCart,
  }
})
