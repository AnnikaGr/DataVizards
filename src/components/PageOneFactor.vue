<template>
  <div class="row">
    <div class="head col-sm-5 col-xs-12">
      <div class="row">
        <h3>
          {{ top_five_statements[this.$.vnode.key] }}
        </h3>
      </div>
    </div>
    <div
      :id="top_five_codes[this.$.vnode.key]"
      class="my-auto col-sm-7 col-xs-12"
    ></div>
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
  name: "PageOneFactor",

  data() {
    return {
      mins:[0,1,0,0,0],
      maxs:[10,4,10,10,10],
      top_five_attributes: [
        "Life satisfaction (0-10)",
        "Stress about household income (1-4)",
        "Economy satisfaction (0-10)",
        "Education satisfaction (0-10)",
        "Health services satisfaction (0-10)",
      ],
      top_five_codes: ["Stflife", "Hincfel", "Stfeco", "Stfedu", "Stfhlth"],
      top_five_titles: [
        "Average of how satisfied people are with life as a whole (0-10)",
        "Average of how stressed people feel about their household income (1-4)",
        "Average of how satisfied people are with country's economy (0-10)",
        "Average of how satisfied people are with country's education (0-10)",
        "Average of how satisfied people are with country's health services (0-10)",
      ],
      top_five_statements: [
        "Happiness positively correlates with life satisfaction.",
        "Happiness positively correlates with lower stress about people's household income.",
        "Happiness positively correlates with people's satisfaction in country's economy.",
        "Happiness positively correlates with people's satisfaction in country's education.",
        "Happiness positively correlates with people's satisfaction in country's health services.",
      ],
    };
  },
  mounted: async function () {
    let data = await fetchData();

    let retrieved_values = [];

    let s = "pair.Avg" + this.top_five_codes[this.$.vnode.key];
    data.forEach((pair) => retrieved_values.push(parseFloat(eval(s))));

    let retrieved_labels = [];
    data.forEach((pair) => retrieved_labels.push(pair.Happy));

    var options = {
      series: [
        {
          name: this.top_five_attributes[this.$.vnode.key],
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
        text: this.top_five_titles[this.$.vnode.key],
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
      axisTicks: {
        show: true,
        offsetX: 0,
        offsetY: 0,
      },
      yaxis: {
        min: this.mins[this.$.vnode.key],
        max: this.maxs[this.$.vnode.key],
        decimalsInFloat: 1,
      },
    };

    var chart = new ApexCharts(
      document.querySelector("#" + this.top_five_codes[this.$.vnode.key]),
      options
    );
    chart.render();
  },
};
</script>
