import Vue from 'vue'
import 'xe-utils'
import VXETable from 'vxe-table'
import VueI18n from 'vue-i18n'
import enUS from 'vxe-table/lib/locale/lang/en-US'

const messages = {
  en_US: {
    ...enUS
  }
}

Vue.use(VueI18n)

const i18n = new VueI18n({
  locale: 'en_US',
  messages
})

Vue.use(VXETable, {
  i18n: (key, args) => i18n.t(key, args)
})
