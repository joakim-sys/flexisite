# Generated by Django 4.2.9 on 2024-02-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pricing", "0002_alter_pricingtier_features"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pricingtier",
            name="features",
            field=models.ManyToManyField(blank=True, to="pricing.pricingfeature"),
        ),
    ]
