<template>
  <div>
    <!-- ログイン画面 -->
    <div class='loginForm' v-if="!tokens.access">
      <input type="text" placeholder="username" v-model="username">
      <!-- scriptのpasswordプロパティに入力値が格納される -->
      <input type="text" placeholder="password" v-model="password">
      <!-- クリックするとloginメソッドを実行 -->
      <button @click="login">login</button>
      <!-- Membersプロパティから -->
      <!-- scriptのuserプロパティに入力値が格納される -->
    </div>
    <!-- ログイン後画面 -->
    <div v-if="tokens.access">
      <div v-for="(member, key) in Members" :key="key">
          <hr>
          <p>{{ member.username }}</p>
          <p>{{ member.gender }}</p>
          <p>{{ member.introduction }}</p>
          <p>{{ member.job }}</p>
          <hr>
        </div>
      <!-- クリックするとgetInfoメソッドを実行 -->
      <button @click="getInfo">メンバー情報を取得</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Members: [],
      tokens: {
        "refresh":'',
        "access":''
      },
      username: '',
      password: '',
    };
  },
  methods: {
    // メンバーの各情報を取得
    getInfo: function(){
      this.axios
      .get("http://127.0.0.1:8000/api/v1/member/",{headers: {
        // postmanでのAPIcall同様にJWTが必要
        // 検証モードで確認できるヘッダー
        "Authorization": 'JWT ' + this.tokens.access,
      }
      })
      // レスポンスをMembersプロパティに格納
      .then(response => (this.Members = response.data));
    },
    // usernameとpasswordからjwt認証を行いaccess_tokenとrefresh_tokenを取得
    login: function(){
      // token取得のためのusernameとpasswordセット
      const data = {username: this.username, password: this.password}
      // access_token&refresh_tokenを取得
      this.axios
        .post("http://127.0.0.1:8000/api-auth/jwt/",data)
        // レスポンスを一旦tokensプロパティに格納
        .then(response => (this.tokens = response.data));
    }
  }
};
</script>