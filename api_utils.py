import requests

from constants import WEATHER_API_ID


def get_city_weather(city):
    params = {
        "q": city,
        "appid": WEATHER_API_ID,
        "units": "metric"
    }
    response = requests.get(
        f'https://api.openweathermap.org/data/2.5/weather',
        params=params
    )

    if response.status_code == 200:
        return response.json()
