import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
var csv = require('jquery-csv');

import './assets/main.css'

const app = createApp(App)

app.use(router)

app.mount('#app')
