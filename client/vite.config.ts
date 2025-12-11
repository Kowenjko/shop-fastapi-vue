// frontend/vite.config.js
/**
 * Конфигурация Vite для Vue проекта.
 * Настройка dev сервера и алиасов путей.
 */

import { fileURLToPath, URL } from 'node:url'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    host: '0.0.0.0',
    port: 5173,
    strictPort: true,

    hmr: {
      host: 'shop.local', // указываем домен для HMR
      protocol: 'ws',
      port: 5173,
    },
    proxy: {
      '/api': {
        target: 'https://api.shop.local',
        changeOrigin: true,
      },
    },
  },
})
