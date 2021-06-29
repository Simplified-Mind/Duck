<template>
  <el-dropdown trigger="click" class="international" @command="handleSetLanguage">
    <div>
      <svg-icon class-name="international-icon" icon-class="language" />
    </div>
    <el-dropdown-menu slot="dropdown">
      <el-dropdown-item :disabled="language==='zh'" command="zh">
        中文
      </el-dropdown-item>
      <el-dropdown-item :disabled="language==='en'" command="en">
        English
      </el-dropdown-item>
      <el-dropdown-item :disabled="language==='es'" command="es">
        Español
      </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</template>

<script>
export default {
  computed: {
    language() {
      return this.$store.getters.language
    }
  },
  methods: {
    handleSetLanguage(lang) {
      this.$i18n.locale = lang
      this.$store.dispatch('app/setLanguage', lang)
      this.$message({
        message: 'Switch Language Success',
        type: 'success'
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.langSelect-container {
  padding: 8px;
  display: inline-block;
  cursor: pointer;
  width: 36px;
  height: 36px;
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
    margin-left: 2px;
  }
}
</style>
