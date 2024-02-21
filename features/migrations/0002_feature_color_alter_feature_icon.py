# Generated by Django 4.2.9 on 2024-02-16 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("features", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="feature",
            name="color",
            field=models.CharField(
                blank=True, help_text="Such as #e80368", max_length=20, null=True
            ),
        ),
        migrations.AlterField(
            model_name="feature",
            name="icon",
            field=models.CharField(
                blank=True, help_text="Such as ri-store-line", max_length=30, null=True
            ),
        ),
    ]