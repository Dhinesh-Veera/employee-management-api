from django.test import TestCase
from unittest.mock import patch, Mock
from requests.exceptions import Timeout
from .services import WeatherService


class WeatherServiceTest(TestCase):

    @patch("weather.services.requests.get")
    def test_get_current_weather_success(self, mock_get):

        mock_response = Mock()

        mock_response.json.return_value = {
            "name": "Chennai",
            "main": {
                "temp": 32,
                "humidity": 75
            },
            "weather": [
                {
                    "description": "clear sky"
                }
            ]
        }

        mock_response.raise_for_status.return_value = None

        mock_get.return_value = mock_response

        result = WeatherService.get_current_weather("Chennai")

        self.assertTrue(result["success"])
        self.assertEqual(result["data"]["city"], "Chennai")
        self.assertEqual(result["data"]["temperature"], 32)

    ################### Test Case 2 Timeout failure #################################
    @patch("weather.services.requests.get")
    def test_get_current_weather_timeout(self, mock_get):
        mock_get.side_effect = Timeout

        result = WeatherService.get_current_weather("Chennai")

        self.assertFalse(result["success"])
        self.assertEqual(
            result["message"],
            "Weather service timed out."
        )