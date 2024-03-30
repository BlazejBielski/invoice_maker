from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from invoices.models import Products, Invoices, Contractors
from invoices.serializers import InvoiceSerializer, ProductsSerializer, ContractorsSerializer


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoices.objects.all()
    serializer_class = InvoiceSerializer
    permission_classes = (IsAuthenticated,)


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)


class ContractorsViewSet(viewsets.ModelViewSet):
    queryset = Contractors.objects.all()
    serializer_class = ContractorsSerializer
    permission_classes = (IsAuthenticated,)
