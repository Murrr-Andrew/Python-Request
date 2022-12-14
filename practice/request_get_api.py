import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

params = {
    'q': 'Lviv',
    'appid': os.getenv('WEATHER_API_KEY')
}

response = requests.get('https://api.openweathermap.org/data/2.5/weather?', params=params)
weather = response.json()

print(weather)
