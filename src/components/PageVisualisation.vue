<template>
  <div class="vis row scrollable">
    <div class="head scrollable col-sm-5 col-xs-12">
      <div class="row">
        <h3>
          In 2022, 33352 Europeans were questioned about various factors. This is the correlations of different factors and people’s responses
          about their happiness. <br />The top 5 factors are: <br /> <br />
          <b>Life satisfaction level</b><br />
          <b>Feeling about household income</b><br />
          <b>Economy satisfaction level</b><br />
          <b>Education satisfaction level</b><br />
          <b>Health service satisfaction level</b><br />
        </h3>
        <p> <br />
          A bigger sunray represents a stronger correlation. Hover over the sunray
          to read the exact correlation value and code of the survey question (to be
          replaced with the actual details about the questions).
        </p>
      </div>
    </div>
    <div id="my_dataviz" class="my-auto scrollable col-sm-7 col-xs-12"></div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { loadScript } from "vue-plugin-load-script";
import ApexCharts from "apexcharts";
import { parse } from "@vanillaes/csv";

loadScript("/src/js/chart1.js");
loadScript(
  "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js"
);
loadScript(
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.min.js"
);

import { csv } from "d3-fetch";
function fetchData() {
  return csv("/labels_list.csv").then((data) => data);
}

export default {
  name: "PageVisualisation",
  async mounted() {
    let data = await fetchData();

    let retrieved_values = [];
    data.forEach((pair) => retrieved_values.push(parseFloat(pair.values)));

    let retrieved_labels = [];
    data.forEach((pair) => retrieved_labels.push(pair.labels));

    console.log(retrieved_values);
    console.log(retrieved_labels);

    var options = {
      series: retrieved_values,
      labels: retrieved_labels,
      chart: {
        type: "polarArea",
      },
      colors: [
        function ({ value }) {
          if (value < 0.22) {
            return "#fdefb1";
          } else if (value < 0.3) {
            return "#fec44f";
          } else {
            return "#ea7531";
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
      tooltip: {
        enabled: true,
        enabledOnSeries: undefined,
        shared: true,
        followCursor: false,
        intersect: false,
        inverseOrder: false,
        custom: undefined,
        fillSeriesColor: true,
        theme: false,
        style: {
          fontSize: "12px",
          fontFamily: undefined,
        },
        onDatasetHover: {
          highlightDataSeries: false,
        },
        marker: {
          show: true,
        },
      },
    };

    var chart = new ApexCharts(document.querySelector("#my_dataviz"), options);
    chart.render();
  },
};

import ScrollReveal from "scrollreveal";
loadScript("https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js");
ScrollReveal().reveal(".form", { delay: 5000 });
ScrollReveal().reveal("#my_dataviz", { delay: 10000 });
</script>
<style scoped></style>
