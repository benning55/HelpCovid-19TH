import Vue from 'vue'
import App from './App.vue'
import '@/assets/css/tailwind.css'
import './registerServiceWorker'
import router from './router'
import store from './store'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import './assets/css/element-variables.scss'
import locale from 'element-ui/lib/locale/lang/th'
import SimpleValidation from 'simple-vue-validator';
import VueAxios from "vue-axios";
import axios from 'axios';
import VueSession from "vue-session/index.esm";
import VueAwesomeSwiper from 'vue-awesome-swiper'
import 'swiper/css/swiper.min.css'

import VueSessionStorage from 'vue-sessionstorage'
Vue.use(VueSessionStorage)

Vue.use(VueSession)
Vue.use(VueAxios, axios)

axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'

Vue.config.productionTip = false
Vue.use(ElementUI, {locale});
Vue.use(SimpleValidation);
Vue.use(VueAwesomeSwiper, /* { default global options } */)

export const Validator = SimpleValidation.Validator; // define validator lib

new Vue({
    router,
    store,
    Validator,
    render: h => h(App)
}).$mount('#app')
