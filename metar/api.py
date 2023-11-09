import requests
from metar.utils import HEADERS
from metar.transformation import *
from metar.response import Response


class WeatherReport:
    """
    Class for fetching and processing weather data from an API endpoint.
    """

    headers = HEADERS
    base_url = "https://tgftp.nws.noaa.gov/data/observations/metar/stations/{}.TXT"

    def __init__(self, station) -> None:
        """
        Initializes a WeatherReport instance.

        Args:
        station (str): The station code for weather data retrieval.
        """
        self.data = Response()
        self.station = station

    def start_requests(self) -> dict:
        """
        Fetches weather data from the specified API endpoint.

        Returns:
        dict: Weather data for the station.
        """
        try:
            self.base_url = self.base_url.format(self.station)
            response = requests.get(url=self.base_url, headers=self.headers)
            response.raise_for_status()  # Raise exception for HTTP errors

            self.get_data(response)

            return {
                'station': self.data.station,
                'last_observation': self.data.last_observation,
                'temperature': self.data.temperature,
                'wind': self.data.wind,
            }

        except requests.exceptions.RequestException as e:
            # Handle any requests-related exceptions
            return {'error': f'Request failed: {str(e)}'}

        except Exception as e:
            # Handle other exceptions
            return {'error': str(e)}

    def get_data(self, response) -> None:
        """
        Extracts relevant weather data from the API response and sets it in the class.

        Args:
        response: The API response containing weather data.
        """
        try:
            last_observation = get_last_observation(response)
            raw_data = str(response.text).split('\n')[1].split()
            temperature = wind_direction_and_velocity = ""

            for data in raw_data:
                if data.endswith('KT'):
                    wind_direction_and_velocity = get_wind_direction_and_velocity(data)

                if '/' in data:
                    temperature = get_temperature(data)

            self.set_data(temperature, last_observation, wind_direction_and_velocity)

        except Exception as e:
            # Handle exceptions
            raise Exception(f"Error in get_data: {str(e)}")

    def set_data(self, temperature, last_observation, wind_direction_and_velocity) -> None:
        """
        Sets weather data in the class.

        Args:
        temperature (str): The temperature data.
        last_observation (str): The last observation data.
        wind_direction_and_velocity (str): The wind direction and velocity data.
        """
        try:
            self.data.temperature = temperature
            self.data.last_observation = last_observation
            self.data.station = self.station
            self.data.wind = wind_direction_and_velocity

        except Exception as e:
            # Handle exceptions
            raise Exception(f"Error in set_data: {str(e)}")
