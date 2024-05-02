from django.urls import path

from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "products"

router = DefaultRouter()

router.register(r"products", viewsets.ProductsViewSet, basename="product")

urlpatterns = [
    *router.urls,
]
