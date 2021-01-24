# modules needed:
# pyowm
# pip install pyowm

import pyowm

api_key = "87c14a67417ff9c291fe0151ab902668"
owm = pyowm.OWM(api_key)
cityName = input("Enter city name")
place = owm.weather_at_place(cityName)
w = place.get_weather()
temperature = w.get_temperature()['temp']
windSpeed = w.get_wind()['speed']
status = w.get_status()
detailedStatus = w.get_detailed_status()
print(temperature, "K")
print(windSpeed, "m/s")
print("brief status:", status)
print("detailed status:", detailedStatus)
