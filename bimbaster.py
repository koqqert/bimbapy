#homework
import requests
from datetime import timedelta, datetime

API_KEY = 'твой токен'
def get_coords(city_name):
    url = 'https://api.openweathermap.org/geo/1.0/direct?'
    params = {
        'q': city_name,
        'appid': API_KEY,
        'limit': 1
    }
    response = requests.get(url, params=params)
    data = response.json()[0]
    return data['lat'], data['lon'], print(f"Широта: {data['lat']}"), print(f"Долгота: {data['lon']}")
def get_weather(city_name):
    coords = get_coords(city_name)
    url = 'https://api.openweathermap.org/data/2.5/weather?'
    params = {
        'lat': coords[0],
        'lon': coords[1],
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    data = response.json()
    main = data['main']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    return f"Время нахождения Солнца на небе: {timedelta(seconds=sunset - sunrise)}"
