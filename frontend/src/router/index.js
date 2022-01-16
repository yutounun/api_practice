import Vue from "vue";
import VueRouter from "vue-router";
import GetMembers from "@/components/GetMembers";
import SignUp from "@/components/SignUp";

Vue.use(VueRouter);

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes : [
    {
      path: "/",
      name: "GetMembers",
      component: GetMembers
    },
    {
      path: "/signup",
      name: "SignUp",
      component: SignUp
    },
  ]
});

export default router;
