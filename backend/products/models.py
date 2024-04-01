from django.db import models

from utils.timestamp import TimeStampModel

VAT_RATE_CHOICES = [
    (23, "A stawka podstawowa podatku 23%"),
    (8, "B stawka obniżona podatku 8%"),
    (5, "C stawka obniżona podatku 5%"),
    (0, "D stawka obniżona podatku 0%"),
    (0, "E zwolnienie z podatku"),
]


class Products(TimeStampModel):
    """
    Model for product
    """
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vat_rate = models.IntegerField(choices=VAT_RATE_CHOICES, default=VAT_RATE_CHOICES[0])
    comment = models.CharField(max_length=255)
    pkd = models.CharField(max_length=7)

    def __str__(self):
        return self.name
