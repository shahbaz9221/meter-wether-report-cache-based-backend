
class Response:

    def __init__(self, station=None, last_observation=None, temperature=None, wind=None) -> None:
        self.station = station
        self.last_observation = last_observation
        self.temperature = temperature
        self.wind = wind

