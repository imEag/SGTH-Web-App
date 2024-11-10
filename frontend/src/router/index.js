import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProfessionalsView from '@/views/ProfessionalsView.vue';
import NewResponsable from '@/views/NewResponsable.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/profesionales',
      name: 'profesionales',
      component: ProfessionalsView,
    },
    {
      path: '/new-professional',
      name: 'new-professional',
      component: NewResponsable,
    }
  ],
});

export default router;
