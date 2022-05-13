import requests
from metar.utils import *
from metar.transformation import *
from metar.response import Response


class WeatherReport:

    headers = HEADERS
    base_url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/{}.TXT"

    def __init__(self, station) -> None:
        self.data = Response()
        self.station = station

    def start_requests(self) -> dict:
        self.base_url = self.base_url.format(self.station)
        response = requests.get(url=self.base_url, headers=self.headers)
        self.get_data(response)

        my_data = {
            'station': self.data.station,
            'last_observation': self.data.last_observation,
            'temperature': self.data.temperature,
            'wind': self.data.wind,
        }

        return my_data

    def get_data(self, response) -> None:

        last_observation = get_last_observation(response)
        raw_data = str(response.text).split('\n')[1].split()
        temperature = wind_direction_and_velocity = ""
        for data in raw_data:

            if data.endswith('KT'):
                wind_direction_and_velocity = get_wind_direction_and_velocity(
                    data)

            if '/' in data:
                temperature = get_temperature(data)

        self.set_data(temperature, last_observation,
                      wind_direction_and_velocity)

    def set_data(self, temperature, last_observation, wind_direction_and_velocity) -> None:
        self.data.temperature = temperature
        self.data.last_observation = last_observation
        self.data.station = self.station
        self.data.wind = wind_direction_and_velocity
