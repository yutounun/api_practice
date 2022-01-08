from django.test import TestCase
from django.urls import reverse

class JobViewTests(TestCase):
  """JobViewSetのテストクラス"""

  def test_get_without_token(self):
      """アクセストークンなしでGETメソッドでJobViewTestsにアクセスしてステータスコード401を返されることを確認"""
      # tinder_appの'jobs-list'というurlのname(自動で決まる)にGETメソッド
      response = self.client.get(reverse('tinder:jobs-list'))
      # レスポンスのステータスコードが401になっているか。
      self.assertEqual(response.status_code, 401)
  