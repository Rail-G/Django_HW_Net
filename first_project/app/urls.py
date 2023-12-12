from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home_view"),
    path('time/', views.time_view, name='time_view'),
    path('workdir/', views.workdir_view, name='workdir_view')
]