import Vue from 'vue'

import Cookies from 'js-cookie'

import 'normalize.css/normalize.css' // A modern alternative to CSS resets

import '@/vendor/GoogleAnalytics'
import '@/vendor/VxeTable'
import Element from 'element-ui'
import './styles/element-variables.scss'

import '@/styles/index.scss' // global css

import enLang from 'element-ui/lib/locale/lang/en'

import App from './App'
import store from './store'
import router from './router'

import './icons' // icon
import './permission' // permission control

import * as filters from './filters' // global filters

import { mockXHR } from '../mock' // simulation data

// mock api in github pages site build
if (process.env.NODE_ENV === 'production') { mockXHR() }

Vue.use(Element, {
  size: Cookies.get('size') || 'medium', // set element-ui default size
  locale: enLang
})

// register global utility filters.
Object.keys(filters).forEach(key => {
  Vue.filter(key, filters[key])
})

Vue.config.productionTip = false

new Vue({
  el: '#app',
  router,
  store,
  // beforeCreate() {
  //   this.$store.dispatch('favourites/initFavs')
  // },
  render: h => h(App)
})
