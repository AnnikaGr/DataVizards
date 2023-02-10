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
              series: [ 0.2370852082354777
                        ,0.2507875116539472
                       ,0.2683588174548252
                        ,0.23835858669205837
                        ,0.24968947355336563
                        ,0.23283863429138307
                       ,0.2710732821671339
                       ,0.21406876947669096
                        ,0.20534733463095653
                        ,0.684866018048639
                        ,0.3051872426611963
                        ,0.23313879215617025
                        ,0.2634083679204297
                        ,0.2212257015186353
                        ,0.28131399244217126
                        ,0.22437670805870788
                        ,0.2274772309894817
                        ,0.216120014957932
                        ,0.21891992544932298
                        ,0.2212981669898249,
                        0.22981531279765416,
                        0.2976172988773695,
                        0.3357803785680879],
              labels: ["netusoft", "ppltrst", "pplfair", "pplhlp", "trstprl", "trstlgl",
              "trstplc", "trstplt", "trstprt", "stflife", "stfeco", "stfgov", "stfdem",
              "stfedu", "stfhlth", "sclmeet", "inprdsc", "fairelcc", "hscopc19", "vdovexre",
              "aesfdrk", " health", "hincfel"],
              chart: {
              type: 'polarArea',
            },
            stroke: {
              colors: ['#fff']
            },
            fill: {
              opacity: 0.8
            },
            responsive: [{
              breakpoint: 480,
              options: {
                chart: {
                  width: 200
                },
                legend: {
                  position: 'bottom'
                }
              }
            }]
            };

            var chart = new ApexCharts(document.querySelector("#my_dataviz"), options);
            chart.render();
  },
};
</script>
<style scoped></style>
