from rest_framework import routers
from django.conf.urls import url, include
from seller.views import VehicleViewSet

router = routers.DefaultRouter()
router.register(r"v1/vehicle", VehicleViewSet, basename="lab_search")

urlpatterns = [
	url(r"^", include(router.urls)),
]