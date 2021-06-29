<template>
  <el-dropdown class="avatar-container" trigger="click">
    <div class="avatar-wrapper">
      <img :src="userPhoto" class="user-avatar">
    </div>
    <el-dropdown-menu slot="dropdown">
      <router-link to="/">
        <el-dropdown-item>
          {{ $t('sidebar.dashboard') }}
        </el-dropdown-item>
      </router-link>
      <router-link to="/user-profile">
        <el-dropdown-item>
          {{ $t('sidebar.userProfile') }}
        </el-dropdown-item>
      </router-link>
      <el-dropdown-item divided>
        <span style="display:block;" @click="confirmLogout">{{ $t('sidebar.logOut') }}</span>
      </el-dropdown-item>
    </el-dropdown-menu>
  </el-dropdown>
</template>

<script>
export default {
  name: 'Avatar',
  data() {
    return {
      userPhoto: `data:image/png;base64,${this.$store.state.user.photo}`
    }
  },
  methods: {
    async logout() {
      await this.$store.dispatch('user/logout')
      this.$router.push(`/login?redirect=${this.$route.fullPath}`)
    },
    confirmLogout() {
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
.avatar-container {
  padding: 8px;
  display: inline-block;
  cursor: pointer;
  width: 36px;
  height: 36px;
  transition: 0.2s;

  &:hover {
    background-color: #001528;
  }

  .user-avatar {
    vertical-align: middle;
    width: 20px;
    height: 20px;
    border-radius: 10px;
  }
}
</style>
