from django.test import TestCase
from django.urls import reverse

class MemberViewTests(TestCase):
  """MemberViewSetのテストクラス"""

  def test_get_without_token(self):
      """アクセストークンなしでGETメソッドでMemberViewTestsにアクセスしてステータスコード401を返されることを確認"""
      # tinder_appの'members-list'というurlのname(自動で決まる)にGETメソッド
      response = self.client.get(reverse('tinder:members-list'))
      # レスポンスのステータスコードが401になっているか
      self.assertEqual(response.status_code, 401)