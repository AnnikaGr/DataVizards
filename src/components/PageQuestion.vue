<template>
  <div class="row scrollable" id="question">
    <form class="my-auto">
      <div class="my-auto row">
        <div class="head scrollable col-sm-6 col-xs-12">
          <div class="row">
            <h1>Which are the 5 factors that you think related most to happiness?<br><br></h1>
            <button
                type="button"
                @click="handleSubmit"
                class="btn btn-lg btn-dark mx-auto"
                style="max-width: 30%"
            >Submit
            </button>

          </div>

        </div>

        <div class="my-auto scrollable col-sm-6 col-xs-12">
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
import {provide} from "vue";



function fetchData() {
  return csv("/labels_list.csv").then((data) => data);
}

export default {
  name: "PageQuestion",
  props: {
    confirmed: [],
  },
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
      this.validated = true;
      this.scrollToElement();
      this.passValues();
    },
    scrollToElement() {
      let element = document.getElementById("my_dataviz");
      try {
        element.scrollIntoView({behavior: "smooth", block: "end"});
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

<style scoped></style>
