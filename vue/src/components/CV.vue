<template>
<div class="scroll">
  <div class="centered" style="flex-direction: column">
    <h1>{{ $store.state.cv.surName }} {{ $store.state.cv.firstName }} {{
        $store.state.cv.middleName
      }}</h1>
    <p>{{ $store.state.cv.sex }} {{ $store.state.cv.age }} ({{ $store.state.cv.birthDate }})
    </p>
  </div>
  <div class="centered" style="margin-top: 50px">
    <div class="cv_column">
      <img width="300" height="600" style="left: 300px" src="/images/test.jpg">
    </div>
    <div class="cv_column">
      <h2 v-if="this.$store.state.pageLocale === 'ru'">Контакты</h2>
      <h2 v-else-if="this.$store.state.pageLocale === 'en'">Contacts</h2>
      <table>
        <tbody>
        <tr>
          <td>Phone:</td>
          <td>{{ $store.state.cv.phone }}</td>
        </tr>
        <tr>
          <td>Email:</td>
          <td>{{ $store.state.cv.email }}</td>
        </tr>
        <tr>
          <td>Telegram:</td>
          <td>{{ $store.state.cv.telegram }}</td>
        </tr>
        <tr>
          <td>Skype:</td>
          <td>{{ $store.state.cv.skype }}</td>
        </tr>
        </tbody>
      </table>
      <h2 v-if="this.$store.state.pageLocale === 'ru'">Опыт</h2>
      <h2 v-else-if="this.$store.state.pageLocale === 'en'">Experience</h2>
      <div v-for="exp in this.$store.state.cv.experience">
        <p>{{ exp }}</p>
      </div>
      <h2 v-if="this.$store.state.pageLocale === 'ru'">Знание языков</h2>
      <h2 v-else-if="this.$store.state.pageLocale === 'en'">Languages</h2>
      <table>
        <tbody>
        <tr v-for="lang in this.$store.state.cv.languages">
          <td>{{ lang.language }}</td>
          <td>{{ lang.experience }}</td>
        </tr>
        </tbody>
      </table>
      <h2 v-if="this.$store.state.pageLocale === 'ru'">Образование</h2>
      <h2 v-else-if="this.$store.state.pageLocale === 'en'">Education</h2>
      <div>
        <p>{{ $store.state.cv.education }}</p>
      </div>
      <h2 v-if="this.$store.state.pageLocale === 'ru'">О себе</h2>
      <h2 v-else-if="this.$store.state.pageLocale === 'en'">About me</h2>
      <div>
        <p>{{ $store.state.cv.personalData }}</p>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: "CV",
  data() {
    return {
      
    }
  },
  methods: {
  },
  mounted: function () {
    this.$store.dispatch("fillCVData");
    // this.fillCVData();
  },
  watch: {
    $store: function (){
      alert(this.$store.state.pageLocale);
    }
  }
}
</script>

<style scoped>
.cv_column {
  width: 350px;
  text-align: center;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
}

.cv_column p, table {
  text-align: left;
}
</style>