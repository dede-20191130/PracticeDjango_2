from django.shortcuts import render
import django_filters
from rest_framework import viewsets

from blog.models import User, Entry
from blog.serializer import UserSerializer, EntrySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    filter_fields = {'author', 'status'}
