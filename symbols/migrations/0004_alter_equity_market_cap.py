# Generated by Django 4.2.7 on 2024-04-18 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("symbols", "0003_rename_cryptocurrency_name_cryptocurrency_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="equity",
            name="market_cap",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
