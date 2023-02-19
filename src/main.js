import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";
import "./assets/main.css";
import ScrollReveal from "scrollreveal";
import "d3-fetch";
const app = createApp(App);

app.use(router);
// In main.js
app.use(ScrollReveal);
app.mount("#app");
