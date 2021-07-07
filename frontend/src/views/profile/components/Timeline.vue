<template>
  <div class="profile-container">
    <el-timeline>
      <el-timeline-item v-for="(item,index) of timeline" :key="index" :timestamp="item.timestamp" placement="top">
        <el-card>
          <h4>{{ item.title }}</h4>
          <p>{{ item.content }}</p>
        </el-card>
      </el-timeline-item>
    </el-timeline>
  </div>
</template>

<script>
export default {
  data() {
    return {
      timeline: [
        {
          timestamp: '18/01/2021',
          title: 'Kick off UI Project',
          content: 'hdam committed 18/01/2020 09:46'
        },
        {
          timestamp: '19/01/2021',
          title: 'UI branch created',
          content: 'hdam committed 19/01/2021 10:03'
        },
        {
          timestamp: '19/01/2021',
          title: 'Rebuild Template',
          content: 'hdam committed 19/01/2021 12:31'
        },
        {
          timestamp: '26/01/2021',
          title: 'Release Demo version',
          content: 'hdam committed 26/01/2021 20:15'
        }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.profile-container {
  margin-top: 20px;
}
.el-timeline {
  padding-left: 10px;
}
.el-card {
    border: 1px solid #bbb;
    background-color: #efefef;
    -webkit-box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.1);
    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}
h4 {
  margin-top: 0;
  margin-bottom: 10px;
}
p {
  margin: 0
}

</style>
