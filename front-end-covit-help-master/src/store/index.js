import Vue from 'vue'
import Vuex from 'vuex'
import VuexPersistence from 'vuex-persist'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        authUser: {
            id: -1,
            hospital: {
                id: -1,
                name: "",
                picture: "",
                address: "",
                donated_money: "",
                tel: "",
                back_account_name: "",
                bank_name: ""
            },
            email: "",
            first_name: "",
            last_name: "",
            tel: ""
        },
        isAuthenticated: false,
        jwt: localStorage.getItem('token'),
        // host: `${window.location.protocol}//${window.location.hostname}/8000`
        host: `${window.location.protocol}//${window.location.hostname}`,
        dataAllHospital:[],
        dataAllPost:[]
    },
    mutations: {
        setAuth(state, isAuthenticated) {
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        setAuthUser(state, {authUser, isAuthenticated}) {
            Vue.set(state, 'authUser', authUser)
            Vue.set(state, 'isAuthenticated', isAuthenticated)
        },
        updateToken(state, newToken) {
            localStorage.setItem('token', newToken)
            state.jwt = newToken;
        },
        removeToken(state) {
            localStorage.removeItem('token')
            state.authUser = {
                id: -1,
                hospital: {
                    id: -1,
                    name: "",
                    picture: "",
                    address: "",
                    donated_money: "",
                    tel: "",
                    back_account_name: "",
                    bank_name: ""
                },
                email: "",
                first_name: "",
                last_name: "",
                tel: ""
            }
            state.jwt = null
            state.isAuthenticated = false
        },
        setDataAllHospital(state,data){
            console.log(data)
            state.dataHome = data
        },
        setDataAllPost(state,data){
            state.dataAllPost = data
        }
    },
    actions: {},
    modules: {},
    plugins: [new VuexPersistence().plugin]
})
