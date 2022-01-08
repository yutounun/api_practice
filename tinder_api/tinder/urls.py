from django.urls import path, include
from .views import *
from django.db import router
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from tinder import views

app_name = 'tinder'

# simpleRouterでGETの場合はbasename+'-list'がnameとなる
router = routers.SimpleRouter()
router.register(r'member', MemberViewSet)
# GETのname = url+'s-list'
router.register(r'job', JobViewSet)

urlpatterns = router.urls