<template>
  <div class="container-fluid mx-auto ">
    <PageIntro class="page row scrollable" ></PageIntro>
    <PageQuestion @valuePass="valueUpdate" class="large-page row scrollable"></PageQuestion>
    <PageVisualisation  class="page row scrollable"></PageVisualisation>
    <PageCompare class="page row scrollable" :selection="updatedValue"></PageCompare>
  </div>
</template>

<script>
import ScrollReveal from "scrollreveal";
import PageVisualisation from "@/components/PageVisualisation.vue";
import PageQuestion from "@/components/PageQuestion.vue";
import PageIntro from "@/components/PageIntro.vue";
import PageCompare from "@/components/PageCompare.vue";
import PageStflife from "@/components/PageStflife.vue";
export default {
  name: "MainRight",
  components: { PageCompare, PageIntro, PageQuestion, PageVisualisation },
  data() {
    return {
      currStep: null,
      updatedValue: [],
    };
  },
  methods: {
    valueUpdate(value) {
      this.updatedValue = [...value];
      console.log(this.updatedValue);
    }
  }
};
ScrollReveal().reveal(".scrollable", {
  delay: 800,
  duration: 500,
  reset: true,
});
</script>

<style>
.page {
  height: 100vh;
  min-width: 80vw;
}
.large-page {
  height: 150vh;
  min-width: 80vw;
}
.head {
  line-height: 1.5;
  max-height: 100vh;
}
.center {
  margin: auto;
  border: 3px solid #73ad21;
  padding: 10px;
}
@media (min-width: 1024px) {
  .head {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .head .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

}
</style>
