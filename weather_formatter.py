from weather_api import Weather


def format_weather(weather:Weather):
    return (f"{weather.city}, температура {weather.temperature}°C, "
    f"{weather.weather_type}\n"
    f"Восход: {weather.sunrise.strftime('%H:%M')}\n"
    f"Закат: {weather.sunset.strftime('%H:%M')}\n")
