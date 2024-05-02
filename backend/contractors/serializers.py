from rest_framework import serializers

from contractors.models import Contractors


class ContractorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = ("name", "nip", "street", "address", "zip_code", "city", "country", "email", "phone", "owner")

