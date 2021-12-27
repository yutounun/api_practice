from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework_simplejwt import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('tinder.urls')),
    # jwt-tokenを取得
    path('api-auth/jwt/', views.TokenObtainPairView.as_view()),
    # jwt-tokenを再取得
    path('api-auth/jwt/refresh', views.TokenRefreshView.as_view()),
]