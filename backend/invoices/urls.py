from django.urls import path

from rest_framework.routers import DefaultRouter

from . import viewsets

app_name = "invoices"

router = DefaultRouter()

router.register(r"invoices", viewsets.InvoiceViewSet, basename="product")

urlpatterns = [
    *router.urls,
]
