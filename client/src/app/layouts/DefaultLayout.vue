<script lang="ts" setup>
import Header from '@/widgets/Header.vue'
import Footer from '@/widgets/Footer.vue'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <Header />
    <RouterView />
    <Footer />
  </div>
</template>
