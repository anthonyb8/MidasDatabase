# Generated by Django 4.2.7 on 2024-06-03 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("regression_analysis", "0002_alter_regressionanalysis_mae_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TimeSeriesData",
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
                ("timestamp", models.BigIntegerField(blank=True, null=True)),
                (
                    "daily_benchmark_return",
                    models.DecimalField(decimal_places=4, max_digits=15),
                ),
                (
                    "regression_analysis",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="timeseries_data",
                        to="regression_analysis.regressionanalysis",
                    ),
                ),
            ],
        ),
    ]
