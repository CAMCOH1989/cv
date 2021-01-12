<template>
  <div class="centered">
    <div v-for="page in  $store.state.statistics.locations">
      <p>{{page}}</p>
    </div>
    <div v-for="system in  $store.state.statistics.systems">
      <p>{{system}}</p>
    </div>

    <div id="chart_div" style="width: 100%; height: 400px;"></div>

    <h2>Essential Links</h2>
  </div>
</template>

<script>
import AmCharts from 'amcharts3'
// import AmSerial from 'amcharts3/amcharts/serial'
export default {
  name: "Statistics",
  created () {
    this.$store.dispatch("getStatistics");
    AmCharts.makeChart("a", "b", "c");
    AmCharts.makeChart("chart_div",
      {
        "type": "serial",
        "categoryField": "type",
        "chartCursor": {},
        "graphs": [
          {
            "type": "column",
            "title": "Pizza types",
            "valueField": "sold",
            "fillAlphas": 0.8
          }
        ],

        "dataProvider": [
          { "type": "Margherita", "sold": 120 },
          { "type": "Funghi", "sold": 82 },
          { "type": "Capricciosa", "sold": 78 },
          { "type": "Quattro Stagioni", "sold": 71 }
        ]
      }
    );
  }
}
</script>

<style scoped>

</style>