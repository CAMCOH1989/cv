<template>
  <div class="centered">
    <vue-word-cloud
        style="
          height: 480px;
          width: 640px;
        "
        :words="this.skills"
        :color="([, weight]) =>
        weight > 90 ? 'DeepPink' :
        weight > 80 ? 'Red' :
        weight > 70 ? 'Grey' :
        weight > 60 ? 'Yellow' :
        weight > 50 ? 'White' :
        weight > 40 ? 'Aqua' :
        weight > 30 ? 'DeepPink' :
        weight > 20 ? 'DeepPink' :
        weight > 10 ? 'RoyalBlue' : 'Indigo'"
        font-family="Roboto"
    />
  </div>
</template>

<script>
import axios from "axios";
import VueWordCloud from 'vuewordcloud';


export default {
  name: "SkillsTags",
  data() {
    return {
      skills: undefined,
    }
  },
  methods: {
    getSkills: function () {
      axios({
        method: "get",
        url: "/api/skills",
        params: {},
      }).then(response => {
        if (response.status === 200) {
          console.log(response.data.skills);
          this.skills = response.data.skills;
        } else {
          console.log(response);
        }
      }).catch(error => {
        console.log(error);
      })
    }
  },
  components: {
    [VueWordCloud.name]: VueWordCloud,
  },
  mounted() {
    this.getSkills();
    console.log(this.skills);
  }
}
</script>

<style>
body {
  color: ;
}
</style>