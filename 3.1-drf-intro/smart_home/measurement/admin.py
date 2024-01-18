from django.contrib import admin
from .models import Sensor, Measurement

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(Measurement)
class MesurementAdmin(admin.ModelAdmin):
    list_display = ('sensor_id', 'temperature', 'date')