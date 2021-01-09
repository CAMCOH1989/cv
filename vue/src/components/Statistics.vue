<template>
  <div>
    <div v-for="page in  $store.state.statistics.pages">
      <p>{{page}}</p>
    </div>
    <div v-for="page in  $store.state.statistics.systems">
      <p>{{page}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Statistics",
  methods: {},
  mounted: function () {
    this.$store.dispatch("getStatistics");
  }
}
</script>

<style scoped>

</style>