from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


class HealthCheckAPIView(APIView):
    authentication_classes = []
    permission_class = []

    def get(self, request):
        return Response({"status": "Healthy"})