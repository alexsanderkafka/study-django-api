from django.shortcuts import render
from ..model.teacher import Teacher
from ..serializer.teacher_serializer import TeacherSerializer
from rest_framework import viewsets

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer