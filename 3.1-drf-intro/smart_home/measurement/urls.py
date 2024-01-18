from django.urls import path, include
from .views import MeasurementCreateList, SensorCreateList, SensorRetrieveUpdate
from rest_framework import routers

# router = routers.SimpleRouter()
# router.register(r'all_sensors', SensorViewSet)


# urlpatterns = [
#     path('measurements/', MeasurementCreateList.as_view()),
#     path('all_sensors/', SensorCreateList.as_view()),
#     path('all_sensors/<int:pk>/', SensorRetrieveUpdate.as_view()),
#     # path('', include(router.urls))
# ]
urlpatterns = [
    path('all_sensors/', SensorCreateList.as_view()),
    path('measurements/', MeasurementCreateList.as_view()),
    path('all_sensors/<int:pk>/', SensorRetrieveUpdate.as_view())
]