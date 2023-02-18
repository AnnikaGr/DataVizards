<template>
  <div id="my_dataviz"></div>
</template>

<script>
import * as d3 from "d3";
import { loadScript } from "vue-plugin-load-script";
import ApexCharts from "apexcharts";
import $ from 'jquery'
import { parse } from '@vanillaes/csv'

loadScript("/src/js/chart1.js");

import { csv } from "d3-fetch";
    function fetchData() {
        return csv('/ESS10-happy-posCorr-bigger-02.csv').then((data) => (data));
    }


export default {
  name: "MainVisualisation",
  async mounted() {

    let data = await fetchData();
    console.log(data)

    let retrieved_values=[];
    data.forEach(pair => retrieved_values.push(parseFloat(pair.values)))
    //let retrieved_values_str= retrieved_values.toString()


    let retrieved_labels=[];
    data.forEach(pair => retrieved_labels.push(pair.labels))
    //let retrieved_labels_str= retrieved_labels.toString()

    console.log(retrieved_values)
    console.log(retrieved_labels)

    data=[0.23673699407418608, 0.2641731833650158, 0.28407462823248225, 0.24639442105125345, 0.26871754777070994, 0.25592184161545756, 0.29162563858008844, 0.22076998267386777, 0.21243591866748937, 0.70709970630172]

    var options = {
      series:  retrieved_values,
      chart: {
        type: "polarArea",
      },
      colors: [
        function ({ value}) {
          if (value < 0.22) {
            return "#fff7bc";
          } else if (value < 0.3) {
            return "#fec44f";
          } else {
            return "#d95f0e";
          }
        },
      ],
      yaxis: {
        show: true,
        max: 1, // the lowest value that can be set is 1
        tickAmount: 4,
      },

      legend: {
        show: false,
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
              width: 600,
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
<style scoped>

</style>
