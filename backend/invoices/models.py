from django.contrib.auth import get_user_model
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
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vat_rate = models.IntegerField(choices=VAT_RATE_CHOICES, default=VAT_RATE_CHOICES[0])
    comment = models.CharField(max_length=255)
    pkd = models.CharField(max_length=7)

    def __str__(self):
        return self.name


class Contractors(TimeStampModel):
    name = models.CharField(max_length=150)
    nip = models.CharField(max_length=14)
    street = models.CharField(max_length=150)
    address_2 = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Invoices(TimeStampModel):
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
