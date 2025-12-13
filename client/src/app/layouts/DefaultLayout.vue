<script lang="ts" setup>
import { AppFooter, AppHeader } from '@/widgets/app'
</script>

<template>
  <div class="min-h-screen bg-gray-50">
    <AppHeader />
    <RouterView />
    <AppFooter />
  </div>
</template>
