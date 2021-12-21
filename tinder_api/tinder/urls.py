from django.urls import path
from .views import *

urlpatterns = [
  path('member/', MemberViewSet.as_view({'get': 'list'}), name='get_all'),
  path('member/<str:member_id>/', SpecificMemberAPIView.as_view(), name='get_all'),
]