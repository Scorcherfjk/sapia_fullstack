import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    isAuth: false,
    token: "",
  },
  mutations: {
    loginSuccess(state) {
      state.isAuth = true;
    },
    updateToken(state, payload) {
      state.token = payload;
      localStorage.setItem('token', payload)
    },
    logOut(state) {
      state.isAuth = false;
      state.token = "";
      localStorage.removeItem('token')
    },
  },
  actions: {
    logInAction({ commit }, payload) {
      commit("loginSuccess");
      commit("updateToken", payload);
    },
    logOutAction({ commit }) {
      commit("logOut");
    },
  },
});
