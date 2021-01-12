<template>
  <div class="main_section">
    <header>
      <div v-if="$store.state.pageLocale === 'en'" style="display: flex">
        <a href="#Main" v-on:click="ShowPage('main')" class="header_button">Main page</a>
        <a href="#Skills" v-on:click="ShowPage('skills')" class="header_button">Skills</a>
        <a href="#CV" v-on:click="ShowPage('cv')" class="header_button">CV</a>
        <a href="#Statistics" v-on:click="ShowPage('stats')" class="header_button">Statistics</a>
      </div>
      <div v-else style="display: flex">
        <a href="#Main" v-on:click="ShowPage('main')" class="header_button">Главная</a>
        <a href="#Skills" v-on:click="ShowPage('skills')" class="header_button">навыки</a>
        <a href="#CV" v-on:click="ShowPage('cv')" class="header_button">Резюме</a>
        <a href="#Statistics" v-on:click="ShowPage('stats')" class="header_button">Статистика</a>
      </div>
      <fieldset class="lang_selector">
        <input v-on:change="SetLocale('ru')" :checked="$store.state.pageLocale === 'ru' || $store.state.pageLocale == undefined"
               type="radio" name="lang" id="ru">
        <label for="ru">RU</label>
        <input v-on:change="SetLocale('en')" :checked="$store.state.pageLocale === 'en'"
               type="radio" name="lang" id="en">
        <label for="en">EN</label>
      </fieldset>
    </header>
    <div v-if="this.pageToShow === 'main'" class="section_div">
      <Main/>
    </div>
    <div v-else-if="this.pageToShow === 'skills'" class="section_div">
      <SkillTags/>
    </div>
    <div v-else-if="this.pageToShow === 'cv'" class="section_div">
      <CV/>
    </div>
    <div v-else-if="this.pageToShow === 'stats'" class="section_div">
      <Statistics/>
    </div>
    <Footer/>
  </div>
</template>

<script>
import Vue from "vue";
import VueCookies from "vue-cookies";
import Vuex from 'vuex';
import Main from '@/components/Main.vue';
import Footer from '@/components/Footer.vue';
import SkillTags from '@/components/SkillTags.vue';
import CV from '@/components/CV.vue';
import Statistics from '@/components/Statistics.vue';
import axios from "axios";

Vue.use(VueCookies);
Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    pageLocale: "ru",
    cv: {
      surName: undefined,
      firstName: undefined,
      middleName: undefined,
      birthDate: undefined,
      age: undefined,
      phone: undefined,
      experience: undefined,
      email: undefined,
      telegram: undefined,
      skype: undefined,
      personalData: undefined,
      education: undefined,
      languages: undefined,
      sex: undefined,
    },
    statistics_raw: undefined,
    statistics: {
      locations: undefined,
      systems: undefined
    }
  },
  actions: {
    fillCVData() {
      axios({
        method: "get",
        url: "/api/cv",
        params: {"locale": this.state.pageLocale},
      }).then(response => {
        if (response.status === 200) {
          console.log(response.data)
          this.state.cv = response.data.cv;
        } else {
          console.log(response);
        }
      }).catch(error => {
        console.log(error);
      })
    },
    getStatistics() {
      axios({
        method: "get",
        url: "/api/statistics",
        params: {"locale": this.state.pageLocale},
      }).then(response => {
        if (response.status === 200) {
          console.log(response.data)
          this.state.statistics = response.data.statistics;
        } else {
          console.log(response);
        }
      }).catch(error => {
        console.log(error);
      })
    }
  }
})

export default {
  name: 'App',
  store: store,
  data() {
    return {
      pageToShow: "main",
    }
  },
  components: {
    Main,
    Footer,
    SkillTags,
    CV,
    Statistics,
  },
  methods: {
    ShowPage(new_page) {
      this.pageToShow = new_page
      const location = {"location": new_page}
      axios({
        method: "post",
        url: "/api/statistics",
        data: location
      }).then(response => {
        if (response.status !== 200) {
          console.log(response);
        }
      }).catch(error => {
        console.log(error);
      })
    },
    SetLocale(new_locale) {
      this.$store.state.pageLocale = new_locale;
      localStorage.setItem("locale", new_locale);
      this.$store.dispatch("fillCVData");
    }
  },
  mounted() {
    if (window.location.hash === "#CV") {
      this.pageToShow = "cv";
    } else if (window.location.hash === "#Main") {
      this.pageToShow = "main";
    } else if (window.location.hash === "#Statistics") {
      this.pageToShow = "stats";
    } else if (window.location.hash === "#Skills") {
      this.pageToShow = "skills";
    } else {
      this.pageToShow = "main";
    }
    this.$store.state.pageLocale = localStorage.getItem("locale")
  }
}
</script>

<style>
html {
  margin: 0;
  padding: 0;
}

body {
  margin: 0;
  padding: 0;
  height: 100vh;
}

header {
  position: fixed;
  width: 100%;
  height: 50px;
  background: #2f2f2f;
  padding: 10px 10px;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  top: 0;
  z-index: 100;
}

.header_button {
  min-width: 20px;
  height: 20px;
  max-width: 100px;
  padding: 15px 10px;
  margin: 0 10px;
  background: #201f1f;
  color: aliceblue;
}

.main_section {
  padding: 70px 0 90px;
  background: #965509;
  color: #201f1f;
  min-height: 80%;
}

h3 {
  height: 100px;
}

.section_div {
  /*height: 100%;*/
}

.lang_selector {
  margin-right: 40px;
}

.centered {
  display: flex;
  justify-content: center;

}
</style>
