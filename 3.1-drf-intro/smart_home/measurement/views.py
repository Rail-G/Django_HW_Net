# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import viewsets
from .models import Sensor, Measurement
from .serializers import SensorLCSerializer, SensorRUSerializer, MesurementsAllSerializer

# class SensorViewSet(viewsets.ModelViewSet):
#     queryset = Sensor.objects.all()
#     serializer_class = SensorRUSerializer

class SensorCreateList(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorLCSerializer

class SensorRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorRUSerializer

class MeasurementCreateList(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MesurementsAllSerializer

