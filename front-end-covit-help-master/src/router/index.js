import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: () => import('../views/Home.vue')
    },
    {
        path: '/about',
        name: 'About',
        component: () => import('../views/About.vue')
    },
    {
        path: '/login',
        name: 'Login',
        component: () => import('../views/Login_Signup.vue')
    },
    {
        path: '/post',
        name: 'DashboardPost',
        component: () => import('../views/DashboardPost.vue')
    },
    {
        path: '/hospital',
        name: 'DashboardHospital',
        component: () => import('../views/DashboardHospital.vue')
    },
    {
        path: '/post/create',
        name: 'PostCreate',
        component: () => import('../views/PostCreate')
    },
    {
        path: '/post/edit',
        name: 'PostEdit',
        component: () => import('../views/PostEdit')
    },
    // {
    //     path: '/hospital/edit',
    //     name: 'HospitalEdit',
    //     component: () => import('../views/HospitalEdit')
    // },
    {
        path: '/all-hospital',
        name: 'DonatePageMoney',
        component: () => import('../views/DonatePageMoney')
    },{
        path: '/all-post',
        name: 'DonatePageObject',
        component: () => import('../views/DonatePageObject')
    },
    {
        path: '/donate-hospital',
        name: 'DonateMoney',
        component: () => import('../views/DonateMoney')
    },{
        path: '/donate-post',
        name: 'DonateObject',
        component: () => import('../views/DonateObject')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
})

export default router
