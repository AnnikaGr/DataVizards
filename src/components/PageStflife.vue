<template>
  <div class="row scrollable">
    <div class="head scrollable col-sm-5 col-xs-12">
      <div class="row">
        <h3>
          When people are happier, they are more satisfied with life as a whole.
        </h3>
      </div>
    </div>
    <div id="Stflife" class="my-auto scrollable col-sm-7 col-xs-12"></div>
  </div>
</template>

<script>
import ApexCharts from "apexcharts";
import { csv } from "https://cdn.skypack.dev/d3-fetch@3";

const dataSrc = new URL(`@/datasets/top5-vs-happy.csv`, import.meta.url).href;
function fetchData() {
  return csv(dataSrc).then((data) => data);
}
export default {
  name: "PageStflife",
  async mounted() {
    let data = await fetchData();

    let retrieved_values = [];
    data.forEach((pair) => retrieved_values.push(parseFloat(pair.AvgStflife)));

    let retrieved_labels = [];
    data.forEach((pair) => retrieved_labels.push(pair.Happy));

    var options = {
      series: [
        {
          name: "Life Satisfaction Level (0-10)",
          data: [...retrieved_values],
        },
      ],
      colors: ["#ea7531"],
      chart: {
        height: 350,
        type: "line",
        zoom: {
          enabled: false,
        },
      },
      dataLabels: {
        enabled: true,
      },
      stroke: {
        curve: "straight",
      },
      title: {
        text: "Average of How satisfied people are with life as a whole (0-10)",
        align: "left",
      },
      grid: {
        row: {
          colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
          opacity: 0.5,
        },
      },
      xaxis: {
        categories: [...retrieved_labels],
        title: {
          text: "How happy are you? (0-10)",
        },
      },
      yaxis: {
        decimalsInFloat: 0,
      },
    };

    var chart = new ApexCharts(document.querySelector("#Stflife"), options);
    chart.render();
  },
};
</script>
