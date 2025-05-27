from django.shortcuts import render
from ..model.scheduled import Scheduled
from ..serializer.scheduled_serializer import ScheduledSerializer
from rest_framework import viewsets, generics

class ScheduledForLabView(generics.ListAPIView):
    serializer_class = ScheduledSerializer

    def get_queryset(self):
        return Scheduled.objects.filter(lab=self.kwargs['id'])


    