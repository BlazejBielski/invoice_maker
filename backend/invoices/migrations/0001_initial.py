# Generated by Django 5.0.2 on 2024-04-01 10:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contractors", "0001_initial"),
        ("products", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Invoices",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("number", models.CharField()),
                ("amount", models.IntegerField(default=1)),
                ("comment", models.CharField(max_length=255)),
                ("sale_date", models.DateField()),
                ("issue_date", models.DateField()),
                ("payment_date", models.DateField()),
                (
                    "contractors",
                    models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="contractors.contractors"),
                ),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ("products", models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to="products.products")),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
