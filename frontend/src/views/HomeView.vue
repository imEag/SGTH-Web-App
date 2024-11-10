<script setup>
import PageContainer from "@/components/PageContainer.vue";
import phoneImgSrc from '@/assets/images/phoneWithMessageBubble.png';
</script>

<template>
  <PageContainer>
    <div class="home">
      <div class="menu">
        <h1>Bienvenido</h1>
        <router-link to="/profesionales">
          <button class="btn">Profesionales</button>
        </router-link>
        <router-link to="/devices-list">
          <button class="btn">Equipos</button>
        </router-link>
      </div>
      <img :src="phoneImgSrc" alt="">
    </div>
  </PageContainer>
</template>

<style lang="scss" scoped>
@import "@/assets/styles/main.scss";

.home {
  display: flex;
  justify-content: center;
  align-items: flex-start;
  flex-wrap: wrap;
  gap: 30px;

  @include respond-to('tablet') {
  }

  @include respond-to('desktop') {
    flex-wrap: nowrap;

  }

  .menu {
    width: 300px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family: $questrial;
    gap: 20px;

    h1 {
      margin: 0;
    }

    .btn {
      width: 260px;
    }
  }

  img {
    width: 300px;

    @include respond-to('tablet') {
      width: 500px;
    }

    @include respond-to('desktop') {
      width: 600px;
    }
  }
}
</style>
