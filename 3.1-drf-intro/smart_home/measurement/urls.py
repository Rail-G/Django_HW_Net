from django.urls import path
from .views import SensorCreateList, MeasurementCreateList, SensorRetrieveUpdate


urlpatterns = [
    path('all_sensors/', SensorCreateList.as_view()),
    path('measurements/', MeasurementCreateList.as_view()),
    path('all_sensors/<int:pk>', SensorRetrieveUpdate.as_view())
]
