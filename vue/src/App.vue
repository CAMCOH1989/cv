<template>
  <div class="main_section">
    <header>
      <div style="display: flex">
        <a href="#Main" v-on:click="ShowMain()" class="header_button">Main page</a>
        <a href="#Skills" v-on:click="ShowSkills()" class="header_button">Skills</a>
        <a href="#CV" v-on:click="ShowCV()" class="header_button">CV</a>
      </div>
      <fieldset class="lang_selector">
        <input v-on:change="SetLocale('ru')" :checked="$store.state.pageLocale === 'ru'"
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
import CV from '@/components/CV.vue'
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
  },
  methods: {
    ShowMain() {
      this.pageToShow = "main"
    },
    ShowSkills() {
      this.pageToShow = "skills"
    },
    ShowCV() {
      this.pageToShow = "cv"
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
  height: 100vh;
}

h3 {
  height: 100px;
}

.section_div {
  height: 100%;
}

.lang_selector {
  margin-right: 40px;
}
</style>
