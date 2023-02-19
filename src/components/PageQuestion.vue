<template>
  <div class="row scrollable" id="question">
    <form class="my-auto">
      <div class="my-auto row">
        <div class="head scrollable col-sm-6 col-xs-12" data-aos="fade-down" data-aos-easing="ease-in">
          <div class="row">
            <h1>
              Which are the 5 factors that you think related most to
              happiness?<br /><br />
            </h1>
            <button
              type="button"
              @click="handleSubmit"
              class="btn btn-lg custom-btn mx-auto"
              style="max-width: 30%"
            >
              Submit
            </button>
          </div>
        </div>

        <div class="my-auto scrollable col-sm-6 col-xs-12" data-aos="fade-down" data-aos-easing="ease-in">
          <div v-for="item in items" :key="item" class="form-check">
            <input
              class="form-check-input"
              type="checkbox"
              id="gridCheck1"
              :value="item"
              v-model="selected"
            />
            <label class="form-check-label" for="gridCheck1">
              {{ item }}
            </label>
          </div>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import { csv } from "d3-fetch";

const dataSrc = new URL(`@/datasets/ESS10-happy-allCorr-bigger-02.csv`, import.meta.url).href;
function fetchData() {
  return csv(dataSrc).then((data) => data);
}

export default {
  name: "PageQuestion",
  props: {
    confirmed: [],
  },
  computed: {},
  data() {
    return {
      items: [],
      selected: [],
      validated: false,
    };
  },
  methods: {
    passValues() {
      this.$emit("valuePass", this.selected);
    },
    handleSubmit() {
      if (this.selected.length !== 5) {
        alert("You need to choose 5 options to submit.");
      } else {
        this.validated = true;
        this.scrollToElement();
        this.passValues();
      }
    },
    scrollToElement() {
      let element = document.getElementById("my_dataviz");
      try {
        element.scrollIntoView({ behavior: "smooth", block: "end" });
      } catch (e) {
        console.log(e);
      }
    },
  },
  async mounted() {
    let data = await fetchData();
    let retrieved_labels = [];
    data.forEach((pair) => retrieved_labels.push(pair.labels));
    this.items = retrieved_labels;
  },
};
</script>

<style scoped>
.form-check-input:checked {
  background-color: lightskyblue !important;
  border: 0;
}
.form-check-input:focus,
.label::after,
label.form-check-label:focus,
.form-check-input::after,
.form-check-input:not(:disabled):not(.disabled):active:focus {
  color: black;
  outline: 0;
  border: 0;
  box-shadow: 0 0 0 0.1rem black !important;
}
.custom-btn{
  background-color: lightskyblue !important;
  color: white !important;
}
</style>
