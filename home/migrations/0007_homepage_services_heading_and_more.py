# Generated by Django 4.2.9 on 2024-02-16 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0006_alter_homepage_about_cta_link"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="services_heading",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="services_subheading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="services_title",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
