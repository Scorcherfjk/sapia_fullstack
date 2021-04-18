import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/register",
    name: "Register",
    component: () => import("../views/Register.vue"),
  },
  {
    path: "/login",
    name: "Login",
    component: () => import("../views/Login.vue"),
  },
  {
    path: "/users",
    name: "Users",
    component: () => import("../views/Users.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/message",
    name: "Message",
    component: () => import("../views/Message.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/profile",
    name: "Profile",
    component: () => import("../views/Profile.vue"),
    meta: { requiresAuth: true }
  },
  {
    path: "/update/user",
    name: "UpdateUser",
    component: () => import("../views/update/User.vue"),
    meta: { requiresAuth: true }
  },
  { path: "*", component: () => import("../views/PageNotFound.vue") },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
