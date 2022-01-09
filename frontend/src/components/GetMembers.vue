<template>
  <v-container>
    <v-row>
      <!-- ログイン画面 -->
      <v-col col="4"></v-col>
      <v-col col="4" class="loginPage" v-if="!tokens.access">
        <div class="loginPage mt-10">
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
            :append-icon="showPass ? 'mdi-eye' : 'mdi-eye-off'"
            :rules="[rules.required, rules.min]"
            :type="showPass ? 'text' : 'password'"
            name="input-10-1"
            @click:append="showPass = !showPass"
          ></v-text-field>
        </div>
        <!-- クリックするとloginメソッドを実行 -->
        <v-btn depressed outlined class="mr-15 pink--text" elevation="2" @click="login">SIGN IN</v-btn>
        <a @click="signup" class='ml-15 pink--text'>SIGN UPはこちら>>></a>
        <!-- Membersプロパティから -->
        <!-- scriptのuserプロパティに入力値が格納される -->
      </v-col>
      <v-col col="4"></v-col>
    </v-row>
    <v-row justify="center">
      <!-- ログイン後画面 -->
      <div v-if="tokens.access">
        <v-btn depressed outlined class="pink--text mb-5" @click="getInfo" elevation="2">メンバー情報を取得</v-btn>
        <!-- post画面 -->
        <v-dialog
          persistent
          v-model="showDialog"
          max-width="600px"
        >
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              depressed
              outlined
              elevation="2"
              class="pink--text mb-5 px-10 ml-10"
              dark
              v-bind="attrs"
              v-on="on"
            >
              メンバー登録
            </v-btn>
          </template>
          <v-card>
            <v-card-title>
              <span class="text-h5 pink--text">メンバー登録</span>
            </v-card-title>
            <v-card-text>
              <v-text-field
                label="名前"
                required
                v-model="postUsername"
              ></v-text-field>
              <v-select
                label="性別"
                required
                v-model="postGender"
                :items="['女性', '男性']"
              ></v-select>
              <v-text-field
                label="年齢"
                required
                v-model="postAge"
              ></v-text-field>
              <v-text-field
                label="自己紹介"
                v-model="postIntroduction"
              ></v-text-field>
              <v-select
                label="職業"
                v-model="postJob"
                required
                :items="['musician', 'developer']"
              ></v-select>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn
                class="pink--text"
                text
                @click="showDialog = false"
              >
                Close
              </v-btn>
              <v-btn
                class="pink--text"
                text
                @click="showDialig = false; postInfo()"
              >
                Save
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <!-- テーブル参照 -->
        <v-data-table
          :headers="headers"
          :items="Members"
          :items-per-page="5"
          class="elevation-1"
          v-show="showTable"
        ></v-data-table>
      </div>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      headers: [
        {
          text: '性別',
          align: 'start',
          sortable: false,
          value: 'gender',
        },
        { text: 'ユーザー名', value: 'username' },
        { text: '年齢', value: 'age' },
        { text: '自己紹介', value: 'introduction' },
        { text: '職業', value: 'job.job_name' },
        { text: '有給取得可能数', value: 'job.paid_holiday_count' },
        { text: '平均収入', value: 'job.average_salary' },
        { text: '休日休みか', value: 'job.is_holiday_on_weekend' },
      ],
      Members: [],
      tokens: {
        refresh: "",
        access: "",
      },
      username: "",
      password: "",
      showTable: false,
      showPass: false,
      rules: {
        required: value => !!value || 'Required.',
        min: v => v.length >= 8 || 'Min 8 characters'
      },
      postUsername:'',
      postGender:'',
      postAge:'',
      postIntroduction:'',
      postJob:'',
      showDialog: null
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
    // 職業をidに変更する
    changeJobToId: function(job){
      if (job=='musician') {
        return 1;
      }else{
        return 2;
      }
    },
    changeGender: function(gender){
      if (gender=='男性') {
        return "M";
      }else{
        return "F";
      }
    },
    // メンバー情報をバックエンドに送信
    postInfo: function () {
      const jobId = this.changeJobToId(this.postJob);
      const gender = this.changeGender(this.postGender)
      const data = {
        "gender": gender,
        "username": this.postUsername,
        "age": this.postAge,
        "introduction": this.postIntroduction,
        "job": jobId
      }
      console.log(this.postJob)
      this.axios
        .post("http://127.0.0.1:8000/api/v1/member/", data, {
          headers: {
            // postmanでのAPIcall同様にJWTが必要
            // 検証モードで確認できるヘッダー
            Authorization: "JWT " + this.tokens.access,
          },
        })
        // レスポンスをMembersプロパティに格納
        .then(() => {
          alert('登録完了')
          this.showDialog = false;
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
    signup: function() {
      // signupページに遷移
      this.$router.push({
        name: 'SignUp',
      })
    }
  },
};
</script>