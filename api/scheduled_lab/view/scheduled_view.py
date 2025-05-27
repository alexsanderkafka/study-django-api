from django.shortcuts import render
from ..model.scheduled import Scheduled
from ..serializer.scheduled_serializer import ScheduledSerializer
from rest_framework import viewsets

class ScheduledView(viewsets.ModelViewSet):
    queryset = Scheduled.objects.all()
    serializer_class = ScheduledSerializer

