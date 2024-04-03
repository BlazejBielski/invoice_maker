# Generated by Django 5.0.2 on 2024-04-01 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Products",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=8)),
                (
                    "vat_rate",
                    models.IntegerField(
                        choices=[
                            (23, "A stawka podstawowa podatku 23%"),
                            (8, "B stawka obniżona podatku 8%"),
                            (5, "C stawka obniżona podatku 5%"),
                            (0, "D stawka obniżona podatku 0%"),
                            (0, "E zwolnienie z podatku"),
                        ],
                        default=(23, "A stawka podstawowa podatku 23%"),
                    ),
                ),
                ("comment", models.CharField(max_length=255)),
                ("pkd", models.CharField(max_length=7)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]