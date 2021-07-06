<template>
  <div :class="{'has-logo':showLogo}">
    <logo v-if="showLogo" :collapse="isCollapse" />
    <el-scrollbar wrap-class="scrollbar-wrapper">
      <div class="default-menu">
        <hamburger id="hamburger-container" :is-active="sidebar.opened" class="hamburger-container white" @toggleClick="toggleSideBar" />
        <avatar class="avatar-container" />
        <ErrorLog class="errlog-container" />
        <screenfull class="screenfull-container" />
        <logout class="logout-container" />
      </div>
      <el-menu
        :default-active="$route.path"
        :collapse="isCollapse"
        :background-color="variables.menuBg"
        :text-color="variables.menuText"
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
import Logout from '@/components/Logout'
import SidebarItem from './SidebarItem'
import variables from '@/styles/variables.scss'

export default {
  components: { SidebarItem, Logo, Hamburger, Avatar, ErrorLog, Screenfull, Logout },
  methods: {
    toggleSideBar() {
      this.$store.dispatch('app/toggleSideBar')
    }
  },
  computed: {
    ...mapGetters([
      'permission_routes',
      'sidebar'
    ]),
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

<style lang="scss" scoped>
.default-menu {
  .errlog-container {
    display: inline-block;
    vertical-align: top;
  }
}
</style>
