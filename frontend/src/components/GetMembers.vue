<template>
  <div>
    <div v-for="(member, key) in Members" :key="key">
      <hr>
      <p>{{ member.username }}</p>
      <hr>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      Members: []
    };
  },
  // ページを読み込んでマウントを行っている状態
  mounted() {
    this.axios
      .get("http://127.0.0.1:8000/api/v1/member/",{
        // headers: {
        //   Authorization: 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjQwNzY4ODIyLCJqdGkiOiIzNGIzMjgwNDMxMzU0MWViYjJkYjljYjdmNzIwN2E0ZiIsInVzZXJfaWQiOjF9.Z5uHYv8A6V39Z_DkcSAIcsDzIXS8V9kzQCtVnJyj7qg',
        // }
      })
      // レスポンスをMembersプロパティに格納
      .then(response => (this.Members = response.data));
  }
};
</script>