# Generated by Django 4.2.7 on 2024-06-13 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("backtest", "0002_rename_price_trade_avg_price_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trade",
            name="trade_value",
            field=models.DecimalField(decimal_places=4, max_digits=15),
        ),
    ]
