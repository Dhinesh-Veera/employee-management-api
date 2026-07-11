import requests
from requests.exceptions import Timeout, RequestException
from django.conf import settings
import logging

logger = logging.getLogger(__name__)


class WeatherService:
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather" #Class Variable

    @staticmethod
    def get_current_weather(city):
        logger.info(f"Fetching weather for city: {city}")
        params = {
            "q": city,
            "appid": settings.WEATHER_API_KEY,
            "units": "metric"
        }
        try:

            response = requests.get(WeatherService.BASE_URL, params=params, timeout=10)

            response.raise_for_status()

            weather_data = response.json()
            logger.info("Weather data fetched successfully.")

            return {"success": True, "data":
                        {
                            "city": weather_data['name'],
                            'temperature': weather_data['main']['temp'],
                            'description': weather_data['weather'][0]['description'],
                            'humidity': weather_data['main']['humidity']
                        }
                    }

        except Timeout:
            logger.exception("Weather API request failed with timeout error")
            return {"success": False, "message": "Weather service timed out."}

        except RequestException as e:
            logger.exception("Weather API request failed.")
            return {"success": False, "message": f"Unable to fetch weather details.{e}"}