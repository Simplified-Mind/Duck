<template>
  <el-card>
    <div slot="header" class="clearfix">
      <span>About me</span>
    </div>

    <div class="profile-container">
      <center>
        <div class="user-profile">
          <pan-thumb :image="`data:image/png;base64,${user.photo}`" :height="'100px'" :width="'100px'" />
          <div class="user-name">{{ user.username }}</div>
          <div class="user-role text-muted">{{ user.group | uppercaseFirst }}</div>
        </div>
      </center>

      <div class="user-bio">
        <div class="user-education user-bio-section">
          <div class="user-bio-section-header">Title</div>
          <div class="user-bio-section-body">
            <div class="text-muted">
              Front Office Models Developer, Power Trading Team 2 (PT)
            </div>
          </div>
        </div>

        <div class="user-skills user-bio-section">
          <div class="user-bio-section-header">Projects</div>
          <div class="user-bio-section-body">
            <div class="progress-item">
              <span>UI</span>
              <el-progress :percentage="65" />
            </div>
            <div class="progress-item">
              <span>Backend</span>
              <el-progress :percentage="18" />
            </div>
            <div class="progress-item">
              <span>DevOps</span>
              <el-progress :percentage="32" />
            </div>
            <div class="progress-item">
              <span>Testing</span>
              <el-progress :percentage="48" />
            </div>
            <div class="progress-item">
              <span>Induction</span>
              <el-progress :percentage="100" status="success" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </el-card>
</template>

<script>
import PanThumb from '@/components/PanThumb'

export default {
  components: { PanThumb },
  props: {
    user: {
      type: Object,
      default: () => {
        return {
          username: '',
          role: '',
          group: '',
          email: '',
          photo: ''
        }
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.text-muted {
  color: #777;
}

.user-profile {
  .user-name {
    font-weight: bold;
    margin-top: 10px;
  }

  .box-center {
    padding-top: 10px;
  }

  .user-role {
    padding-top: 10px;
    font-weight: 400;
    font-size: 14px;
  }

  .box-social {
    padding-top: 30px;

    .el-table {
      border-top: 1px solid #dfe6ec;
    }
  }

  .user-follow {
    padding-top: 20px;
  }
}

.user-bio {
  margin-top: 20px;
  color: #606266;

  span {
    padding-left: 4px;
  }

  .user-bio-section {
    font-size: 14px;
    padding: 15px 0;

    .user-bio-section-header {
      border-bottom: 1px solid #dfe6ec;
      padding-bottom: 10px;
      margin-bottom: 10px;
      font-weight: bold;
    }
  }
}
</style>
