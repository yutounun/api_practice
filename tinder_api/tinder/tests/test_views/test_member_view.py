from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate
from ...views import MemberViewSet
import json

class AuthMemberViewTests(APITestCase):
    """authorizedでGETメソッドでMemberViewTestsにアクセスしてステータスコード200を返されることを確認"""
    
    # ライフサイクルの初めにuser, tokenの作成を行う
    def setUp(self):
        # APIRequestFactoryのインスタンスを作成
        self.factory = APIRequestFactory()
        # Userのオブジェクトを作成、testDBに保存し、self.userへ代入
        self.user = User.objects.create_user(
            username='test', email='test@test.com', password='password')
        # self.userのログイン情報からtokenのオブジェクトを作成、
        # testDBに保存し、self.userへ代入
        self.token = Token.objects.create(user=self.user)
    
    # setUp後に実行される
    def test_token_auth(self):
        # JobViewSetにtokenをつけて、GETメソッド
        request = self.factory.get('tinder:members-list', HTTP_AUTHORIZATION='Token {}'.format(self.token))
        # requestにuserの認証情報を追加し、認証済みrequestにする
        force_authenticate(request, user=self.user)
        # as_viewはMemberViewSetのインスタンス(member_view)を生成するようなもの
        member_view = MemberViewSet.as_view({'get': 'list'})
        # 認証済みのリクエストをMemberViewSetのインスタンス(member_view)に送る
        response = member_view(request)
        # JobViewSetのレスポンスが200であることを確認
        self.assertEqual(response.status_code, 300)

class UnauthMemberViewTests(TestCase):
  """MemberViewSetのテストクラス"""
  def test_unauth_get(self):
      """unauthorizedでGETメソッドでMemberViewTestsにアクセスしてステータスコード401を返されることを確認"""
      # tinder_appの'members-list'というurlのname(自動で決まる)にGETメソッド
      response = self.client.get(reverse('tinder:members-list'))
      # レスポンスのステータスコードが401になっているか。
      self.assertEqual(response.status_code, 401)