import {createRouter, createWebHistory} from 'vue-router';
import HomeView from '../views/HomeView.vue';
import ProfessionalsView from '@/views/ProfessionalsView.vue';
import NewResponsable from '@/views/NewResponsable.vue';
import EquipamentList from '@/views/EquipamentList.vue';
import NewEquipament from '@/views/NewEquipament.vue';
import ProfessionalView from "@/views/ProfessionalView.vue";
import EditEquipament from '@/views/EditEquipament.vue';


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
        },
        {
            path: '/devices-list',
            name: 'EquipamentList',
            component: EquipamentList,
        },
        {
            path: '/devices-create',
            name: 'NewEquipament',
            component: NewEquipament,
        },
        {
            path: '/devices/:id',
            name: 'EditEquipament',
            component: EditEquipament,
        },
        {
            path: '/professional/:id',
            name: 'professional',
            component: ProfessionalView,
        }
    ],
});

export default router;
