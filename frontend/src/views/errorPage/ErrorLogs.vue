<template>
  <div class="app-container errorlogs">
    <vxe-table
      round
      border
      auto-resize
      size="mini"
      header-align="center"
      :max-height="500"
      :data="errorLogs"
      :sort-config="{trigger: 'cell', orders:['desc','asc',null]}"
    >
      <vxe-table-column type="seq" width="40" align="center" />
      <vxe-table-column field="time" title="Time" :formatter="formatDateTime" :width="130" sortable />
      <vxe-table-column field="url" title="Page" :formatter="formatURL" :width="80" />
      <vxe-table-column field="info" title="Component" :width="100" />
      <vxe-table-column field="vm" title="Error" :width="150" />
      <vxe-table-column field="err" title="Traceback" />
    </vxe-table>
    <br>
    <div v-show="errorLogs.length" class="inlineFlex">
      <el-button size="mini" type="secondary" icon="el-icon-delete" @click="clearAll">Clear All</el-button>
      <!--<el-button type="primary" size="mini" icon="el-icon-message" @click="handleReport()">Report Issues</el-button>-->
    </div>
  </div>
</template>

<script>
import moment from 'moment'

export default {
  name: 'ErrorLogs',
  data() {
    return {}
  },
  computed: {
    errorLogs() {
      return this.$store.getters.errorLogs
    }
  },
  methods: {
    clearAll() {
      this.$store.dispatch('errorLog/clearErrorLog')
    },
    formatDateTime({ cellValue }) {
      if (cellValue === '' || cellValue === null) {
        return '-'
      }
      return moment(cellValue).format('YYYY-MM-DD - HH:mm:ss')
    },
    formatURL({ cellValue }) {
      return cellValue.split('#/')[1].replace('/', ' / ')
    },
    handleReport() {
      const recipients = [
        'hao.dam@gazprom-mt.com',
        'hong.ji@gazprom-mt.com'
      ]
      const subject = 'Error Report'
      let body = '<table><tr><th>Time</th><th>Page</th><th>Component</th><th>Error</th><th>Traceback</th></tr>'
      this.$store.getters.errorLogs.forEach(element => {
        body += '<tr>'
        body += '<td>' + element.time + '</td>'
        body += '<td>' + element.url + '</td>'
        body += '<td>' + element.info + '</td>'
        body += '<td>' + element.vm + '</td>'
        body += '<td>' + element.err + '</td>'
        body += '</tr>'
      })
      body += '</table>'
      body = body.replace(/["']/g, '')
      console.log('report', 'mailto:' + recipients.join(',') + '?subject=' + subject + '&body=' + body)
      // window.open("mailto:" + recipients.join(',') + "?subject=" + subject + "&body=" + body);
    }
  }
}
</script>

<style lang="scss">
.errorlogs {
  .vxe-body--column {
    vertical-align: top;
  }
  .vxe-table .vxe-cell {
    word-break: break-word;
  }
}
</style>
