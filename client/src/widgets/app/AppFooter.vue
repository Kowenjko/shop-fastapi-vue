<script lang="ts" setup>
const nowDate = new Date()
</script>

<template>
  <footer class="bg-white border-t-2 border-black mt-16">
    <div class="max-w-7xl mx-auto px-4 py-8">
      <div class="text-center text-gray-600">
        <p class="mb-2">© {{ nowDate.getFullYear() }} FastAPI Shop. All rights reserved.</p>
        <p class="text-sm">Built with FastAPI + Vue.js</p>
      </div>
    </div>
  </footer>
</template>
