# Generated by Django 5.0.1 on 2024-01-21 15:27

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
                (
                    "security_type",
                    models.CharField(
                        choices=[
                            ("EQUITY", "EQUITY"),
                            ("FUTURE", "FUTURE"),
                            ("OPTION", "OPTION"),
                        ],
                        max_length=10,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"unique_together": {("symbol", "security_type")},},
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
                ("currency", models.CharField(max_length=3)),
                ("industry", models.CharField(default="NULL", max_length=50)),
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
        migrations.CreateModel(
            name="Future",
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
                ("product_code", models.CharField(max_length=10)),
                ("product_name", models.CharField(max_length=50)),
                ("exchange", models.CharField(max_length=25)),
                ("contract_size", models.FloatField()),
                ("contract_units", models.CharField(max_length=20)),
                ("tick_size", models.FloatField()),
                ("min_price_fluctuation", models.FloatField()),
                ("last_trading_day", models.TextField()),
                ("trading_hours", models.TextField()),
                ("contract_months", models.CharField(max_length=100)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="future",
                        to="assets.asset",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Option",
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
                ("strike_price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("expiration_date", models.DateTimeField()),
                ("option_type", models.CharField(max_length=4)),
                ("contract_size", models.IntegerField()),
                ("underlying_name", models.CharField(max_length=50)),
                ("exchange", models.CharField(blank=True, max_length=25, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "asset",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="option",
                        to="assets.asset",
                    ),
                ),
            ],
        ),
    ]
