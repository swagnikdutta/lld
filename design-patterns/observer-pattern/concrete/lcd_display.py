from concrete.weather_station import WeatherStation
from interface.observer import Observer


class LCDDisplay(Observer):
    def __init__(self, ws: WeatherStation):
        self.weather_station_instance = ws

    def update(self, ):
        print("LCDDisplay: Something has changed. Updating LCD display")
        # something has changed,
        # pull the latest data
        # how to pull? - use the instance of the WeatherStation concrete class
        cur_temp = self.weather_station_instance.get_temperature()
        print(f"LCDDisplay: Current temperature: {cur_temp}\n")
