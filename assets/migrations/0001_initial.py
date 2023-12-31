# Generated by Django 5.0 on 2023-12-21 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("symbol", models.CharField(max_length=10, unique=True)),
                ("type", models.CharField(max_length=50)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"unique_together": {("symbol", "type")},},
        ),
        migrations.CreateModel(
            name="Commodity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("commodity_name", models.CharField(max_length=25)),
                ("base_future_code", models.CharField(max_length=10)),
                ("expiration_date", models.DateTimeField()),
                ("industry", models.CharField(default="NULL", max_length=50)),
                ("exchange", models.CharField(blank=True, max_length=25, null=True)),
                ("currency", models.CharField(blank=True, max_length=3, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="commodity",
                        to="assets.asset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cryptocurrency",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cryptocurrency_name", models.CharField(max_length=50)),
                ("circulating_supply", models.IntegerField(blank=True, null=True)),
                ("market_cap", models.IntegerField(blank=True, null=True)),
                ("total_supply", models.IntegerField(blank=True, null=True)),
                ("max_supply", models.IntegerField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cryptocurrency",
                        to="assets.asset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Equity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("company_name", models.CharField(max_length=150)),
                ("exchange", models.CharField(max_length=25)),
                ("currency", models.CharField(blank=True, max_length=3, null=True)),
                ("industry", models.CharField(default="NULL", max_length=50)),
                ("description", models.TextField(blank=True, null=True)),
                ("market_cap", models.IntegerField(blank=True, null=True)),
                ("shares_outstanding", models.IntegerField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="equity",
                        to="assets.asset",
                    ),
                ),
            ],
        ),
    ]