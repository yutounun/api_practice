from django.test import TestCase
from django.urls import reverse, resolve
from ...views import JobViewSet

class TestUrls(TestCase):
    def test_job_url(self):
        """tinder_appのurl:jobのクラス名とJobViewSetクラス名が一致するか確認する"""
        # tinder_appのurl:jobのURLを代入
        view = reverse('tinder:jobs-list')
        self.assertEqual(resolve(view).func.__name__, JobViewSet.__name__)