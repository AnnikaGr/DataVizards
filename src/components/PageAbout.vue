<template xmlns="http://www.w3.org/1999/html">
  <div class="page row" id="about">
    <div
        data-aos="fade-down"
        data-aos-easing="ease-in"
        class="head scrollable col-sm-3 col-xs-12"
    >
      <div class="row">
        <h1 class="display-1"><b>Reflection</b><br /><br /></h1>
      </div>
    </div>

    <div
        data-aos="fade-down"
        data-aos-easing="ease-in"
        class="mx-auto my-auto scrollable col-sm-9 col-xs-12"
    >
      <h4>
        We now encourage you to take a moment to reflect on the topic. <br />
         Why do you think your choices matched or differed from the correlations measured in the survey?<br />
         How might such data be useful for policymakers or the general public?<br />
         What are other factors that make you happy and do you actively incorporate them in your daily life?<br />
      </h4>
    </div>
  </div>

  <div class="page row" id="about">
    <div
      data-aos="fade-down"
      data-aos-easing="ease-in"
      class="head scrollable col-sm-3 col-xs-12"
    >
      <div class="row">
        <h1 class="display-1"><b>About the data</b><br /><br /></h1>
      </div>
    </div>

    <div
      data-aos="fade-down"
      data-aos-easing="ease-in"
      class="mx-auto my-auto scrollable col-sm-9 col-xs-12"
    >
      <h5>
        The dataset used in this visualization was collected in the 10th
        European Social Survey (ESS) in 2022. ESS is a biennial survey of
        Europeans and the chosen dataset contains responses from over 33352
        individuals across 22 European countries. The data was gathered in
        face-to-face interviews and used questions on a range of topics relating
        to individual and societal well-being. <br />
        <br />We used Spearman’s rank correlation coefficient to calculate and
        showcase the strength and direction of the association between various
        factors and the responses on individuals’ happiness. We used this
        correlation coefficient since the dataset consisted of ordinal data and
        Spearman's correlation does not assume a linear relationship between the
        values. We selected questions with an absolute correlation stronger than
        0.2. While clearing up the data, we deleted the datasets of respondents
        wherein the individuals did not respond to one of the selected questions
        as well as overly specific questions. <br /><br />
        It is important to consider that correlations do not imply causation.
        Further research would be needed to determine whether there are causal
        relationships between the chosen factors and happiness. Moreover, the
        data is based on individuals' self-reported answers and might hence be
        subject to subjectivity and other biases.<br /><br />
        Online resource:
        <a
          href="https://ess-search.nsd.no/en/study/172ac431-2a06-41df-9dab-c1fd8f3877e7"
          >https://ess-search.nsd.no/en/study/172ac431-2a06-41df-9dab-c1fd8f3877e7</a
        >
      </h5>
    </div>
  </div>
</template>

<script>
export default {
  name: "PageAbout",
};
</script>

<style scoped></style>
