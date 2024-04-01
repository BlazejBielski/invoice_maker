from django.db import models

from utils.timestamp import TimeStampModel


class Contractors(TimeStampModel):
    """
    Contractors model
    """
    name = models.CharField(max_length=150)
    nip = models.CharField(max_length=14)
    street = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    zip_code = models.CharField(max_length=10)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=8)

    def __str__(self):
        return self.name
