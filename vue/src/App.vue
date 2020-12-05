<template>
  <div id="app">
    <Main/>
    <ProfessionalSkills/>
  </div>
</template>

<script>
import Main from './components/Main.vue';
import ProfessionalSkills from './components/ProfessionalSkills.vue';

export default {
  name: 'app',
  state: {

  },
  components: {
    ProfessionalSkills,
    Main
  }
}

const router = new VueRouter({
  mode: 'history',
  routes: [
    {
      path: '/main',
      name: 'Main',
      component: Home,
      meta: {
        title: 'Main page',
        requiresAuthorization: true,
      },
    },
    {
      path: '/professional-skills',
      name: 'Authorized',
      component: ProfessionalSkills,
      meta: {
        title: 'Authorized',
        requiresAuthorization: false,
      },
    },
  ],
});

</script>

<style>
#app {
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
