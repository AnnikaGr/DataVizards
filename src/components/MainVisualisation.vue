<template>
  <div id="my_dataviz"></div>
  <div id="another-vis"></div>
</template>

<script>
import * as d3 from "d3";
import { loadScript } from "vue-plugin-load-script";
import ApexCharts from "apexcharts";

loadScript("/src/js/chart1.js");

export default {
  name: "MainVisualisation",
  mounted() {
    var options = {
      series: [21, 17, 15, 10, 12, 17, 21],
      chart: {
        type: "polarArea",
      },
      stroke: {
        colors: ["#fff"],
      },
      fill: {
        opacity: 0.8,
      },
      responsive: [
        {
          breakpoint: 480,
          options: {
            chart: {
              width: 200,
            },
            legend: {
              position: "bottom",
            },
          },
        },
      ],
    };

    var chart = new ApexCharts(document.querySelector("#my_dataviz"), options);
    chart.render();
  },
};
</script>
<style scoped></style>
