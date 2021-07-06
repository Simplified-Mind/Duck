<template>
  <div @click="redirect">
    <el-badge :value="errorLogs.length" type="warning" :hidden="errorLogs.length === 0">
      <svg-icon icon-class="bug" />
    </el-badge>
  </div>
</template>

<script>
export default {
  name: 'ErrorLog',
  computed: {
    errorLogs() {
      return this.$store.getters.errorLogs
    }
  },
  methods: {
    redirect() {
      this.$router.push(`/error/log`)
    }
  }
}
</script>

<style lang="scss" scoped>
.errlog-container {
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
