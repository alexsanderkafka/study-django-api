from ..model.scheduled import Scheduled
from rest_framework import serializers

class ScheduledSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scheduled
        fields = '__all__'