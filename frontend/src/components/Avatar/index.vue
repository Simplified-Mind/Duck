<template>
  <div @click="redirect">
    <img :src="photo" class="user-avatar">
  </div>
</template>

<script>
export default {
  name: 'Avatar',
  data() {
    return {
      photo: 'data:image/png;base64,' + this.$store.state.user.photo
    }
  },
  methods: {
    redirect() {
      this.$router.push(`/profile/index`)
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
