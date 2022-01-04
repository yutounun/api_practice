<template>
  <div>
    <!-- ログイン画面 -->
    <div class="loginForm" v-if="!tokens.access">
      <!-- scriptのusernameプロパティに入力値が格納される -->
      <v-text-field
        label="username"
        :rules="rules"
        hide-details="auto"
        v-model="username"
      ></v-text-field>
      <!-- scriptのpasswordプロパティに入力値が格納される -->
      <v-text-field label="password" v-model="password"></v-text-field>
      <!-- クリックするとloginメソッドを実行 -->
      <v-btn color="pink lighten-1 white--text" elevation="2" @click="login">LOGIN</v-btn>
      <!-- Membersプロパティから -->
      <!-- scriptのuserプロパティに入力値が格納される -->
    </div>
    <!-- ログイン後画面 -->
    <div v-if="tokens.access">
      <v-btn  color="pink lighten-1 white--text" @click="getInfo" elevation="2">メンバー情報を取得</v-btn>
      <v-data-table
        :headers="headers"
        :items="Members"
        :items-per-page="5"
        class="elevation-1"
        v-show="showTable"
      ></v-data-table>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: 'gender',
          align: 'start',
          sortable: false,
          value: 'gender',
        },
        { text: 'username', value: 'username' },
        { text: 'age', value: 'age' },
        { text: 'introduction', value: 'introduction' },
        { text: 'job', value: 'job' },
      ],
      Members: [],
      tokens: {
        refresh: "",
        access: "",
      },
      username: "",
      password: "",
      showTable: false
    };
  },
  methods: {
    // メンバーの各情報を取得
    getInfo: function () {
      this.axios
        .get("http://127.0.0.1:8000/api/v1/member/", {
          headers: {
            // postmanでのAPIcall同様にJWTが必要
            // 検証モードで確認できるヘッダー
            Authorization: "JWT " + this.tokens.access,
          },
        })
        // レスポンスをMembersプロパティに格納
        .then((response) => {
          this.showTable = true
          this.Members = response.data
        });
    },
    // usernameとpasswordからjwt認証を行いaccess_tokenとrefresh_tokenを取得
    login: function () {
      // token取得のためのusernameとpasswordセット
      const data = { username: this.username, password: this.password };
      // access_token&refresh_tokenを取得
      this.axios
        .post("http://127.0.0.1:8000/api-auth/jwt/", data)
        // レスポンスを一旦tokensプロパティに格納
        .then((response) => (this.tokens = response.data));
    },
  },
};
</script>
