<template>
  <div @click="click">
    <svg-icon :icon-class="isFullscreen?'exit-fullscreen':'fullscreen'" />
  </div>
</template>

<script>
import screenfull from 'screenfull'

export default {
  name: 'Screenfull',
  data() {
    return {
      isFullscreen: false
    }
  },
  mounted() {
    this.init()
  },
  beforeDestroy() {
    this.destroy()
  },
  methods: {
    click() {
      if (!screenfull.enabled) {
        this.$message({
          message: 'you browser can not work',
          type: 'warning'
        })
        return false
      }
      screenfull.toggle()
    },
    change() {
      this.isFullscreen = screenfull.isFullscreen
    },
    init() {
      if (screenfull.enabled) {
        screenfull.on('change', this.change)
      }
    },
    destroy() {
      if (screenfull.enabled) {
        screenfull.off('change', this.change)
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.screenfull-container {
  padding: 10px;
  display: inline-block;
  width: 36px;
  height: 36px;
  cursor: pointer;
  transition: 0.2s;

  &:hover {
    background-color: #001528;
  }

  .svg-icon {
    vertical-align: middle;
    width: 16px;
    height: 16px;
    fill: #fff;
    margin-right: 0 !important;
  }

}
</style>
