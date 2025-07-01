from rest_framework import serializers
from .models import PlateLog

class PlateLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlateLog
        fields = '__all__'
