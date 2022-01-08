from django.test import TestCase
from django.urls import reverse, resolve
from ...views import MemberViewSet

class TestUrls(TestCase):
    def test_member_url(self):
        """tinder_appのurl:memberのクラス名とMemberViewSetクラス名が一致するか確認する"""
        # tinder_appのurl:memberのURLを代入
        view = reverse('tinder:members-list')
        self.assertEqual(resolve(view).func.__name__, MemberViewSet.__name__)