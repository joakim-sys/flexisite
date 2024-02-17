# Generated by Django 4.2.9 on 2024-02-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_homepage_faq_heading_homepage_faq_subheading_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="contact_heading",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="contact_subheading",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="contact_title",
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
