from django.urls import path, include
from .views import *
from django.db import router
from rest_framework import routers
from tinder import views

router = routers.SimpleRouter()
# 全てのHTTPメソッドに対応
router.register(r'member', MemberViewSet)
urlpatterns = router.urls