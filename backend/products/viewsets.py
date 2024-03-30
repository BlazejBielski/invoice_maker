from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from products.models import Products
from products.serializers import ProductsSerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = (IsAuthenticated,)
