<template>
  <div class="profile-container">
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'https://i.pinimg.com/originals/de/64/80/de64801f0275c1ab2ea5a9e2bb3ce7bc.jpg'+avatarPrefix">
        <span class="username text-muted">Deborah</span>
        <span class="description">Shared publicly - 7:30 PM today</span>
      </div>
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
      </p>
      <div class="user-images">
        <el-carousel :interval="5000" type="card" height="220px">
          <el-carousel-item v-for="item in carouselImages" :key="item">
            <img :src="item+carouselPrefix" class="image">
          </el-carousel-item>
        </el-carousel>
      </div>
    </div>
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNGG5QdMCpHqj1z42B12HfcCa1hwUCjiw9ag&usqp=CAU'+avatarPrefix">
        <span class="username">Touka</span>
        <span class="description">Sent you a message - yesterday</span>
      </div>
      <p>
        Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
      </p>
    </div>
    <div class="post">
      <div class="user-block">
        <img class="img-circle" :src="'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQscEoyxLz4-tFEvEh2jtNyXiOIMkKPCD-GNA&usqp=CAU'+avatarPrefix">
        <span class="username text-muted">Peter</span>
        <span class="description">Posted 4 photos - 2 days ago</span>
      </div>
      <p>
        Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
      </p>
    </div>
  </div>
</template>

<script>
const avatarPrefix = '?imageView2/1/w/80/h/80'
const carouselPrefix = '?imageView2/2/h/440'

export default {
  data() {
    return {
      carouselImages: [
        'https://russiabusinesstoday.com/wp-content/uploads/2018/06/gazprom.jpg',
        'https://i.ytimg.com/vi/ts32YV1o7Zo/mqdefault.jpg',
        'https://careers.gazprom-mt.com/wp-content/uploads/2018/01/gazprom-marketing-trading-btl-group-next-phase.jpg',
        'https://www.gazprom.com/f/posts/22/394541/pskov.jpg'
      ],
      avatarPrefix,
      carouselPrefix
    }
  }
}
</script>

<style lang="scss" scoped>
.profile-container {
  margin-top: 20px;

  .user-block {

    .username,
    .description {
      display: block;
      margin-left: 50px;
      padding: 2px 0;
    }

    .username{
      font-size: 16px;
      color: #000;
    }

    :after {
      clear: both;
    }

    .img-circle {
      border-radius: 50%;
      width: 40px;
      height: 40px;
      float: left;
    }

    span {
      font-weight: 500;
      font-size: 12px;
    }
  }

  .post {
    font-size: 14px;
    border-bottom: 1px solid #d2d6de;
    margin-bottom: 15px;
    padding-bottom: 15px;
    color: #666;

    .image {
      width: 100%;
      height: 100%;

    }

    .user-images {
      padding-top: 20px;
    }
  }

  .list-inline {
    padding-left: 0;
    margin-left: -5px;
    list-style: none;

    li {
      display: inline-block;
      padding-right: 5px;
      padding-left: 5px;
      font-size: 13px;
    }

    .link-black {

      &:hover,
      &:focus {
        color: #999;
      }
    }
  }

}

.box-center {
  margin: 0 auto;
  display: table;
}

.text-muted {
  color: #777;
}
</style>
