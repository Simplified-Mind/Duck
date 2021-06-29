<template>
  <div :class="{'has-logo':showLogo}">
    <logo v-if="showLogo" :collapse="isCollapse" />
    <el-scrollbar wrap-class="scrollbar-wrapper">
      <div class="defaultMenu">
        <hamburger :is-active="sidebar.opened" class="hamburger-container" @toggleClick="toggleSideBar" />
        <avatar class="avatar-container" />
        <error-log class="errorLog-container" />
        <screenfull class="screenFull-container" />
        <el-tooltip v-if="internationalization" :content="$t('sidebar.size')" effect="dark" placement="bottom">
          <size-select class="sizeSelect-container" />
        </el-tooltip>
        <size-select v-if="internationalization === false" class="sizeSelect-container" />
        <lang-select v-if="internationalization" class="langSelect-container" />
      </div>
      <el-menu
        :default-active="activeMenu"
        :collapse="isCollapse"
        :background-color="variables.menuBg"
        :text-color="variables.menuText"
        :unique-opened="false"
        :active-text-color="variables.menuActiveText"
        :collapse-transition="false"
        mode="vertical"
      >
        <sidebar-item v-for="route in permission_routes" :key="route.path" :item="route" :base-path="route.path" />
      </el-menu>
    </el-scrollbar>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
import Logo from './Logo'
import Hamburger from '@/components/Hamburger'
import Avatar from '@/components/Avatar'
import ErrorLog from '@/components/ErrorLog'
import Screenfull from '@/components/Screenfull'
import SizeSelect from '@/components/SizeSelect'
import LangSelect from '@/components/LangSelect'
import SidebarItem from './SidebarItem'
import variables from '@/styles/variables.scss'

export default {
  components: {
    SidebarItem,
    Logo,
    Hamburger,
    Avatar,
    ErrorLog,
    Screenfull,
    SizeSelect,
    LangSelect
  },
  data() {
    return {
      internationalization: process.env.VUE_APP_INTERNATIONALIZATION === 'true'
    }
  },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    },
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    }
  },
  computed: {
    ...mapGetters([
      'permission_routes',
      'sidebar',
      'name',
      'avatar',
      'device'
    ]),
    activeMenu() {
      const route = this.$route
      const { meta, path } = route
      if (meta.activeMenu) {
        return meta.activeMenu
      }
      return path
    },
    showLogo() {
      return this.$store.state.settings.sidebarLogo
    },
    variables() {
      return variables
    },
    isCollapse() {
      return !this.sidebar.opened
    }
  }
}
</script>
