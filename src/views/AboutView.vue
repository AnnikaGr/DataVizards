<template>
  <div class="about">

<p>
<p>
      The data basis for this visualization is the
      <a
        href="https://www.europeansocialsurvey.org/"
        target="_blank"
        rel="noopener"
        >European Social Survey</a
      >.
</p>
<p>
    WHAT the visualizations show:
    The main visualization seen on the webpage is a preliminary version of our main visualization. We tested different libraries and selected relevant and interesting correlations to show in a sun-like shape that we will still rework for the final version.
</p>
<p>
    WHO the visualization is for:
    Anyone with an interest in the overall topic of happiness and factors that might have an influence on it. It could be specifically interesting to people from Europe or residing in Europe since the survey responses are limited to participants from Europe.
</p>
<p>
    WHY we the audience should care about it:
    We aim to raise an awareness about the strength of correlations of a variety of factors in relation to people’s happiness and overall well being. In our final visualization, we plan to encourage personal reflection before revealing the data visualization (Which 3 factors do you think impact your happiness the most? Which 3 factors do you think have the strongest correlation with the average European’s happiness?) to encourage people to actively think about the topic, reflect on their behaviour and potentially reveal misconceptions.
</p>
<p>
    HOW to read the visualization.
    Look at the visualization to gain an overview of the strength of the correlations of different factors and people’s responses about their happiness. A bigger sunray represents a stronger correlation. Hover over the sunray to read the exact correlation value and code of the survey question (to be replaced with the actual details about the questions).
</p>

  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }

  .text{
  display: flex;
      align-items: center;
  }
}

p{
margin: 50px;
font-size: 20px;
}

</style>
