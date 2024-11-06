<script setup lang="ts">
import Header from "@/components/AppHeader.vue";
import Footer from "@/components/AppFooter.vue";
import BannerFull from "@/components/Banner/BannerFull.vue";
import {defineProps} from "vue";

const props = defineProps({
  showBanner: {
    type: Boolean,
    default: true,
  },
});
</script>

<template>
  <div class="page-container">
    <div>
      <Header/>
      <BannerFull v-if="showBanner"/>
    </div>
    <main class="main-content">
      <slot/>
    </main>
    <Footer/>
  </div>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/main.scss";

div.page-container {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  min-height: 100vh;
}

.main-content {
  flex-grow: 1;
}

</style>
