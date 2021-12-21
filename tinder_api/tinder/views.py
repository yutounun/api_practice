from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import Members
from .serializer import MemberSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Members.objects.all()
    serializer_class = MemberSerializer