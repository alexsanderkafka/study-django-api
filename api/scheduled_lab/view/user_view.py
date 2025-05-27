from django.shortcuts import render
from ..model.user import User
from ..serializer.user_serializer import UserSerializer
from rest_framework import viewsets

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer