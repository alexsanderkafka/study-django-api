from ..model.lab import Lab
from rest_framework import serializers

class LabSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lab
        fields = '__all__'