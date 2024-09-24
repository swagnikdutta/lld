from concrete.lcd_display import LCDDisplay
from concrete.phone_display import PhoneDisplay
from concrete.weather_station import WeatherStation

if __name__ == '__main__':
    # creating instance of concrete observable class
    ws = WeatherStation()

    # creating instances of concrete observer classes
    phone_display = PhoneDisplay(ws)
    lcd_display = LCDDisplay(ws)

    # registering the observers to the observable
    ws.add(phone_display)
    ws.add(lcd_display)

    ws.activate_sensors()




