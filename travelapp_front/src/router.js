import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import LogIn from './components/LogIn.vue' /*importar los componentes*/
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Account from './components/Account.vue'
import Flight from './components/Flight.vue'
import Booking from './components/Booking.vue'
import FlightCreate from './components/FlightCreate.vue'
import FlightUpdate from './components/FlightUpdate.vue'

const routes = [{
        path: '/',
        name: 'root',
        component: App
    },
    {
        path: '/user/logIn',
        name: "logIn",
        component: LogIn
    },
    {
        path: '/user/home',
        name: "home",
        component: Home
    },
    {
        path: '/user/signUp',
        name: "signUp",
        component: SignUp
    },

    {
        path: '/user/account',
        name: "account",
        component: Account
    },
    {
        path: '/flight',
        name: "flight",
        component: Flight
    },
    {
        path: '/user/booking',
        name: "booking",
        component: Booking
    },
    {
        path: '/create-flight',
        name: "createflight",
        component: FlightCreate
    },
    {
        path: '/update-flight',
        name: "updateflight",
        component: FlightUpdate
    },
]
const router = createRouter({
    history: createWebHistory(),
    routes,
})
export default router;