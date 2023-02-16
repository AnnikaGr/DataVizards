<template>
  <div class="container" style="max-width: 100%">
    <div class="page row scrollable">
      <PageIntro></PageIntro>
    </div>

    <div class="page row scrollable">
      <PageQuestion></PageQuestion>
    </div>

    <div class="page row scrollable">
      <MainVisualisation></MainVisualisation>
    </div>

    <!-- This section will reveal itself each time it's scrolled into view -->

    <!-- Element-specific configuration options can be passed like this -->
    <div class="page scrollable">
      <h1>Slightly late tada!</h1>
    </div>
  </div>
</template>

<script>
import ScrollReveal from "scrollreveal";
import MainVisualisation from "@/components/PageVisualisation.vue";
import PageQuestion from "@/components/PageQuestion.vue";
import PageIntro from "@/components/PageIntro.vue";
export default {
  name: "MainRight",
  components: {PageIntro, PageQuestion, MainVisualisation },
  data() {
    return {
      currStep: null,
    };
  },
};
ScrollReveal().reveal(".scrollable", {
  delay: 500,
  duration: 500,
  reset: true,
});
</script>

<style>
.page {
  height: 100vh;
  width: 90vw;
}
.head {
  line-height: 1.5;
  max-height: 100vh;
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

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
