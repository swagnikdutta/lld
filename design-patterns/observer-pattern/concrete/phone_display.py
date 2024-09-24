from concrete.weather_station import WeatherStation
from interface.observer import Observer


class PhoneDisplay(Observer):
    def __init__(self, ws: WeatherStation):
        self.weather_station_instance = ws

    def update(self):
        print("PhoneDisplay: Something has changed. Updating phone display")
        # code to update phone's display with new temperature.
        # How to get the new temperature?
        # via the object of WeatherStation concrete class
        cur_temp = self.weather_station_instance.get_temperature()
        print(f"PhoneDisplay: Current temperature: {cur_temp}\n")
