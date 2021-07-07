<template>
  <div class="profile-container">
    <el-form :inline="true">
      <el-row>
        <el-form-item label="Name:">
          <el-input v-model.trim="user.username" />
        </el-form-item>
      </el-row>
      <el-row>
        <el-form-item label="Email:">
          <el-input v-model.trim="user.email" />
        </el-form-item>
      </el-row>
      <el-row>
        <el-form-item>
          <el-button type="primary" @click="submit">Update</el-button>
        </el-form-item>
      </el-row>
    </el-form>
  </div>
</template>

<script>
export default {
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          name: '',
          email: ''
        }
      }
    }
  },
  methods: {
    submit() {
      this.$message({
        message: 'User information has been updated successfully',
        type: 'success',
        duration: 10 * 1000,
        showClose: true
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.profile-container {
  margin-top: 20px;
}
</style>
