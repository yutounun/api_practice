from django.urls import path, include
from .views import *

urlpatterns = [
  path('member/', MemberViewSet.as_view({'get': 'list'}), name='get_all'),
]