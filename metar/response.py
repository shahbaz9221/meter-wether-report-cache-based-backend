class Response:
    """
    Represents a response containing weather data.

    Attributes:
    - station (str): The station code.
    - last_observation (str): The last observation timestamp.
    - temperature (str): The temperature data.
    - wind (str): The wind data.
    """

    def __init__(self, station=None, last_observation=None, temperature=None, wind=None) -> None:
        """
        Initializes a Response object with weather data.

        Args:
        - station (str): The station code.
        - last_observation (str): The last observation timestamp.
        - temperature (str): The temperature data.
        - wind (str): The wind data.
        """
        try:
            self.station = station
            self.last_observation = last_observation
            self.temperature = temperature
            self.wind = wind

        except Exception as e:
            # Handle exceptions
            raise Exception(f"Error in Response initialization: {str(e)}")
