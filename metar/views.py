from metar.models import WeatherData
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from metar.api import WeatherReport
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings ,'CACHE_TTL' , DEFAULT_TIMEOUT)


def pong(request) -> JsonResponse:
    """
    Responds with a JSON object containing 'pong'.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: A JSON response with 'pong'.
    """
    try:
        response = {
            'data': 'pong'
        }
        return JsonResponse(response)
    except Exception as e:
        return JsonResponse({'error': str(e)})


def get_weather_report(request) -> JsonResponse:
    """
    Retrieves weather report data based on the provided parameters.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    JsonResponse: A JSON response with weather report data.
    """
    try:
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
            scode = get_scode(data, filter_scode)
            cache.set_many(scode)
        else:
            scode = data

        my_data = {
            'data': scode
        }
        return JsonResponse(my_data)
    except Exception as e:
        return JsonResponse({'error': str(e)})



def get_scode(data, filter_scode=None):
    """
    Retrieves weather data for a specific station code.

    Args:
    data (dict): The weather data.
    filter_scode (str, optional): The station code to filter. Defaults to None.

    Returns:
    dict: The weather data for the specified station code.
    """
    try:
        station_code = data.get("station")

        if WeatherData.objects.filter(station_code=station_code).exists():
            print("DATA COMING FROM DB")
            scode = WeatherData.objects.get(station_code=station_code)
            return {
                'station': scode.station_code,
                'last_observation': scode.last_observation,
                'temperature': scode.temperature,
                'wind': scode.wind
            }

        else:
            weather_data = WeatherData(station_code=station_code, last_observation=data.get("last_observation", ""), temperature=data.get("temperature", ""), wind=data.get("wind", ""))
            weather_data.save()
            return {'data': data}

    except Exception as e:
        return JsonResponse({'error': str(e)})