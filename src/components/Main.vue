<template>
  <div class="container p-5 mx-auto mx-auto">
    <PageIntro class="page row"></PageIntro>
    <PageQuestion
      @valuePass="valueUpdate"
      class="large-page row"
    ></PageQuestion>
    <PageVisualisation class="slightly-large-page row" :selection="updatedValue"></PageVisualisation>
    <PageAbout></PageAbout>
    <PageAudience></PageAudience>
  </div>
</template>

<script>
import PageVisualisation from "@/components/PageVisualisation.vue";
import PageQuestion from "@/components/PageQuestion.vue";
import PageIntro from "@/components/PageIntro.vue";
import {loadScript} from "vue-plugin-load-script";
import AOS from "aos";
import "aos/dist/aos.css";
import PageAbout from "@/components/PageAbout.vue";
import PageAudience from "@/components/PageAudience.vue";
loadScript("https://unpkg.com/aos@2.3.1/dist/aos.js");
export default {
  name: "MainRight",
  components: {PageAudience, PageAbout, PageIntro, PageQuestion, PageVisualisation },
  data() {
    return {
      currStep: null,
      updatedValue: [],
    };
  },
  mounted() {
    AOS.init({
      // Global settings:
      offset: 120, // offset (in px) from the original trigger point
      delay: 0, // values from 0 to 3000, with step 50ms
      duration: 700, // values from 0 to 3000, with step 50ms
      easing: 'ease', // default easing for AOS animations
      once: false, // whether animation should happen only once - while scrolling down
      anchorPlacement: 'top-bottom', // defines which position of the element regarding to window should trigger the animation
    });
  },
  methods: {
    valueUpdate(value) {
      this.updatedValue = [...value];
      console.log(this.updatedValue);
    },
  },
};

</script>

<style>
.page {
  height: 100vh;
  min-width: 80vw;
}
.large-page {
  height: 180vh;
  min-width: 80vw;
}
.slightly-large-page {
  height: 120vh;
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
