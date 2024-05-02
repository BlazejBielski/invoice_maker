from django.urls import path

from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "contractors"

router = DefaultRouter()

router.register(r"contractors", viewsets.ContractorsViewSet, basename="contractor")

urlpatterns = [
    *router.urls,
]
