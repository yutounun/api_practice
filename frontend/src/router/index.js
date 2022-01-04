import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import GetMembers from "@/components/GetMembers";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/get_members",
    name: "GetMembers",
    component: GetMembers
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
