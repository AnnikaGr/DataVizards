<template>
  <h2 class="head scrollable col-sm-6 col-xs-12">
    The strength of the correlations of different factors and people’s
    responses about their happiness. A bigger sunray represents a stronger
    correlation. Hover over the sunray to read the exact correlation value
    and code of the survey question (to be replaced with the actual details
    about the questions).
  </h2>
  <div id="my_dataviz" class="my-auto scrollable col-sm-6 col-xs-12"></div>
</template>

<script>
import * as d3 from "d3";
import { loadScript } from "vue-plugin-load-script";
import ApexCharts from "apexcharts";
import $ from 'jquery'
import { parse } from '@vanillaes/csv'

loadScript("/src/js/chart1.js");
loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js");
loadScript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js");

import { csv } from "d3-fetch";
    function fetchData() {
        return csv('/ESS10-happy-allCorr-bigger-02.csv').then((data) => (data));
    }


export default {
  name: "MainVisualisation",
  async mounted() {

    let data = await fetchData();
    console.log(data)

    let retrieved_values=[];
    data.forEach(pair => retrieved_values.push(parseFloat(pair.values)))

    let retrieved_labels=[];
    data.forEach(pair => retrieved_labels.push(pair.labels))

    console.log(retrieved_values)
    console.log(retrieved_labels)

    var options = {
      series:  retrieved_values,
      labels: retrieved_labels,
      chart: {
        type: "polarArea",
      },
      colors: [
        function ({ value}) {
          if (value < 0.22) {
            return "#ffca36";
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



  import ScrollReveal from "scrollreveal";
  loadScript("https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js");
  ScrollReveal().reveal(".form", { delay: 5000 });
  ScrollReveal().reveal('#my_dataviz', { delay: 10000 });


</script>
<style scoped>

</style>
