<template>
  <div class="page row scrollable">
    <form class="my-auto">
      <div class="my-auto row">
        <h1 class="head scrollable col-sm-6 col-xs-12">
          Which are the factors that you think related most to happiness?
        </h1>
        <div class="my-auto scrollable col-sm-6 col-xs-12">
          <div v-for="item in items" :key="item" class="form-check">
            <input class="form-check-input" type="checkbox" id="gridCheck1" />
            <label class="form-check-label" for="gridCheck1">
              {{ item }}
            </label>
          </div>
        </div>
      </div>
      <button type="submit" class="btn btn-lg btn-dark">Submit</button>
    </form>
  </div>
</template>

<script>
import { csv } from "d3-fetch";

function fetchData() {
  return csv("/ESS10-happy-allCorr-bigger-02.csv").then((data) => data);
}

export default {
  name: "PageQuestion",
  data() {
    return {
      items: [],
    };
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
