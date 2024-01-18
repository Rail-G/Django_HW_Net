from rest_framework import serializers
from .models import Sensor, Measurement

class MesurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'photo']

class SensorRUSerializer(serializers.ModelSerializer):
    mesaurement = MesurementsSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'mesaurement']

class SensorLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']