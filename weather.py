# Weather Application
import requests
import geocoder
import openweathermapy.core as owm
import json

def weatherFinder():
    F = '\u00b0' + 'F'
    APIKEY = "35abd900cd915a1260ef23b5d5b0f238"
    location = geocoder.ip('me')
    (lat, lon) = location.latlng
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={round(lat)}&lon={round(lon)}&appid={APIKEY}"
    page = requests.get(url)
    x = page.json()
    
    temp = (x['main']['temp'] - 273.15)*(9/5) + 32
    max_temp = (x['main']['temp_max'] - 273.15)*(9/5) + 32
    min_temp = (x['main']['temp_min'] - 273.15)*(9/5) + 32
    humidity = x['main']['humidity']
    wind_speed = x['wind']['speed']*2.237
    weather_type = x['weather'][0]['main']
    weather_subtype = x['weather'][0]['description']

    print(f"The type of weather: {weather_type} with {weather_subtype}")
    print(f"Temperature now: {round(temp)}{F}")
    print(f"Maximum temperature: {round(max_temp)}{F}")
    print(f"Minimum temperature: {round(min_temp)}{F}")
    print(f"Humidity ratio: {humidity}%")
    print(f"Wind speed: {round(wind_speed, 2)} mph")

if __name__ == "__main__":
    weatherFinder()
