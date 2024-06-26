import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import TaskForm from '@/components/Task/TaskForm.vue';
import TaskList from '@/components/Task/TaskList.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'TaskForm',
      component: TaskForm
    },
    {
      path: '/listLastSevenDays',
      name: 'see',
      component: TaskList
    },
    {
      path: '/list',
      name: 'list',
      component: TaskList
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    }
  ],
  mode: 'history'
})

export default router
