import { createApp } from 'vue'
import App from './App.vue'
import { PerfectScrollbarPlugin } from 'vue3-perfect-scrollbar';
import 'vue3-perfect-scrollbar/style.css';

createApp(App).use(PerfectScrollbarPlugin).mount('#app')
