<template>
  <div class="login-container">
    <el-form ref="loginForm" :model="loginForm" :rules="loginRules" class="login-form" auto-complete="on" label-position="left">

      <div class="title-container">
        <img
          class="logo"
          src="../../../public/login-logo.svg"
        >
      </div>

      <el-form-item prop="username">
        <span class="svg-container">
          <svg-icon icon-class="user" />
        </span>
        <el-input
          ref="username"
          v-model="loginForm.username"
          class="inputTransparent"
          placeholder="username"
          name="username"
          type="text"
          auto-complete="on"
        />
      </el-form-item>
      <el-tooltip v-model="capsTooltip" content="Caps lock is On" placement="right" manual>
        <el-form-item prop="password">
          <span class="svg-container">
            <svg-icon icon-class="password" />
          </span>
          <el-input
            :key="passwordType"
            ref="password"
            v-model="loginForm.password"
            :type="passwordType"
            placeholder="password"
            name="password"
            auto-complete="on"
            @keyup.native="checkCapslock"
            @blur="capsTooltip === false"
            @keyup.enter.native="handleLogin"
          />
          <span class="show-pwd" @click="showPwd">
            <svg-icon :icon-class="passwordType === 'password' ? 'eye' : 'eye-open'" />
          </span>
        </el-form-item>
      </el-tooltip>
      <el-button :loading="loading" type="primary" style="width:100%;margin-bottom:30px;" @click.native.prevent="handleLogin">Login</el-button>
    </el-form>
  </div>
</template>

<script>

export default {
  name: 'Login',
  data() {
    return {
      loginForm: {
        username: 'admin',
        password: '111111'
      },
      loginRules: {
        username: [{ required: true, trigger: 'blur' }],
        password: [{ required: true, trigger: 'blur' }]
      },
      passwordType: 'password',
      capsTooltip: false,
      loading: false,
      showDialog: false,
      redirect: undefined,
      otherQuery: {}
    }
  },
  watch: {
    $route: {
      handler: function(route) {
        this.redirect = route.query && route.query.redirect
      },
      immediate: true
    }
  },
  created() {
    // window.addEventListener('storage', this.afterQRScan)
  },
  mounted() {
    if (this.loginForm.username === '') {
      this.$refs.username.focus()
    } else if (this.loginForm.password === '') {
      this.$refs.password.focus()
    }
  },
  destroyed() {
    // window.removeEventListener('storage', this.afterQRScan)
  },
  methods: {
    checkCapslock(e) {
      const { key } = e
      this.capsTooltip = key && key.length === 1 && (key >= 'A' && key <= 'Z')
    },
    showPwd() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
      } else {
        this.passwordType = 'password'
      }
      this.$nextTick(() => {
        this.$refs.password.focus()
      })
    },
    handleLogin() {
      this.$refs.loginForm.validate(valid => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/login', this.loginForm)
            .then(() => {
              this.$router.push({ path: this.redirect || '/' })
              this.loading = false
            })
            .catch(() => {
              this.loading = false
            })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    getOtherQuery(query) {
      return Object.keys(query).reduce((acc, cur) => {
        if (cur !== 'redirect') {
          acc[cur] = query[cur]
        }
        return acc
      }, {})
    }
  }
}
</script>

<style lang="scss">
$bg:#2d3a4b;
$dark_gray:#2d3a4b;
$light_gray:#eee;
$primary: #0065BD;
$input_bg: #f0f2f5;

@keyframes pulse {
  from {
    background-color: rgba(0, 0, 0, 0.3);
  }
  to {
    background-color: rgba(0, 0, 0, 0);
  }
}

.login-container {
  min-height: 100%;
  width: 100%;
  overflow: hidden;
  background-image: url("../../../public/bg.jpeg");
  z-index: -9000 !important;
  background-size: cover !important;
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-position-y: 70%;
  background-blend-mode: soft-light;
  -webkit-animation: pulse 8s ease-in-out infinite alternate;
  animation: pulse 4s ease-in-out infinite alternate;

  .login-form {
    position: relative;
    width: 400px;
    max-width: 100%;
    padding: 20px 40px 40px 40px;
    margin: 10% auto 0 auto;
    overflow: hidden;
    background: #fff;
    border-radius: 3px;
    -webkit-box-shadow: 1px 1px 2px rgba(0,0,0,0.5);
    box-shadow: 1px 1px 2px rgba(0,0,0,0.5);
  }

  .svg-container {
    padding: 6px 5px 6px 15px;
    color: $bg;
    vertical-align: middle;
    width: 30px;
    display: inline-block;
  }

  .title-container {
    position: relative;

    .logo{
      display: block;
      width: 30%;
      height: 30%;
      margin-left: auto;
      margin-right: auto;
    }
    .title {
      font-size: 20px;
      color: $bg;
      margin: 0px auto 20px auto;
      text-align: center;
      font-weight: 300;
    }
  }

  .login-logo {
    max-width: 80%;
    margin-bottom: 30px;
  }

  .show-pwd {
    position: absolute;
    right: 10px;
    top: 7px;
    font-size: 16px;
    color: $bg;
    cursor: pointer;
    user-select: none;

    &:hover {
      color: $primary;
    }
  }

  .thirdparty-button {
    position: absolute;
    right: 0;
    bottom: 6px;
  }

  @media only screen and (max-width: 470px) {
    .thirdparty-button {
      display: none;
    }
  }

  .el-button {
    font-size: 16px;
  }
}
</style>
