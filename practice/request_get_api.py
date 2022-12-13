import requests
import apikey


params = {
    'q': 'Lviv',
    'appid': apikey.WEATHER_API_KEY
}

response = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params)
weather = response.json()

print(weather)
