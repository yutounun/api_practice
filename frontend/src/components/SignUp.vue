<template>
  <v-container>
    <v-row>
      <v-col col="4"></v-col>
      <v-col col="4">
        <div class="mt-10">
          <!-- scriptのusernameプロパティに入力値が格納される -->
          <v-text-field
            label="username"
            hide-details="auto"
            v-model="username"
          ></v-text-field>
          <!-- scriptのpasswordプロパティに入力値が格納される -->         
          <v-text-field
            label="password"
            v-model="password"
            :rules="[rules.required, rules.min]"
            :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
            :type="showPass ? 'text' : 'password'"
            name="input-10-1"
            @click:append="showPass = !showPass"
          ></v-text-field>
        </div>
        <v-btn depressed outlined class="mr-15 pink--text" elevation="2" @click="regist">SIGN UP</v-btn>
        <a @click="signin" class='ml-15 pink--text'>SIGN INはこちら>>></a>
      </v-col>
      <v-col col="4"></v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    username: "",
    password: "",
    showPass: false,
    rules: {
      required: value => !!value || 'Required.',
      min: v => v.length >= 8 || 'Min 8 characters'
    },
  }),
  methods:{
    signin: function() {
      this.$router.push({
        name: 'GetMembers',
      })
    },
    regist:function() {
      const data = { username: this.username, password: this.password };
      // access_token&refresh_tokenを取得
      this.axios
        .post("http://127.0.0.1:8000/api/v1/regist/", data)
        // レスポンスを一旦tokensプロパティに格納
        .then((response) => {
          this.tokens = response.data
          alert('登録完了！')
          // GetMembersページに遷移
          this.$router.push({
            name: 'GetMembers',
          })
        });
    }
  }
};
</script>