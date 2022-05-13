from django.urls import path

from .views import *

urlpatterns = [

    path('metar/ping',pong , name='pong'),
    path('metar/info/',get_weather_report , name='get_weather_report'),
    
]