import Calculate from './components/CalculateSumm.vue';
import HelloWorld from './components/HelloWorld.vue';
import Users from './components/UserList.vue';
const routes = [
    {
        name: "calculate",
        path: "/calculate",
        meta: { title: 'Сумма двух чисел' },
        component: Calculate
    },
    {
        name: "hw",
        path: "/hw",
        meta: { title: 'hw' },
        component: HelloWorld
    },
    {
        name: "users",
        path: "/users",
        meta: {title: "Пользователи"},
        component: Users
    }
]

export default routes