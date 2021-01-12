<template>
  <footer class="centered_row">
    <div class="column">
      <div class="small_row" style="padding-top: 30px">
        <a href="https://github.com/CAMCOH1989">Github</a>
        <a href="https://t.me/joinchat/@CAMCOH1989">Telegram</a>
        <a href="mailto:camcoh1989@gmail.com">Email</a>
        <a href="tel:+79032997420">+7 (903) 299-74-20</a>
        <a href="#">Skype</a>
      </div>
      <div class="small_row">
        <a href="#">LinkedIn</a>
        <a href="#">HH.ru</a>
        <a href="#">VK</a>
        <a href="#">Facebook</a>
      </div>
    </div>
  </footer>
</template>

<script>

export default {
  name: "Footer",
  // icons: {
  //   iconfont: 'mdiSvg'
  // }
}
</script>

<style scoped>
footer {
  bottom: 0;
  background: #2f2f2f;
  position: fixed;
  width: 100%;
  height: 90px;
}

a {
  color: white;
  margin-bottom: 10px;
}

.centered_row {
  display: flex;
  justify-content: space-around;
}

.small_row {
  display: flex;
  justify-content: space-around;
}

.column {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 1000px;
}

.ico {
  width: 20px;
  height: 20px;
  margin-right: 5px;
}
 a {
   display: flex;
   align-items: center;
   text-decoration: none;
 }
</style>