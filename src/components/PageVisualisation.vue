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

loadScript("/src/js/chart1.js");
loadScript("https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js");
loadScript("https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js");

export default {
  name: "MainVisualisation",
  mounted() {
    var options = {
      series: [
        0.237, 0.25, 0.268, 0.238, 0.249, 0.232, 0.271, 0.214, 0.205, 0.684,
        0.305, 0.233, 0.263, 0.221, 0.281, 0.224, 0.227, 0.216, 0.218, 0.221,
        0.229, 0.297, 0.335,
      ],
      labels: [
        "netusoft",
        "ppltrst",
        "pplfair",
        "pplhlp",
        "trstprl",
        "trstlgl",
        "trstplc",
        "trstplt",
        "trstprt",
        "stflife",
        "stfeco",
        "stfgov",
        "stfdem",
        "stfedu",
        "stfhlth",
        "sclmeet",
        "inprdsc",
        "fairelcc",
        "hscopc19",
        "vdovexre",
        "aesfdrk",
        " health",
        "hincfel",
      ],
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



  import ScrollReveal from "scrollreveal";
  loadScript("https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js");
  ScrollReveal().reveal(".form", { delay: 5000 });
  ScrollReveal().reveal('#my_dataviz', { delay: 10000 });


</script>
<style scoped>

</style>
