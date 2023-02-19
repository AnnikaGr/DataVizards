<template>
  <div class="row scrollable" id="vis">
    <div class="head scrollable col-sm-4 col-xs-12">
      <div class="row">
        <h4>
          In 2020, 33352 Europeans were questioned about various aspects of their lives. Here you can
          see the correlations (0-1) of people’s responses about different factors in their life with their overall happiness. These correlations might mean
          that higher happiness is caused by these factors, or that higher happiness causes itself better rating of the factor, but there might also be no causation at all.
          <br />
          <br />
          <br />Explore the top 5 factors correlating with happiness : <br />
          <br />
          <div v-for="(item, index) in top_five_strings" :key="item">
            <button
              type="button"
              class="btn btn-light bg-transparent m-2 btn-custom p-3"
              data-bs-toggle="modal"
              :data-bs-target="`#exampleModal`"
              @click="buttonPressed(index)"
            >
              {{ item }}</button
            ><br />
          </div>
        </h4>
        <!-- Button trigger modal -->

        <!-- Modal -->

        <div
          class="modal fade modal-xl"
          :id="`exampleModal`"
          tabindex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel"></h1>
                <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <div class="modal-body">
                <PageOneFactor :key="factorIndex"></PageOneFactor>
              </div>
            </div>
          </div>
        </div>

        <p>
          <br />
          A bigger sunray represents a stronger correlation. Hover over the
          sunray to read the exact correlation value and code of the survey
          question (to be replaced with the actual details about the questions).
        </p>
      </div>
    </div>
    <div
      data-aos="fade-down"
      data-aos-easing="ease-in"
      id="my_dataviz"
      class="my-auto scrollable col-sm-8 col-xs-12"
    ></div>
    <div class="sticky-bottom text-center">
      <a
        href="#about"
        class="ca3-scroll-down-link ca3-scroll-down-arrow"
        data-ca3_iconfont="ETmodules"
        data-ca3_icon=""
      ></a>
    </div>
  </div>
</template>

<script>
import * as d3 from "d3";
import { loadScript } from "vue-plugin-load-script";
import ApexCharts from "apexcharts";
import PageOneFactor from "./PageOneFactor.vue";
import { csv } from "d3-fetch";

const dataSrc = new URL(
  `@/datasets/ESS10-happy-allCorr-bigger-02.csv`,
  import.meta.url
).href;
function fetchData() {
  return csv(dataSrc).then((data) => data);
}

export default {
  name: "PageVisualisation",
  components: { PageOneFactor },
  data() {
    return {
      factorIndex: 0,
      top_five_strings: [
        "General life satisfaction",
        "Feeling about household income",
        "Satisfaction with country's economy",
        "Satisfaction with country's education",
        "Satisfaction with country's health services",
      ],
    };
  },
  props: ["selection"],
  methods: {
    buttonPressed(index) {
      this.factorIndex = index;
    },
    async initChart() {
      document.querySelector("#my_dataviz").innerHTML = "";
      console.log("mounted called");
      let data = await fetchData();

      let retrieved_values = [];
      data.forEach((pair) => retrieved_values.push(parseFloat(pair.values)));

      let retrieved_labels = [];
      data.forEach((pair) => retrieved_labels.push(pair.labels));

      let selected_indeces = [];
      this.selection.forEach((selected) =>
        selected_indeces.push(
          retrieved_labels.findIndex((label) => label === selected)
        )
      );

      console.log("selected indices" + selected_indeces);


        var options = {
          series: retrieved_values,
          labels: retrieved_labels,
          chart: {
            type: "polarArea",
          },
          colors: [
            function ({ value,seriesIndex }) {
              if (selected_indeces.includes(seriesIndex)){
                return "#87CEFAFF";
              }
              else if (value < 0.22) {
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

      var chart = new ApexCharts(
        document.querySelector("#my_dataviz"),
        options
      );
      chart.render();
    },
  },
  async beforeUpdate() {
    console.log("beforeUpdate called");
    this.initChart();
  },
  async mounted() {
    this.initChart();
  },
};

import ScrollReveal from "scrollreveal";
loadScript("https://unpkg.com/scrollreveal@4.0.0/dist/scrollreveal.min.js");
ScrollReveal().reveal(".form", { delay: 5000 });
ScrollReveal().reveal("#my_dataviz", { delay: 10000 });
</script>
<style scoped>
.btn-custom{
  border-color: #ea7531;
}

</style>
