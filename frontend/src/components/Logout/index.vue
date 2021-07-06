<template>
  <div @click="confirm">
    <svg-icon icon-class="logout" />
  </div>
</template>

<script>
export default {
  name: 'Logout',
  data() {
    return {
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    confirm() {
      this.$confirm('Are you sure you want to leave this session?', 'Logout', {
        confimrButtonText: 'Ok',
        cancelButtonText: 'Cancel',
        type: 'warning'
      }).then(() => {
        this.logout()
      }).catch(() => {})
    }
  }
}
</script>

<style lang="scss" scoped>
.logout-container {
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
    width: 20px;
    height: 20px;
    fill: #fff;
    margin-right: 0 !important;
    margin-left: 2px;
  }
}
</style>
