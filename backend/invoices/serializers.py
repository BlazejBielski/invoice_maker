from rest_framework import serializers
from invoices.models import Invoices, Products, Contractors


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = ("number", "products", "contractors", "owner", "amount", "comment", "sale_date", "issue_date", "payment_date")


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ("name", "price", "vat_rate", "comment", "pkd")


class ContractorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractors
        fields = ("name", "nip", "street", "address", "zip_code", "city", "country", "email", "phone")

