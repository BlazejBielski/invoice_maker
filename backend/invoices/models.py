from django.contrib.auth import get_user_model
from django.db import models

from contractors.models import Contractors
from products.models import Products
from utils.timestamp import TimeStampModel


class Invoices(TimeStampModel):
    """
    Invoices model
    """
    number = models.CharField()
    products = models.ForeignKey(Products, on_delete=models.DO_NOTHING)
    contractors = models.ForeignKey(Contractors, on_delete=models.DO_NOTHING)
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=4)
    comment = models.CharField(max_length=255)
    sale_date = models.DateField()
    issue_date = models.DateField()
    payment_date = models.DateField()

    def __str__(self):
        return f'{self.owner} + {self.number}'
