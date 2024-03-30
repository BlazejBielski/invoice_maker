from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from contractors.models import Contractors
from contractors.serializers import ContractorsSerializer


class ContractorsViewSet(viewsets.ModelViewSet):
    queryset = Contractors.objects.all()
    serializer_class = ContractorsSerializer
    permission_classes = (IsAuthenticated,)
