from pyowm import OWM

owm = OWM('5dfdd607d0c33f12e428ca24dce76755')
mgr = owm.weather_manager()

city = input("Enter the city: ")

observation = mgr.weather_at_place(city)
w = observation.weather


print(f'\nStatus - {w.detailed_status.capitalize()}')
print(f'Temperature: {w.temperature("celsius")["temp"]} C \nFeels like: {w.temperature("celsius")["feels_like"]} C')
print(f'Visibility distance: {w.visibility_distance/1000} km')
print(f'Humidity: {w.humidity} %')
print(f'Pressure: {w.pressure["press"]} hPa\n')
