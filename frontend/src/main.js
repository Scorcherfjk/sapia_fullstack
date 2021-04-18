import Vue from "vue";
import App from "./App.vue";
import store from "./store";
import router from "./router";
import axios from "axios";

import "@/assets/css/tailwind.css";

Vue.config.productionTip = false;

axios.interceptors.response.use(
  function(response) {
    if (response.status == 401) {
      localStorage.removeItem('token')
      router.replace("/login");
    }
    return response;
  },
  function(error) {
    if (error.response.status > 400  && router.currentRoute.path != "/login") {
      localStorage.removeItem('token')
      router.replace("/login");
    }
    return Promise.reject(error);
  }
);

router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth) {
    if (store.state.isAuth) {
      next();
    } else {
      if(localStorage.token){
        store.dispatch("logInAction", localStorage.token)
        next()
      } else {
        next("/login");
      }
    }
  } else {
    next();
  }
});

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
