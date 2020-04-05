import Vue from 'vue'
import VueRouter from 'vue-router'
// import app from "../App";

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
        path: '/post/:id',
        name: 'DashboardPost',
        component: () => import('../views/DashboardPost.vue')
    },
    {
        path: '/hospital/:id',
        name: 'DashboardHospital',
        component: () => import('../views/DashboardHospital.vue')
    },
    {
        path: '/post/create',
        name: 'PostCreate',
        component: () => import('../views/PostCreate')
    },
    {
        path: '/post/edit/:id',
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
    }, {
        path: '/all-post',
        name: 'DonatePageObject',
        component: () => import('../views/DonatePageObject')
    },
    {
        path: '/donate-hospital/:id',
        name: 'DonateMoney',
        component: () => import('../views/DonateMoney')
    }, {
        path: '/donate-post/:id',
        name: 'DonateObject',
        component: () => import('../views/DonateObject')
    }, {
        path: '/search-word/:title',
        name: 'SearchPage',
        component: () => import('../views/SearchPage')
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes,
    // scrollBehavior: (to, from, savedPosition) => {
    //     console.log(savedPosition)
    //     if (savedPosition) {
    //         return savedPosition;
    //     } else if (to.hash) {
    //         return {
    //             selector: to.hash
    //         };
    //     } else {
    //         return {x: 0, y: 0};
    //     }
    // }

    scrollBehavior(to, from, savedPosition) {
        // console.log(savedPosition)
        // Default scroll position will be 0, 0 unless overridden by a saved position
        const position = {
            x: 0,
            y: 0
        };

        // Override default with saved position (if it exists)
        if (savedPosition) {
            position.x = savedPosition.x;
            position.y = savedPosition.y;
        }

        // Listen for scrollBeforeEnter event and set scroll position
        return new Promise(resolve => {

            this.app.$root.$once("scrollBeforeEnter", () => {
                console.log(position)
                resolve(position);
            });
        });
    }

})

export default router
