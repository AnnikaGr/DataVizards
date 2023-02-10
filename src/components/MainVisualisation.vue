<template>
  <div id="my_dataviz"></div>
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
              series: [
               0.237
                        ,0.250
                       ,0.268
                        ,0.238
                        ,0.249
                        ,0.232
                       ,0.271
                       ,0.214
                        ,0.205
                        ,0.684
                        ,0.305
                        ,0.233
                        ,0.263
                        ,0.221
                        ,0.281
                        ,0.224
                        ,0.227
                        ,0.216
                        ,0.218
                        ,0.221,
                        0.229,
                        0.297,
                        0.335],
              labels: ["netusoft", "ppltrst", "pplfair", "pplhlp", "trstprl", "trstlgl",
              "trstplc", "trstplt", "trstprt", "stflife", "stfeco", "stfgov", "stfdem",
              "stfedu", "stfhlth", "sclmeet", "inprdsc", "fairelcc", "hscopc19", "vdovexre",
              "aesfdrk", " health", "hincfel"],
              chart: {
              type: 'polarArea',
            },
            yaxis: {
                      show: true,
                      max: 1,
                    },
            colors:[function({ value, seriesIndex, w }) {
                      if (value < 0.1 ) {
                          return '#fff7bc'
                      } else if (value < 0.2) {
                         return '#fec44f'
                                              }
                       else {
                          return '#d95f0e'
                      }
                    }
                    ],
            legend: {
                show: true},
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
                  width: 600
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
