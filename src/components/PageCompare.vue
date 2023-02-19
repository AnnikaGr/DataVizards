<template>
  <div class="page row scrollable" id="compare">
    <div
      class="head scrollable col-sm-6 col-xs-12"
      data-aos="fade-down"
      data-aos-easing="ease-in"
    >
      <div class="row">
        <h3>
          Your top 5 factors are: <br />
          <br />
        </h3>
        <div v-for="item in selection" :key="item" class="form-check">
          <h4>
            <b>
              {{ item }}
            </b>
          </h4>
        </div>
      </div>
    </div>

    <div
      class="mx-auto my-auto scrollable col-sm-6 col-xs-12"
      data-aos="fade-down"
      data-aos-easing="ease-in"
    >
      <img
        src="../assets/happyintro.jpg"
        class="img-fluid rounded mx-auto d-block"
        alt="happy"
      />
    </div>
  </div>
</template>

<script>
export default {
  name: "PageCompare",
  props: ["selection"],
};
</script>

<style scoped></style>
