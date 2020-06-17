from django.conf import settings
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response  # noqa
from django.http import HttpResponse
from seller.serializers import VehicleSerializer
from seller.models import Vehicle



class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()