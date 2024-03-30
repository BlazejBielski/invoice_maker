from rest_framework import serializers
from invoices.models import Invoices


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoices
        fields = ("number", "products", "contractors", "owner", "amount", "comment", "sale_date", "issue_date", "payment_date")
