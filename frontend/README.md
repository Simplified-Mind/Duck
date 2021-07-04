## Configuration

### Settings
#### Mutable/Reactive 
* frontend/src/settings.js
  * Configurations vary depending on the state
#### Immutable/Environment
Same configurations will be applied to all states. 
* frontend/.env.development
* frontend/.env.production
* frontend/.env.staging

### Static
* login background image
    * bg.jpeg
      * frontend/src/views/login/index.vue
* favorite icon
    * favicon.ico
      * frontend/public/index.html
* logo
  * logo.svg
    * frontend/src/views/login/index.vue
    * frontend/src/layout/components/Sidebar/Logo.vue

### Icon
1. Download [icon](https://www.iconfont.cn/) as svg
2. Place svg to frontend/src/icons
```html
<svg-icon icon-class="logout" />
```

### Internationalization
1. [vue-injected-methods](https://kazupon.github.io/vue-i18n/api/#vue-injected-methods)
2. Key-value pairs are stored in the frontend/src/lang