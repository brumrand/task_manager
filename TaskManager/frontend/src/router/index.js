import Vue from 'vue'
import Router from 'vue-router'
import TaskForm from '@/components/Task/TaskForm';
import TaskList from '@/components/Task/TaskList';

Vue.use(Router)

export default new Router({
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
    }
  ],
  mode: 'history'
})
