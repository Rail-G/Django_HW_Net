from rest_framework import serializers
from .models import Sensor, Measurement

class MesurementsAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor_id', 'temperature', 'date', 'photo']

class MesurementsNotAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date', 'photo']

class SensorRUSerializer(serializers.ModelSerializer):
    mesaurement = MesurementsNotAllSerializer(read_only=True, many=True)
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'mesaurement']
        

class SensorLCSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']