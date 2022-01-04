<template>
  <v-app>
    <v-app-bar app color="pink lighten-1 white--text" dark>
      <div class="d-flex align-center">
        <v-icon>mdi-head-heart-outline</v-icon>
        <h2>TINOER</h2>
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="https://github.com/yutounun/api_practice"
        target="_blank"
        text
      >
        <h3 class="mr-2">Github</h3>
        <v-icon>mdi-github</v-icon>
      </v-btn>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
