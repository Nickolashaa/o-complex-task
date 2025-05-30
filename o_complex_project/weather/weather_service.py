import requests
import os


def get_weather(town):
    try:
        api_key = os.environ.get("WEATHER_API_KEY")
        url = f"http://api.openweathermap.org/data/2.5/weather?q={town}&appid={api_key}&units=metric&lang=ru"
        response = requests.get(url).json()
        return f"Погода в городе {response['name']}: Температура: {response['main']['temp']}°C, ощущается как {response['main']['feels_like']}°C. В целом, {response['weather'][0]['description']}!"
    except Exception:
        return "Ошибка на стороне сервера. Извините..."
