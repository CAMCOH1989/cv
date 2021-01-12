<template>
  <footer class="centered_row">
    <div v-if="$store.state.pageLocale === 'en'" class="small_row">
      <a>Github</a>
      <a>Telegram</a>
      <a>Email</a>
      <a>Phone</a>
      <a>Skype</a>
    </div>
    <div v-else class="column">
      <a>Github</a>
      <a>Telegram</a>
      <a>Email</a>
      <a>Телефон</a>
      <a>Skype</a>
    </div>
  </footer>
</template>

<script>
export default {
  name: "Footer"
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
  padding-top: 30px;
  width: 100%;
  max-width: 1000px;
}
</style>