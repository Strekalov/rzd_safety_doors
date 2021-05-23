import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import ConfigPage from './components/ConfigPage'
import MainPage from './components/MainPage'
import vuetify from './plugins/vuetify'

Vue.use(VueRouter)
Vue.config.productionTip = false


const routes = [
  { path: '/settings', component: ConfigPage },
  { path: '/home', component: MainPage },
];

const router = new VueRouter({ routes });

new Vue({
  vuetify,
  router,
  render: h => h(App)
}).$mount('#app')
