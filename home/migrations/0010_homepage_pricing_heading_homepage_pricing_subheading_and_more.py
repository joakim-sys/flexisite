# Generated by Django 4.2.9 on 2024-02-17 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0009_homepage_cta_descr_homepage_cta_link_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="pricing_heading",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="pricing_subheading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="pricing_title",
            field=models.CharField(
                blank=True,
                help_text="Should be one word such as, Pricing",
                max_length=100,
                null=True,
            ),
        ),
    ]
