from django.db import models

# Create your models here.


class WeatherData(models.Model):
    station_code = models.CharField(max_length=100)
    last_observation = models.CharField(max_length=100)
    temperature = models.CharField(max_length=100)
    wind = models.CharField(max_length=100)
    
    def __str__(self):
        return self.station_code