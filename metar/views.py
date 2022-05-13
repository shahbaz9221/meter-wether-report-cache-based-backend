from http.client import HTTPResponse
from .models import *
import ast
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from django.http import JsonResponse
from metar.api import WeatherReport

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)


def pong(request) -> JsonResponse:
    response = {
        'data': 'pong'
    }
    return JsonResponse(response)

def get_weather_report(request) -> JsonResponse:
    filter_scode = request.GET.get('scode')
    nocache = request.GET.get('nocache')
    weather_data = WeatherReport(filter_scode)
    data = weather_data.start_requests()
    if nocache == "1":
        cache.clear()
        cache.set_many(data)
        scode = data


    elif cache.get_many(list(data.keys())):
        print("DATA COMING FROM CACHE")
        scode = cache.get_many(list(data.keys()))
    elif filter_scode:
        
        scode = get_scode(data,filter_scode)
        cache.set_many(scode)
    
        
    my_data = {
        'data': scode
    }
    return JsonResponse(my_data)



def get_scode(data,filter_scode = None):
    if WeatherData.objects.filter(station_code=data.get("station")).exists():
        print("DATA COMING FROM DB")
        scode = WeatherData.objects.get(station_code=data.get("station"))
        my_dict ={
            'station':scode.station_code,
            'last_observation':scode.last_observation,
            'temperature':scode.temperature,
            'wind':scode.wind
        }
        return my_dict
    else:
        weather_data = WeatherData(station_code=data.get("station"),last_observation=data.get("last_observation",""),temperature=data.get("temperature",""),wind=data.get("wind",""))
        weather_data.save()
        return JsonResponse({'data': data})