from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_spectacular.utils import (extend_schema, OpenApiParameter, OpenApiResponse)

from .services import WeatherService


# Create your views here.


class WeatherAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get Current Weather",
        description="Returns the current weather information for a given city.",
        parameters=[
            OpenApiParameter(
                name="city",
                description="Name of the city",
                required=True,
                type=str,
            )
        ],
        responses={
            200: OpenApiResponse(description="Weather details fetched successfully."),
            400: OpenApiResponse(description="City parameter is missing."),
            500: OpenApiResponse(description="Weather service error."),
        },
    )
    def get(self, request):
        city = request.query_params.get("city")
        print(city)
        if not city:
            return Response({"success": False, "message": "City parameter is required"},
                            status=status.HTTP_400_BAD_REQUEST)
        data = WeatherService.get_current_weather(city)

        if data["success"]:
            return Response({"success": True, "data": data}, status=status.HTTP_200_OK)

        return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
