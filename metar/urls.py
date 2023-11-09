from django.urls import path

from metar.views import pong, get_weather_report

urlpatterns = [

    path('metar/ping',pong , name='pong'),
    path('metar/info/',get_weather_report , name='get_weather_report'),
    
]