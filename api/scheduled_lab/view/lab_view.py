from django.shortcuts import render
from ..model.lab import Lab
from ..serializer.lab_serializer import LabSerializer
from rest_framework import viewsets

class LabView(viewsets.ModelViewSet):
    queryset = Lab.objects.all()
    serializer_class = LabSerializer

    