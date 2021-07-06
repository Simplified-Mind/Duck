<template>
  <section class="app-main">
    <transition name="fade-transform" mode="out-in" duration="0.2">
      <keep-alive :include="cachedViews">
        <router-view :key="key" />
      </keep-alive>
    </transition>
    <BackToTop :visibility-height="0" :back-position="0" transition-name="fade" />
    <footer class="footer">
      <p>Copyright © {{ new Date().getFullYear() }} <strong>{{ copyright }}</strong>. All rights reserved.</p>
    </footer>
  </section>
</template>

<script>
import BackToTop from '@/components/BackToTop'

export default {
  name: 'AppMain',
  components: { BackToTop },
  data() {
    return {
      copyright: process.env.VUE_APP_COPYRIGHT
    }
  },
  computed: {
    cachedViews() {
      return this.$store.state.tagsView.cachedViews
    },
    key() {
      return this.$route.fullPath
    }
  }
}
</script>

<style lang="scss" scoped>
.app-main {
  /* 50= navbar  50  */
  min-height: calc(100vh - 50px);
  width: 100%;
  position: relative;
  overflow: hidden;
  background-color: #eef1f6;
  display: flex;
  flex-direction: column;
  height: 100%;
}

.fixed-header+.app-main {
  padding-top: 50px;
}

.hasTagsView {
  .app-main {
    min-height: calc(100vh);
  }
}

.footer {
  flex-shrink: 0;
  text-align: center;
  background-color: #ddd;

  p {
    margin: 17px;
    font-size: 14px;
  }
}

</style>

<style lang="scss">
// fix css style bug in open el-dialog
.el-popup-parent--hidden {
  .fixed-header {
    padding-right: 15px;
  }
}
</style>
