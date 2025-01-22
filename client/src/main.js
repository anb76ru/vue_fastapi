import { createApp } from 'vue';
import App from './App.vue';
import { Quasar } from 'quasar';
import quasarUserOptions from './quasar-user-options';
import { createRouter, createWebHistory} from 'vue-router';
import LeftNav from './components/LeftNav.vue';
import routes from './routes';

const app = createApp(App);
const router = createRouter({
    routes: routes,
    history: createWebHistory()
});

app.use(router);
app.use(Quasar, quasarUserOptions)
app.component('left-nav', LeftNav)
app.mount('#app')
